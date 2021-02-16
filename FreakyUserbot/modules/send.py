import asyncio
import os
from datetime import datetime

from FreakyUserbot import ALIVE_NAME, CMD_HELP
from FreakyUserbot.utils import Freaky_on_cmd

freakythumb = "./resources/FreakyUserbot.jpg"
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "Freaky"


@Freaky.on(Freaky_on_cmd(pattern="send ?(.*)"))
async def send(event):
    if event.fwd_from:
        return
    message_id = event.message.id
    input_str = event.pattern_match.group(1)
    start = datetime.now()
    if input_str.endswith(".py"):
        the_plugin_file = "./FreakyUserbot/modules/{}".format(input_str)
    else:
        the_plugin_file = "./FreakyUserbot/modules/{}.py".format(input_str)
    end = datetime.now()
    (end - start).seconds
    men = f"**► Plugin Name:** `{input_str}`\n**► Uploaded in {time_taken_in_ms} seconds.**\n**► Uploaded by:** [{DEFAULTUSER}](tg://user?id={hmm})\n\n© @FreakyUserbot"  # String From Telebot
    if not os.path.exists(the_plugin_file):
        await event.edit(f"Error 404: **{input_str}** Not Found")
        return
    await event.client.send_file(  # pylint:disable=E0602
        event.chat_id,
        the_plugin_file,
        thumb=freakythumb,
        caption=men,
        force_document=True,
        allow_cache=False,
        reply_to=message_id,
    )
    await asyncio.sleep(5)
    await event.delete()


CMD_HELP.update(
    {
        "send": "**Send**\
\n\n**Syntax : **`.send <plugin name>`\
\n**Usage :** sends the plugin."
    }
)
