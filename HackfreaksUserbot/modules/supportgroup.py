"""Emoji
Available Commands:
.support
Support Channel/Group
"""


import asyncio

from HackfreaksUserbot.utils import Hackfreaks_on_cmd


@Hackfreaks.on(Hackfreaks_on_cmd("Hackfreaks"))
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 0.1
    animation_ttl = range(0, 36)
    # input_str = event.pattern_match.group(1)
    # if input_str == "support":
    await event.edit("for our support group")
    animation_chars = [
        "Click here",
        "[Support](https://t.me/HackfreaksUserbot)",
    ]

    for i in animation_ttl:

        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 18])
