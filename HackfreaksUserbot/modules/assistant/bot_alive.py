from HackfreaksUserbot import ALIVE_NAME

DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "HackfreaksUserbot Admeme"
PM_IMG = "https://telegra.ph/file/bb3741b7596bf90f47568.png"
pm_caption = "👑 Hackfreaks's Assistant IS: WORKING 👑\n\n"
pm_caption += "✯ **Hackfreaks Stats**\n"
pm_caption += "✯ **Telethon Version:** `Latest` \n"
pm_caption += "✯ **Python:** `3.8.5` \n"
pm_caption += "✯ **Database Status:**  `Functional`\n"
pm_caption += "✯ **Current Branch** : `Alpha`\n"
pm_caption += f"✯ **My Boss** : {DEFAULTUSER} \n"
pm_caption += "✯ **Database** : `AWS - Working Properly`\n\n"
pm_caption += "✯**[Join Our Channel]**(https://t.me/HackfreaksUserbot)\n"
pm_caption += "✯ **License** : [GNU General Public License v3.0](https://github.com/swatv3nub/HackfreaksTelethonUserbot/blob/main/LICENSE)\n"
pm_caption += "✯ **Copyright** : By [Hackfreaks](https://t.me/HackfreaksUserbot)\n"
pm_caption += "[Userbot By Hackfreaks 🇮🇳]"

# only Owner Can Use it
@assistant_cmd("alive", is_args=False)
@peru_only
async def hackfreaksuserbot(event):
    await hackfreaksbot.send_file(event.chat_id, PM_IMG, caption=pm_caption)
