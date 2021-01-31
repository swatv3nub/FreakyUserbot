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


"""Invite the user(s) to the current chat
Syntax: .invite <User(s)>"""

from telethon import functions

from FreakyUserbot import CMD_HELP
from FreakyUserbot.utils import Freaky_on_cmd, sudo_cmd

"""Invite the user(s) to the current chat
Syntax: .invite <User(s)>"""

from telethon import functions

from FreakyUserbot.utils import Freaky_on_cmd, edit_or_reply, sudo_cmd


@Freaky.on(Freaky_on_cmd(pattern="invite ?(.*)"))
@Freaky.on(sudo_cmd(pattern="invite ?(.*)", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    to_add_users = event.pattern_match.group(1)
    if event.is_private:
        await edit_or_reply(
            event, "`.invite` users to a chat, not to a Private Message"
        )
    else:
        logger.info(to_add_users)
        if not event.is_channel and event.is_group:
            # https://lonamiwebs.github.io/Telethon/methods/messages/add_chat_user.html
            for user_id in to_add_users.split(" "):
                try:
                    await borg(
                        functions.messages.AddChatUserRequest(
                            chat_id=event.chat_id, user_id=user_id, fwd_limit=1000000
                        )
                    )
                except Exception as e:
                    await event.reply(str(e))
            await event.edit("Invited Successfully")
        else:
            # https://lonamiwebs.github.io/Telethon/methods/channels/invite_to_channel.html
            for user_id in to_add_users.split(" "):
                try:
                    await borg(
                        functions.channels.InviteToChannelRequest(
                            channel=event.chat_id, users=[user_id]
                        )
                    )
                except Exception as e:
                    await event.reply(str(e))
            await edit_or_reply(event, "Invited Successfully")


CMD_HELP.update(
    {
        "add": "**Add**\
\n\n**Syntax : **`.add <user_id or user-name>`\
\n**Usage :** Adds User To Group"
    }
)
