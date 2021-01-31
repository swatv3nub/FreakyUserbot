# For @UniBorg
# (c) Shrimadhav U K

from telethon.tl.functions.channels import GetAdminedPublicChannelsRequest
from uniborg.util import Freaky_on_cmd

from FreakyUserbot import CMD_HELP


@Freaky.on(Freaky_on_cmd("reserved"))
async def mine(event):
    """ For .reserved command, get a list of your reserved usernames. """
    result = await bot(GetAdminedPublicChannelsRequest())
    output_str = ""
    for channel_obj in result.chats:
        output_str += f"{channel_obj.title}\n@{channel_obj.username}\n\n"
    await event.edit(output_str)


CMD_HELP.update(
    {
        "Reserved Usernames": "**List my reserved usernames**\
\n\n**Syntax : **`.reserved`\
\n**Usage :** it lists all your usernames you are holding"
    }
)
