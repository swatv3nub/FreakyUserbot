from asyncio import wait

from telethon import events

from FreakyUserbot import CMD_HELP
from FreakyUserbot.utils import Freaky_on_cmd


@borg.on(Freaky_on_cmd(pattern=r"hola"))
async def hi(event):
    if event.fwd_from:
        return
    await event.edit("╔┓┏╦━╦┓╔┓╔━━╗\n║┗┛║┗╣┃║┃║X X  ║\n║┏┓║┏╣┗╣┗╣╰╯║\n╚┛┗╩━╩━╩━╩━━╝")


@borg.on(Freaky_on_cmd(pattern=r"plus"))
async def hi(event):
    if event.fwd_from:
        return
    await event.edit(
        "╭━━━━━━━━━━━━━╮\n┃╱╱╱╱╱╱╱╱┏┓╱╱╱┃\n┃╱╱╱┏┓╱╱┏╯┃╱╱╱┃\n┃╱╱┏┛┗┓╱┗┓┃╱╱╱┃\n┃╱╱┗┓┏┛╱╱┃┃╱╱╱┃\n┃╱╱╱┗┛╱╱╱┃┃╱╱╱┃\n┃╱╱╱╱╱╱╱╱┗┛╱╱╱┃\n╰━━━━━━━━━━━━━╯"
    )


@borg.on(Freaky_on_cmd(pattern=r"yes"))
async def hi(event):
    if event.fwd_from:
        return
    await event.edit(
        "┏┓┏┓╭━━┓╭━━╮▕▔▔▏\n┃┃┃┃┃┏━┛┃╭━┛▕┈┈▏\n┃╰╯┃┃┗━┓┃╰━╮▕┈┈▏\n╰━╮┃┃┏━┛╰━╮┃┈╲╱┈\n┏━╯┃┃┗━┓┏━╯┃┈╭╮┈\n╰━━╯╰━━┛╰━━╯┈╰╯┈"
    )


@borg.on(Freaky_on_cmd(pattern=r"lol"))
async def hi(event):
    if event.fwd_from:
        return
    await event.edit(
        "▂▂╱▔▔▔▔▔▔▔▔▔▔▔▔╲\n╲▂┈╭╮┈┈╭━━╮╭╮┈┈▕\n┈┈▏┃┃┈┈┃╭╮┃┃┃┈┈▕\n┈┈▏┃╰━╮┃╰╯┃┃╰━╮▕\n┈┈▏╰━━╯╰━━╯╰━━╯▕\n┈┈╲▂▂▂▂▂▂▂▂▂▂▂▂╱"
    )


@borg.on(Freaky_on_cmd(pattern=r"android"))
async def hi(event):
    if event.fwd_from:
        return
    await event.edit(
        "┈┈┈╲┈┈┈┈╱┈┈┈┈┈┈┈\n┈┈┈╱▔▔▔▔╲┈┈┈┈┈┈┈\n┈┈┃┈▇┈┈▇┈┃┈┈┈┈┈┈\n╭╮┣━━━━━━┫╭╮┈┈┈┈\n┃┃┃┈┈┈┈┈┈┃┃┃┈┈┈┈\n╰╯┃┈┈┈┈┈┈┃╰╯┈┈┈┈\n┈┈╰┓┏━━┓┏╯┈┈┈┈┈┈\n┈┈┈╰╯┈┈╰╯┈┈┈┈┈┈┈"
    )


@borg.on(Freaky_on_cmd(pattern=r"hmm"))
async def hi(event):
    if event.fwd_from:
        return
    await event.edit(
        "┈┈╱▔▔▔▔▔╲┈┈┈HM┈HM\n┈╱┈┈╱▔╲╲╲▏┈┈┈HMMM\n╱┈┈╱━╱▔▔▔▔▔╲━╮┈┈\n▏┈▕┃▕╱▔╲╱▔╲▕╮┃┈┈\n▏┈▕╰━▏▊▕▕▋▕▕━╯┈┈\n╲┈┈╲╱▔╭╮▔▔┳╲╲┈┈┈\n┈╲┈┈▏╭━━━━╯▕▕┈┈┈\n┈┈╲┈╲▂▂▂▂▂▂╱╱┈┈┈\n┈┈┈┈▏┊┈┈┈┈┊┈┈┈╲┈\n┈┈┈▏┊┈┈┈┈┊▕╲┈┈╲\n┈╱▔╲▏┊┈┈┈┈┊▕╱▔╲▕\n┈▏┈┈┈╰┈┈┈┈╯┈┈┈▕▕\n┈╲┈┈┈╲┈┈┈┈╱┈┈┈╱┈╲\n┈┈╲┈┈▕▔▔▔▔▏┈┈╱╲╲╲▏\n┈╱▔┈┈▕┈┈┈┈▏┈┈▔╲▔▔\n┈╲▂▂▂╱┈┈┈┈╲▂▂▂╱┈"
    )


@borg.on(Freaky_on_cmd(pattern=r"happybirthday"))
async def hi(event):
    if event.fwd_from:
        return
    await event.edit(
        "¸.•°*”˜˜”*°•.¸☆ ★ ☆¸.•°*”˜˜”*°\n╔╗╔╦══╦═╦═╦╗╔╗ ★ ★ \n║╚╝║══║═║═║╚╝║ ☆¸.•° \n║╔╗║╔╗║╔╣╔╩╗╔╝ ★\n╚╝╚╩╝╚╩╝╚╝═╚╝★Birthday!★"
    )


@borg.on(Freaky_on_cmd(pattern=r"WTF"))
async def hi(event):
    if event.fwd_from:
        return
    await event.edit(
        "┏┓┏┓┏┓┏━━━┓┏━━━┓\n┃┃┃┃┃┃┗┓╱┏┛┃╱┏━┛\n┃┗┛┗┛┃┈┃╱┃┈┃╱┗┓\n┃╱╱╱╱┃┈┃╱┃┈┃╱┏┛\n┗━━━━┛◯┗━┛◯┗━┛◯"
    )


@borg.on(Freaky_on_cmd(pattern=r"lmao"))
async def hi(event):
    if event.fwd_from:
        return
    await event.edit(
        "┏┓┈╭━━╮╭━━╮╭━━╮\n┃┃┈┃┃┃┃┃╭╮┃┃╭╮┃\n┃┗┓┃┃┃┃┃┏┓┃┃╰╯┃\n┗━┛┗┻┻┛┗┛┗┛╰━━╯"
    )


@borg.on(events.NewMessage(pattern=r"\.spam", outgoing=True))
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


@borg.on(Freaky_on_cmd(pattern=r"no"))
async def hi(event):
    if event.fwd_from:
        return
    await event.edit(
        "███╗░░██╗░█████╗░ \n████╗░██║██╔══██╗ \n██╔██╗██║██║░░██║ \n██║╚████║██║░░██║ \n██║░╚███║╚█████╔╝ \n╚═╝░░╚══╝░╚════╝░ "
    )


CMD_HELP.update(
    {
        "artist": "**Artist**\
\n\n**Syntax : **`.hola, .plus, .android, .lol, .yes, .hmm, .happybirthday, .WTF, .lmao, .no`\
\n**Usage :** ASCII Plugin"
    }
)
