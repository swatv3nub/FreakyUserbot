# For @UniBorg
# Courtesy @yasirsiddiqui

"""
.bye
"""
import time

from telethon.tl.functions.channels import LeaveChannelRequest

from HackfreaksUserbot import CMD_HELP
from HackfreaksUserbot.utils import Hackfreaks_on_cmd, edit_or_reply, sudo_cmd


@Hackfreaks.on(Hackfreaks_on_cmd("bye", outgoing=True))
@Hackfreaks.on(sudo_cmd("bye", allow_sudo=True))
async def leave(e):
    hackfreaksuserbot = await edit_or_reply(e, "Bye Kek")
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        await hackfreaksuserbot.edit("`I am leaving this chat.....!`")
        time.sleep(3)
        if "-" in str(e.chat_id):
            await borg(LeaveChannelRequest(e.chat_id))
        else:
            await hackfreaksuserbot.edit("`Sir This is Not A Group`")


CMD_HELP.update(
    {
        "bye": "**Bye**\
\n\n**Syntax : **`.bye`\
\n**Usage :** use this plugin to leave a group."
    }
)
