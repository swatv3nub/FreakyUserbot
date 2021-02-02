# Assamese Abuse made for @FreakyUserbot
# By @swatv3nub // Yes, First Self-Written File in this Userbot...LOL

import asyncio

from FreakyUserbot import CMD_HELP
from FreakyUserbot.utils import Freaky_on_cmd


@Freaky.on(Freaky_on_cmd(pattern=r"kela"))
async def _(event):

    if event.fwd_from:
        return
    animation_interval = 1
    animation_ttl = range(0, 36)
    # input_str = event.pattern_match.group(1)
    # if input_str == "kela":
    await event.edit("Kela O")
    animation_chars = [
        "Oi",
        "Kela",
        "Kun Beh Toi",
        "Bohai Bohai Sudim",
        "Kela Sini Pua nai muk",
        "Oi Sutmaroni Kela",
        "Koti maarim Kela",
        "Sudurbhai",
        "Ja kela Leura",
        "Koti Maarge Rendi Kela",
        "Hizira Kela Hizira",
        "Rendi Suda",
        "Maira Suda",
        "Laz nai ne kela",
        "Etiya u Porhi Aso",
        "Bhag Chutia Kela",
    ]

    for i in animation_ttl:

        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 18])


CMD_HELP.update(
    {
        "kela": "Kela\
\n\nSyntax : .kela\
\nUsage : Want Assamese Gaali, Use this, LUL"
    }
)
