# For @UniBorg
# courtesy Yasir siddiqui
"""Self Destruct Plugin
.sd <time in seconds> <text>
"""


import time

from FreakyUserbot import CMD_HELP
from FreakyUserbot.utils import Freaky_on_cmd


@Freaky.on(Freaky_on_cmd("sd", outgoing=True))
async def selfdestruct(destroy):
    """ For .sd command, make seflf-destructable messages. """
    if not destroy.text[0].isalpha() and destroy.text[0] not in ("/", "#", "@", "!"):
        message = destroy.text
        counter = int(message[4:6])
        text = str(destroy.text[6:])
        text = (
            text
            + "\n\n`This message shall be self-destructed in "
            + str(counter)
            + " seconds`"
        )
        await destroy.delete()
        smsg = await destroy.client.send_message(destroy.chat_id, text)
        time.sleep(counter)
        await smsg.delete()


CMD_HELP.update(
    {
        "selfdestruct": "SelfDestruct\
\n\nSyntax : .sd <time in seconds><text>\
\nUsage : Destructs Your Massage in Given Time"
    }
)
