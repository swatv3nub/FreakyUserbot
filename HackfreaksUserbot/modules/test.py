from FreakyUserbot import CMD_HELP
from FreakyUserbot.utils import Freaky_on_cmd


@Freaky.on(Freaky_on_cmd(pattern=r"test"))
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
