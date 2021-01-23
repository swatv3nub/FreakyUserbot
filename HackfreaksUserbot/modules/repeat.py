from asyncio import wait

from HackfreaksUserbot.utils import Hackfreaks_on_cmd


@Hackfreaks.on(Hackfreaks_on_cmd("repeat ?(.*)"))
async def _(event):
    message = event.text[10:]
    count = int(event.text[8:10])
    repmessage = message * count
    await wait([event.respond(repmessage) for i in range(count)])
    await event.delete()
