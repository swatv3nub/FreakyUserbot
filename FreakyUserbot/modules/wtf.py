"""Emoji

Available Commands:

.wtf"""


import asyncio

from FreakyUserbot import CMD_HELP
from FreakyUserbot.utils import Freaky_on_cmd


@Freaky.on(Freaky_on_cmd("wtf"))
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 0.3
    animation_ttl = range(0, 5)
    await event.edit("wtf")
    animation_chars = [
        "What",
        "What The",
        "What The F",
        "What The F Brah",
        "[What The F Brah](https://telegra.ph/file/63a02b3ef3245b321e54a.jpg)",
    ]

    for i in animation_ttl:

        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 5])


CMD_HELP.update(
    {
        "wtf": "Wtf\
\n\nSyntax : .wtf <reply>\
\nUsage : Fun Plugin"
    }
)
