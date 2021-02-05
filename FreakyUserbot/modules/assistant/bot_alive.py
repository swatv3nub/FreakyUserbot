from FreakyUserbot import ALIVE_NAME

DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "FreakyUserbot Admeme"
PM_IMG = "https://telegra.ph/file/ab9f85afcdc4ec394f8f6.jpg"
pm_caption = "👑 Freaky's Assistant IS: WORKING 👑\n\n"
pm_caption += "✗ **Freaky Stats**\n"
pm_caption += "✗ **Telethon Version:** `Latest` \n"
pm_caption += "✗ **Python:** `3.8.6` \n"
pm_caption += "✗ **Current Branch** : `Alpha`\n"
pm_caption += f"✗ **Owner** : {DEFAULTUSER} \n"
pm_caption += "✗ **Database** : `Working Properly`\n\n"
pm_caption += "✗**[Join Our Channel]**(https://t.me/FreakyUserbot)\n"
pm_caption += "✗ **License** : [GNU General Public License v3.0](https://github.com/swatv3nub/FreakyUserbot/blob/main/LICENSE)\n"
pm_caption += "✗ **Copyright** : By [Freaky](https://t.me/FreakyUserbot)\n"
pm_caption += "[Userbot By Freaks 🇮🇳]"

# only Owner Can Use it
@assistant_cmd("alive", is_args=False)
@freaks_only
async def FreakyUserbot(event):
    await freakybot.send_file(event.chat_id, PM_IMG, caption=pm_caption)
