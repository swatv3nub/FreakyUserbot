#    Hackfreaks - UserBot
#    Copyright (C) 2020 Hackfreaks

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


"""Emoji
Available Commands:
.support
"""


import asyncio

from HackfreaksUserbot import CMD_HELP
from HackfreaksUserbot.utils import Hackfreaks_on_cmd


@Hackfreaks.on(Hackfreaks_on_cmd("HackfreaksBot"))
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 0.1
    animation_ttl = range(0, 36)
    # input_str = event.pattern_match.group(1)
    # if input_str == "Read This Telegraph Whole info here":
    await event.edit("Thanks")
    animation_chars = [
        "Click here to Go to Telegraph",
        "[Click Here For Guide](https://telegra.ph/file/63a02b3ef3245b321e54a.jpg)",
    ]

    for i in animation_ttl:

        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 18])


CMD_HELP.update(
    {
        "HackfreaksBot": "HackfreaksBot\
\n\nSyntax : .support\
\nUsage : Join @HackfreaksUserbot"
    }
)
