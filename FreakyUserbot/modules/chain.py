# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from telethon.tl.functions.messages import SaveDraftRequest

from FreakyUserbot import CMD_HELP
from FreakyUserbot.utils import Freaky_on_cmd, edit_or_reply, sudo_cmd


@Freaky.on(Freaky_on_cmd(pattern="chain"))
@Freaky.on(sudo_cmd(pattern="chain", allow_sudo=True))
async def _(event):
    pokemonlub = await edit_or_reply(event, "Counting...")
    count = -1
    message = event.message
    while message:
        reply = await message.get_reply_message()
        if reply is None:
            await borg(
                SaveDraftRequest(
                    await event.get_input_chat(), "", reply_to_msg_id=message.id
                )
            )
        message = reply
        count += 1
    await pokemonlub.edit(f"Chain length: {count}")


CMD_HELP.update(
    {
        "chain": ".chain\nUse- Find the total number of replies to a message and it's origin."
    }
)
