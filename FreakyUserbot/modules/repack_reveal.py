#  (c)2020 TeleBot
#
# You may not use this plugin without proper authorship and consent from TeleBotSupport
#
# Creted by @buddhhu, @itzsjdude
#
import asyncio
import os

from FreakyUserbot import CMD_HELP
from FreakyUserbot.utils import Freaky_on_cmd, sudo_cmd


@Freaky.on(Freaky_on_cmd(pattern="repack ?(.*)", outgoing=True))
@Freaky.on(sudo_cmd(pattern="repack ?(.*)", allow_sudo=True))
async def _(event):
    a = await event.get_reply_message()
    input_str = event.pattern_match.group(1)
    b = open(input_str, "w")
    b.write(str(a.message))
    b.close()
    a = await event.reply(f"**Packing into** `{input_str}`")
    await asyncio.sleep(2)
    await a.edit(f"**Uploading** `{input_str}`")
    await asyncio.sleep(2)
    await event.client.send_file(event.chat_id, input_str)
    await a.delete()
    os.remove(input_str)


@Freaky.on(Freaky_on_cmd(pattern="reveal ?(.*)", outgoing=True))
@Freaky.on(sudo_cmd(pattern="reveal ?(.*)", allow_sudo=True))
async def _(event):
    b = await event.client.download_media(await event.get_reply_message())
    a = open(b, "r")
    c = a.read()
    a.close()
    a = await event.reply("**Reading file...**")
    if len(c) > 4095:
        await a.edit("`The Total words in this file is more than telegram limits.`")
    else:
        await event.client.send_message(event.chat_id, f"```{c}```")
        await a.delete()
    os.remove(b)


CMD_HELP.update(
    {
        "repack_reveak": "**Repack_Reveal**\
\n\n**Syntax : **`.repack <filename.extension> <reply to text>`\
\n**Usage :** Pack the text and send as a file.\
\n\n**Syntax : **`.reveal <reply to a file>`\
\n**Usage :** Read contents of file and send as a telegram message."
    }
)
