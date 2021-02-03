"""Emoji
Available Commands:
.extraplugs
GitLink + Channel Link
"""


import asyncio

from FreakyUserbot.utils import Freaky_on_cmd


@Freaky.on(Freaky_on_cmd("extraplugs"))
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 1
    animation_ttl = range(0, 36)
    # input_str = event.pattern_match.group(1)
    # if input_str == "support":
    await event.edit("Extra Plugins")
    animation_chars = [
        "Click here",
        "[Github](https://github.com/swatv3nub/FreakyPlugs) or Request External Plugins [Here](https://t.me/AskPlugins)",
    ]

    for i in animation_ttl:

        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 18])
