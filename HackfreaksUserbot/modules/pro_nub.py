"""Available Commands:

.unoob
.menoob
.upro
.mepro

@arnab431"""


import asyncio

from HackfreaksUserbot import CMD_HELP
from HackfreaksUserbot.utils import Hackfreaks_on_cmd


@Hackfreaks.on(Hackfreaks_on_cmd("(.*)"))
async def _(event):

    if event.fwd_from:

        return

    animation_interval = 0.5

    animation_ttl = range(0, 9)

    input_str = event.pattern_match.group(1)

    if input_str == "unoob":

        await event.edit(input_str)

        animation_chars = [
            "EvErYbOdY",
            "iZ",
            "BiGGeSt",
            "NoOoB",
            "uNtiL",
            "YoU",
            "aRriVe",
            "😈",
            "EvErYbOdY iZ BiGGeSt NoOoB uNtiL YoU aRriVe 😈",
        ]

        for i in animation_ttl:

            await event.edit(animation_chars[i % 9])
            await asyncio.sleep(animation_interval)


@Hackfreaks.on(Hackfreaks_on_cmd("(.*)"))
async def _(event):

    if event.fwd_from:

        return

    animation_interval = 0.5

    animation_ttl = range(0, 9)

    input_str = event.pattern_match.group(1)

    if input_str == "menoob":

        await event.edit(input_str)

        animation_chars = [
            "EvErYbOdY",
            "iZ",
            "BiGGeSt",
            "NoOoB",
            "uNtiL",
            "i",
            "aRriVe",
            "😈",
            "EvErYbOdY iZ BiGGeSt NoOoB uNtiL i aRriVe 😈",
        ]

        for i in animation_ttl:

            await event.edit(animation_chars[i % 9])
            await asyncio.sleep(animation_interval)


@Hackfreaks.on(Hackfreaks_on_cmd("(.*)"))
async def _(event):

    if event.fwd_from:

        return

    animation_interval = 0.5

    animation_ttl = range(0, 8)

    input_str = event.pattern_match.group(1)

    if input_str == "upro":

        await event.edit(input_str)

        animation_chars = [
            "EvErYbOdY",
            "iZ",
            "PeRu",
            "uNtiL",
            "YoU",
            "aRriVe",
            "😈",
            "EvErYbOdY iZ PeRu uNtiL YoU aRriVe 😈",
        ]

        for i in animation_ttl:

            await event.edit(animation_chars[i % 8])
            await asyncio.sleep(animation_interval)


@Hackfreaks.on(Hackfreaks_on_cmd("(.*)"))
async def _(event):

    if event.fwd_from:

        return

    animation_interval = 0.5

    animation_ttl = range(0, 8)

    input_str = event.pattern_match.group(1)

    if input_str == "mepro":

        await event.edit(input_str)

        animation_chars = [
            "EvErYbOdY",
            "iZ",
            "PeRu",
            "uNtiL",
            "i",
            "aRriVe",
            "😈",
            "EvErYbOdY iZ PeRu uNtiL i aRriVe 😈",
        ]

        for i in animation_ttl:

            await event.edit(animation_chars[i % 8])
            await asyncio.sleep(animation_interval)


CMD_HELP.update(
    {
        "pro_nub": "Pro_Nob\
\n\nSyntax : .unoob, .menoob, upro, .mepro\
\nUsage : Amazing Plugin To Give Respect"
    }
)
