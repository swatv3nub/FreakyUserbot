from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError

from FreakyUserbot import CMD_HELP
from FreakyUserbot.utils import Freaky_on_cmd


@Freaky.on(Freaky_on_cmd("grab ?(.*)"))
async def _(event):
    if event.fwd_from:
        return
    if not event.reply_to_msg_id:
        await event.edit("```Reply to any user message.```")
        return
    reply_message = await event.get_reply_message()
    if not reply_message.media:
        await event.edit("```reply to text message```")
        return
    chat = "@ThemerBot"
    reply_message.sender
    if reply_message.sender.bot:
        await event.edit("```Reply to actual users message.```")
        return
    await event.edit("```Processing```")
    async with Freaky.conversation(chat) as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=864838521)
            )
            await Freaky.forward_messages(chat, reply_message)
            response = await response
        except YouBlockedUserError:
            await event.reply("```Please unblock @sangmatainfo_bot and try again```")
            return
        if response.text.startswith("Hi"):
            await event.edit(
                "```can you kindly disable your forward privacy settings for good?```"
            )
        else:
            await Freaky.send_file(event.chat_id, response.message)


CMD_HELP.update(
    {
        "grab": "**Grab**\
\n\n**Syntax : **`.grab`\
\n**Usage :** Reply to User."
    }
)
