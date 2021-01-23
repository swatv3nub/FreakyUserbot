from telethon import events

from HackfreaksUserbot import CMD_HELP


@Hackfreaks.on(events.NewMessage(pattern=r"^.note (.*)", outgoing=True))
async def test(event):
    if event.fwd_from:
        return
    uwu = event.pattern_match.group(1)
    await event.edit("Added note to Evernote".format(uwu))
    await Hackfreaks.send_message("@ifttt", "#note {}".format(uwu))


CMD_HELP.update(
    {
        "everynote": "**Everynote**\
\n\n**Syntax : **`.note <text>`\
\n**Usage :** Saves The Note."
    }
)
