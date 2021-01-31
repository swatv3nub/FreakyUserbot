# For @UniBorg
# Courtesy @yasirsiddiqui

"""
.bye
"""
import time

from telethon.tl.functions.channels import LeaveChannelRequest

from FreakyUserbot import CMD_HELP
from FreakyUserbot.utils import Freaky_on_cmd, edit_or_reply, sudo_cmd


@Freaky.on(Freaky_on_cmd("bye", outgoing=True))
@Freaky.on(sudo_cmd("bye", allow_sudo=True))
async def leave(e):
    FreakyUserbot = await edit_or_reply(e, "Bye Kek")
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        await FreakyUserbot.edit("`I am leaving this chat.....!`")
        time.sleep(3)
        if "-" in str(e.chat_id):
            await borg(LeaveChannelRequest(e.chat_id))
        else:
            await FreakyUserbot.edit("`Sir This is Not A Group`")


CMD_HELP.update(
    {
        "bye": "**Bye**\
\n\n**Syntax : **`.bye`\
\n**Usage :** use this plugin to leave a group."
    }
)
