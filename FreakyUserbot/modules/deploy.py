"""Emoji
Available Commands:
.deploy"""


import asyncio

from FreakyUserbot import ALIVE_NAME, CMD_HELP
from FreakyUserbot.utils import Freaky_on_cmd

DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "Freak"


@Freaky.on(Freaky_on_cmd(pattern=r"deploy"))
async def _(event):

    if event.fwd_from:

        return

    animation_interval = 10

    animation_ttl = range(0, 12)

    # input_str = event.pattern_match.group(1)

    await event.edit("Deploying...")

    animation_chars = [
        "**Heroku Connecting To Latest Github Build (swatv3nub/FreakyUserbot)**",
        f"**Build started by user** **{DEFAULTUSER}**",
        f"**Deploy** `535a74f0` **by user** **{DEFAULTUSER}**",
        "**Restarting Heroku Server...**",
        "**State changed from up to starting**",
        "**Stopping all processes with SIGTERM**",
        "**Process exited with** `status 143`",
        "**Starting process with command** `python3 -m FreakyUserbot`",
        "**State changed from starting to up**",
        f"__INFO:FreakyUserbot:Logged in as {DEFAULTUSER}",
        "__INFO:FreakyUserbot:Successfully loaded all plugins__",
        "**Build Succeeded**",
    ]

    for i in animation_ttl:

        await asyncio.sleep(animation_interval)

        await event.edit(animation_chars[i % 12])


CMD_HELP.update({"deploy": ".deploy" "\nUsage show fake animation of deploy "})
