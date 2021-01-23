#    Copyright (C) Dayam Zaidi 2020
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <https://www.gnu.org/licenses/>.


from HackfreaksUserbot import ALIVE_NAME

DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "Unknown"
PM_IMG = "https://telegra.ph/file/63d2f8bcdae4da2ec5e7e.jpg"
pm_caption = "👑 Hackfreaks's Assistant IS: WORKING 👑\n\n"
pm_caption += "✯ **Hackfreaks Stats**\n"
pm_caption += "✯ **Telethon Version:** `1.15.0` \n"
pm_caption += "✯ **Python:** `3.7.4` \n"
pm_caption += "✯ **Database Status:**  `Functional`\n"
pm_caption += "✯ **Current Branch** : `master`\n"
pm_caption += f"✯ **My Boss** : {DEFAULTUSER} \n"
pm_caption += "✯ **Heroku Database** : `AWS - Working Properly`\n\n"
pm_caption += "✯**[Join Our Channel]**(https://t.me/HackfreaksOT)\n"
pm_caption += "✯ **License** : [GNU General Public License v3.0](https://github.com/swatv3nub/HackfreaksTelethonUserbot/blob/main/LICENSE)\n"
pm_caption += "✯ **Copyright** : By [Hackfreaks](https://t.me/HackfreaksUserbot)\n"
pm_caption += "[Assistant By Hackfreaks 🇮🇳]"

# only Owner Can Use it
@assistant_cmd("alive", is_args=False)
@peru_only
async def friday(event):
    await tgbot.send_file(event.chat_id, PM_IMG, caption=pm_caption)
