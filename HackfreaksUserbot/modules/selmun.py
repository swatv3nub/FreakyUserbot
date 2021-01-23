# Credit To @Kraken_The_BadASS . Keep credit if you are going to edit it.


import asyncio

from HackfreaksUserbot import CMD_HELP
from HackfreaksUserbot.utils import Hackfreaks_on_cmd


@Hackfreaks.on(Hackfreaks_on_cmd(pattern="selmun ?(.*)"))
async def _(event):
    if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        await event.edit("😁Selmun Bhoi wants to go on a Ride😨")
        await asyncio.sleep(2)
        await event.edit("🚘🚘🚘\n🚗🚗🚗\n🚘🚘🚘\n🚗🚗🚗")
        await asyncio.sleep(1)
        await event.edit("🚗🚗🚗\n🚘🚘🚘\n🚗🚗🚗\n🚘🚘🚘")
        await asyncio.sleep(1)
        await event.edit("🚘🚘🚘\n🚗🚗🚗\n🚘🚘🚘\n🚗🚗🚗")
        await asyncio.sleep(1)
        await event.edit("🚗🚗🚗\n🚘🚘🚘\n🚗🚗🚗\n🚘🚘🚘")
        await asyncio.sleep(1)
        await event.edit(
            "🙁Selmun Bhoi Iz feeling Hungry😖 \nAlso he iz big fan of Bear Grills🤫😬"
        )
        await asyncio.sleep(2.4)
        await event.edit("A Blackbuck iz spooted🦌")
        await asyncio.sleep(1.9)
        await event.edit("😨Bhoi takes Out his Crossbow?🏹")
        await asyncio.sleep(1.8)
        await event.edit("Rest Iz Mystery🤫 \nThat blackbuck🦌 was never found again😨")
        await asyncio.sleep(2)
        await event.edit("Bhoi Iz going back to his home")
        await asyncio.sleep(2)
        await event.edit("I don't know how😨 \nBut he iz no more hungry🤫🦌")
        await asyncio.sleep(2)
        await event.edit("He iz heading back to his home")
        await asyncio.sleep(2)
        await event.edit("🚘🚘🚘\n🚗🚗🚗\n🚘🚘🚘\n🚗🚗🚗")
        await asyncio.sleep(1)
        await event.edit("🚗🚗🚗\n🚘🚘🚘\n🚗🚗🚗\n🚘🚘🚘")
        await asyncio.sleep(1)
        await event.edit("🚘🚘🚘\n🚗🚗🚗\n🚘🚘🚘\n🚗🚗🚗")
        await asyncio.sleep(1)
        await event.edit("🚗🚗🚗\n🚘🚘🚘\n🚗🚗🚗\n🚘🚘🚘")
        await asyncio.sleep(1)
        await event.edit("Selmun Bhoi reached home🙂 \nAnd went to sleep😴🛌")
        await asyncio.sleep(2)
        await event.edit(
            "Next Day \n2 Poor people \nWho used to sleep on foothpath \nWere reported ded⚰️🥀"
        )
        await asyncio.sleep(2.5)
        await event.edit(
            "Selmun bhoi drove his car from that road last night🌃 \nRest is a mystery......."
        )
        await asyncio.sleep(2.2)
        await event.edit("**R**")
        await asyncio.sleep(0.2)
        await event.edit("**R** \n**I**")
        await asyncio.sleep(0.2)
        await event.edit("**R** \n**I** \n**P**")
        await asyncio.sleep(0.2)
        await event.edit("**⚰️🦌RIP🦌⚰️**")


CMD_HELP.update(
    {
        "selmun": "Selmun\
\n\nSyntax : .selmun\
\nUsage : Try YourSelf"
    }
)
