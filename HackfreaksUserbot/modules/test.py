from HackfreaksUserbot import CMD_HELP
from HackfreaksUserbot.utils import Hackfreaks_on_cmd


@Hackfreaks.on(Hackfreaks_on_cmd(pattern=r"test"))
async def test(event):
    if event.fwd_from:
        return
    await event.edit("Test Successfull. Boss !")


CMD_HELP.update(
    {
        "test": "Test\
\n\nSyntax : .test\
\nUsage : Another Fun Plugin"
    }
)
