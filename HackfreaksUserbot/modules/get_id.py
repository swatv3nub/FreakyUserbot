"""Get ID of any Telegram media, or any user
Syntax: .get_id"""
from telethon.utils import pack_bot_file_id

from FreakyUserbot import CMD_HELP
from FreakyUserbot.utils import Freaky_on_cmd, edit_or_reply, sudo_cmd


@Freaky.on(Freaky_on_cmd("get_id"))
@Freaky.on(sudo_cmd("get_id", allow_sudo=True))
async def _(event):
    noobfreaksop = await edit_or_reply(event, "Processing")
    if event.fwd_from:
        return
    if event.reply_to_msg_id:
        await event.get_input_chat()
        r_msg = await event.get_reply_message()
        if r_msg.media:
            bot_api_file_id = pack_bot_file_id(r_msg.media)
            await noobfreaksop.edit(
                "Current Chat ID: `{}`\nFrom User ID: `{}`\nBot API File ID: `{}`".format(
                    str(event.chat_id), str(r_msg.from_id), bot_api_file_id
                )
            )
        else:
            await noobfreaksop.edit(
                "Current Chat ID: `{}`\nFrom User ID: `{}`".format(
                    str(event.chat_id), str(r_msg.from_id)
                )
            )
    else:
        await noobfreaksop.edit("Current Chat ID: `{}`".format(str(event.chat_id)))


CMD_HELP.update(
    {
        "get_id": "**Get_Id**\
\n\n**Syntax : **`.get_id`\
\n**Usage :** Tells You Abour Chat id, Group id."
    }
)
