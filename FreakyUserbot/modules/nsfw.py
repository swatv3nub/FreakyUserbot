#    Copyright (C) DevsExpo 2020-2021
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <https://www.gnu.org/licenses/>.

from telethon import events
from telethon.tl.functions.channels import EditBannedRequest
from telethon.tl.types import ChatBannedRights

from FreakyUserbot.functions import is_admin, is_nsfw
from FreakyUserbot.modules.sql_helper.nsfw_sql import (
    add_nsfwatch,
    get_all_nsfw_enabled_chat,
    is_nsfwatch_indb,
    rmnsfwatch,
)
from FreakyUserbot.utils import Freaky_on_cmd

MUTE_RIGHTS = ChatBannedRights(until_date=None, send_messages=False)


@Freaky.on(Freaky_on_cmd(pattern="addnsfw$"))
async def nsfw_watch(event):
    if not event.is_group:
        await event.edit("**NSFW WATCH CAN ONLY BE ENABLED IN GROUPS**.")
        return
    if not await is_admin(event, bot.uid):
        await event.edit("`NO PERMISSION!`")
        return
    if is_nsfwatch_indb(str(event.chat_id)):
        await event.edit("`NSFW WATCH Already Enabled.`")
        return
    add_nsfwatch(str(event.chat_id))
    await event.edit(
        f"**Added Chat {event.chat.title} With ID {event.chat_id} To Database. This Groups NSFW Contents Will Be Deleted And Logged in Logging Group**"
    )


@Freaky.on(Freaky_on_cmd(pattern="rmnsfw$"))
async def disable_nsfw(event):
    if not event.is_group:
        await event.edit("**NSFW WATCH CAN ONLY BE DISABLED IN GROUPS**.")
        return
    if not await is_admin(event, bot.uid):
        await event.edit("`NO PERMISSIONS!`")
        return
    if not is_nsfwatch_indb(str(event.chat_id)):
        await event.edit("NSFW WATCH is Already Turned Off.")
        return
    rmnsfwatch(str(event.chat_id))
    await event.edit(
        f"**Removed Chat {event.chat.title} With Id {event.chat_id} From NSFW Watch**"
    )


@bot.on(events.NewMessage())
async def ws(event):
    noob_nibba = get_all_nsfw_enabled_chat()
    if len(noob_nibba) == 0:
        return
    if not is_nsfwatch_indb(str(event.chat_id)):
        return
    if not event.media:
        return
    if not (
        event.gif or event.video or event.video_note or event.photo or event.sticker
    ):
        return
    if not await is_admin(event, bot.uid):
        return
    hmmnibba = await is_nsfw(event)
    his_id = event.sender_id
    if hmmnibba is True:
        try:
            await event.delete()
            await event.client(EditBannedRequest(event.chat_id, his_id, MUTE_RIGHTS))
        except:
            pass
        lolchat = await event.get_chat()
        ctitle = event.chat.title
        if lolchat.username:
            hehe = lolchat.username
        else:
            hehe = event.chat_id
        wnibba = await event.client.get_entity(his_id)
        if wnibba.username:
            nibbi = wnibba.username
        else:
            nibbi = wnibba.id
        try:
            await borg.send_message(
                Config.PRIVATE_GROUP_ID,
                f"**#NSFW_WATCH** \n**Chat :** `{hehe}` \n**Nsfw Sender - User / Bot :** `{nibbi}` \n**Chat Title:** `{ctitle}`",
            )
            return
        except:
            return
