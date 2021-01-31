# Ported from other Telegram UserBots for TeleBot//Made for TeleBot
# Kangers, don't remove this line
# @xditya
# Rewriten by @swatv3nub
# Made for @FreakyUserbot
# Knagers keep the credit

#    Freaky - Userbot
#    Copyright (C) 2020 Freaky

#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.

#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.

#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <https://www.gnu.org/licenses/>.


"""COMMAND : .pbio, .ppic, .pname, .delpfp {n}"""

import os

from telethon.tl import functions
from telethon.tl.functions.photos import DeletePhotosRequest, GetUserPhotosRequest
from telethon.tl.types import InputPhoto

from FreakyUserbot import CMD_HELP
from FreakyUserbot.utils import Freaky_on_cmd


@Freaky.on(Freaky_on_cmd(pattern="pbio (.*)"))
async def _(event):
    if event.fwd_from:
        return
    bio = event.pattern_match.group(1)
    try:
        await borg(functions.account.UpdateProfileRequest(about=bio))
        await event.edit("Succesfully changed my profile bio")
    except Exception as e:  # pylint:disable=C0103,W0703
        await event.edit(str(e))


@Freaky.on(Freaky_on_cmd(pattern="pname ((.|\n)*)"))
async def _(event):
    if event.fwd_from:
        return
    names = event.pattern_match.group(1)
    first_name = names
    last_name = ""
    if "\\n" in names:
        first_name, last_name = names.split("\\n", 1)
    try:
        await borg(
            functions.account.UpdateProfileRequest(
                first_name=first_name, last_name=last_name
            )
        )
        await event.edit("My name was changed successfully")
    except Exception as e:
        await event.edit(str(e))


@Freaky.on(Freaky_on_cmd(pattern="ppic"))
async def _(event):
    if event.fwd_from:
        return
    reply_message = await event.get_reply_message()
    await event.edit("Downloading Profile Picture to my local ...")
    if not os.path.isdir(Config.TMP_DOWNLOAD_DIRECTORY):
        os.makedirs(Config.TMP_DOWNLOAD_DIRECTORY)
    photo = None
    try:
        photo = await borg.download_media(  # pylint:disable=E0602
            reply_message, Config.TMP_DOWNLOAD_DIRECTORY
        )
    except Exception as e:  # pylint:disable=C0103,W0703
        await event.edit(str(e))
    else:
        if photo:
            await event.edit("now, Uploading to @Telegram ...")
            file = await borg.upload_file(photo)  # pylint:disable=E0602
            try:
                await borg(functions.photos.UploadProfilePhotoRequest(file))
            except Exception as e:  # pylint:disable=C0103,W0703
                await event.edit(str(e))
            else:
                await event.edit("My profile picture was succesfully changed")
    try:
        os.remove(photo)
    except Exception as e:
        logger.warn(str(e))


@Freaky.on(Freaky_on_cmd(pattern="delpfp ?(.*)"))
async def remove_profilepic(delpfp):
    """ For .delpfp command, delete your current profile picture in Telegram. """
    group = delpfp.text[8:]
    if group == "all":
        lim = 0
    elif group.isdigit():
        lim = int(group)
    else:
        lim = 1

    pfplist = await delpfp.client(
        GetUserPhotosRequest(user_id=delpfp.from_id, offset=0, max_id=0, limit=lim)
    )
    input_photos = []
    for sep in pfplist.photos:
        input_photos.append(
            InputPhoto(
                id=sep.id,
                access_hash=sep.access_hash,
                file_reference=sep.file_reference,
            )
        )
    await delpfp.client(DeletePhotosRequest(id=input_photos))
    await delpfp.edit(f"`Successfully deleted {len(input_photos)} profile picture(s).`")


CMD_HELP.update(
    {
        "account_edits": "➟ .pbio <text>\n     To change your profile bio to <text>.\
         \n\n➟ .pname <name>\n     Change your profile name to <name>.\
         \n\n➟ .ppic (reply to pic)\n      To change your profile pic to the replied picture.\
         \n\n➟ .delpfp <number>(optional)\n    To delete 'n' number of profile pics, one if no number specified."
    }
)
