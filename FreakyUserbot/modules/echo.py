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

"""
Echoes the message via your bot
"""

from FreakyUserbot import CMD_HELP
from FreakyUserbot.utils import Freaky_on_cmd, sudo_cmd


@Freaky.on(Freaky_on_cmd(pattern=r"echo (.*)"))
@Freaky.on(sudo_cmd(pattern=r"echo ( .*)", allow_sudo=True))
async def _(event):
    bxt = Var.TG_BOT_USER_NAME_BF_HER
    try:
        tex = str(event.text[6:])
        await freakybot.send_message(event.chat_id, tex)
        await event.delete()
    except BaseException:
        await event.client.send_message(event.chat_id, f"Please add @{bxt} here first!")
        await event.delete()


CMD_HELP.update(
    {
        "echo": ".echo <mssg>\nUse - Echoes the message you send via your bot. You must add it to this chat first, ofc."
    }
)
