"""Check if HackfreaksUserbot alive. If you change these, you become the gayest gay such that even the gay world will disown you."""
# CREDITS: @WhySooSerious, @Sur_vivor
import time

from HackfreaksUserbot import ALIVE_NAME, CMD_HELP, Lastupdate
from HackfreaksUserbot.Configs import Config, Var
from HackfreaksUserbot.modules import currentversion
from HackfreaksUserbot.utils import Hackfreaks_on_cmd, sudo_cmd


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

PM_IMG = Var.ALIVE_IMAGE if Var.ALIVE_IMAGE else None

pm_caption = "**✗ Hackfreaks Userbot is Alive ✗**\n\n"
pm_caption += f"**✗ Owner **: {DEFAULTUSER}\n\n"
pm_caption += "**✗ Telethon Version:** `Latest` \n"
pm_caption += f"**✗ Hackfreaks Version**: `{currentversion} Alpha`\n"
pm_caption += "**✗ Python:** `3.8.5` \n"
pm_caption += f"**✗ Uptime** : `{uptime}` \n\n"
pm_caption += "**✗ Copyright** : [Hackfreaks](https://t.me/HackfreaksUserbot)\n\n"
pm_caption += "**✗ License** : [GNU General Public License v3.0](https://github.com/swatv3nub/HackfreaksTelethonUserbot/blob/main/LICENSE)\n\n"
pm_caption += "**[✗ Updates](https://t.me/HackfreaksUserbot)**\n"
pm_caption += "**[✗ Support](https://t.meHackfreaksSupport)**\n\n"
pm_caption += "**[✗ GitHub Respiratory ✗](https://github.com/swatv3nub/HackfreaksTelethonUserbot/)**\n"
pm_caption += "**[✗ Deploy Hackfreaks ✗](https://heroku.com/deploy?template=https://github.com/swatv3nub/HackfreaksTelethonUserbot)**"



@Hackfreaks.on(Hackfreaks_on_cmd(pattern=r"alive"))
@Hackfreaks.on(sudo_cmd(pattern=r"alive", allow_sudo=True))
async def Hackfreaks(alive):
    await alive.get_chat()
    """ For .alive command, check if the bot is running.  """
    if PM_IMG == None
        await borg.send_message(alive.chat_id, pm_caption)
        await alive.delete()
        await alive.delete()
    else:
        await both.send_file(alive.chat_id, PM_IMG, caption=pm_caption)
        await alive.delete()
        await alive.delete()


CMD_HELP.update(
    {
        "alive": "**Alive**\
\n\n**Syntax : **`.alive`\
\n**Usage :** Check if UserBot is Alive"
    }
)
