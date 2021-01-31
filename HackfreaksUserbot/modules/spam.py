from asyncio import wait

from telethon import events

from FreakyUserbot import CMD_HELP


@Freaky.on(events.NewMessage(pattern=r"\.spam", outgoing=True))
async def spammer(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        message = e.text
        counter = int(message[6:8])
        spam_message = str(e.text[8:])

        await wait([e.respond(spam_message) for i in range(counter)])

        await e.delete()
        if LOGGER:
            await e.client.send_message(
                LOGGER_GROUP, "#SPAM \n\n" "Spam was executed successfully"
            )


CMD_HELP.update(
    {
        "spam": "Spam\
\n\nSyntax : .spam <numaric value> <text>\
\nUsage : Spamming PLugin Must Try On Yourself Becasue This Causes FloodWait"
    }
)
