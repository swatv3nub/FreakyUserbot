"""Check if FreakyUserbot alive."""
# CREDITS: @WhySooSerious, @Sur_vivor
import time

from FreakyUserbot import ALIVE_NAME, CMD_HELP, Lastupdate
from FreakyUserbot.Configs import Config
from FreakyUserbot.modules import currentversion
from FreakyUserbot.utils import Freaky_on_cmd, sudo_cmd


# Functions
def get_readable_time(seconds: int) -> str:
    count = 0
    ping_time = ""
    time_list = []
    time_suffix_list = ["s", "m", "h", "days"]

    while count < 4:
        count += 1
        if count < 3:
            remainder, result = divmod(seconds, 60)
        else:
            remainder, result = divmod(seconds, 24)
        if seconds == 0 and remainder == 0:
            break
        time_list.append(int(result))
        seconds = int(remainder)

    for x in range(len(time_list)):
        time_list[x] = str(time_list[x]) + time_suffix_list[x]
    if len(time_list) == 4:
        ping_time += time_list.pop() + ", "

    time_list.reverse()
    ping_time += ":".join(time_list)

    return ping_time


uptime = get_readable_time((time.time() - Lastupdate))
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "Unknown"

PM_IMG = Config.ALIVE_IMAGE

pm_caption = "**✗ Freaky Userbot is Alive ✗**\n\n"
pm_caption += f"**✗ Owner **: {DEFAULTUSER}\n\n"
pm_caption += "**✗ Telethon Version:** `Latest` \n"
pm_caption += f"**✗ Freaky Version**: `{currentversion} Alpha`\n"
pm_caption += "**✗ Python:** `3.8.6` \n"
pm_caption += f"**✗ Uptime** : `{uptime}` \n\n"
pm_caption += (
    "**✗ Copyright** : [ProjectHackfreaks](https://t.me/ProjectHackfreaks)\n\n"
)
pm_caption += "**✗ License** : [GNU General Public License v3.0](https://github.com/swatv3nub/FreakyUserbot/blob/main/LICENSE)\n\n"
pm_caption += "**[✗ Updates](https://t.me/FreakyUserbot)**\n"
pm_caption += "**[✗ Support](https://t.me/HackfreaksSupport)**\n\n"
pm_caption += (
    "**[✗ GitHub Repository ✗](https://github.com/swatv3nub/FreakyUserbot/)**\n"
)
pm_caption += "**[✗ Deploy Freaky ✗](https://heroku.com/deploy?template=https://github.com/swatv3nub/FreakyUserbot)**\n\n"
pm_caption += "**A Part of @ScannerOverPowered // @PythonDevs**"


@Freaky.on(Freaky_on_cmd(pattern=r"alive"))
@Freaky.on(sudo_cmd(pattern=r"alive", allow_sudo=True))
async def Freaky(alive):
    await alive.get_chat()
    """ For .alive command, check if the bot is running.  """
    await borg.send_file(alive.chat_id, PM_IMG, caption=pm_caption)
    await alive.delete()
    await alive.delete()


CMD_HELP.update(
    {
        "alive": "**Alive**\
\n\n**Syntax : **`.alive`\
\n**Usage :** Check if UserBot is Alive"
    }
)
