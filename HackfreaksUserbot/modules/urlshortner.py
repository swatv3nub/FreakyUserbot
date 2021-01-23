import pyshorteners

from HackfreaksUserbot import CMD_HELP
from HackfreaksUserbot.utils import Hackfreaks_on_cmd, sudo_cmd


@Hackfreaks.on(Hackfreaks_on_cmd(pattern="urlshort (.*)"))
@Hackfreaks.on(sudo_cmd(pattern="urlshort (.*)", allow_sudo=True))
async def vom(event):
    try:
        link = event.pattern_match.group(1)
        sed = pyshorteners.Shortener()
        kek = sed.tinyurl.short(link)
        bestisbest = (
            f"<b>Url Shortened</b> \n<b><u>Given Link</u></b> ➠ <code>{link}</code> \n"
            f"<b><u>Shortened Link</u></b> ➠ <code>{kek}</code>"
        )
        await event.edit(bestisbest, parse_mode="HTML")
    except Exception as e:
        await event.edit("SomeThing Went Wrong. \nError : " + e)


CMD_HELP.update(
    {
        "urlshortner": "UrlShortner\
\n\nSyntax : .urlshort <link>\
\nUsage : Shortens Your Url"
    }
)
