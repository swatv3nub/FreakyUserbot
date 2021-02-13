#    Copyright (C) 2021 Swonit
#
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

# import os
# 
# from FreakyUserbot import CMD_HELP
# from FreakyUserbot.utils import Freaky_on_cmd, sudo_cmd
# 
# 
# @Freaky.on(Freaky_on_cmd(pattern="ubs ?(.*)"))
# @Freaky.on(sudo_cmd(pattern="ubs ?(.*)"), allow_sudo=True)
# async def _(event):
#     if event.fwd_from:
#         return
#     ok = await event.edit("`Checking for User's Ban Status...`")
#     if event.reply_to_msg_id:
#         previous_message = await event.get_reply_message()
#         sysarg = str(previous_message.sender_id)
#         user = f"[user](tg://user?id={sysarg})"
#     else:
#         sysarg = event.pattern_match.group(1)
#     if sysarg == "":
#         await ok.edit("`Give me an UserID / Username or Atleast Tag him Noob Nibba`")
#         return
#     else:
#         async with borg.conversation("@rSophieBot") as conv:  # DEAI
#             await conv.send_message("/start")
#             await conv.get_response()
#             await conv.send_message(
#                 f"/fcheck {sysarg} 845d33d3-0961-4e44-b4b5-4c57775fbdac"
#             )
#             msg = await conv.get_response()
#             deai = await ok.edit(
#                 msg.text
#                 + "\n\nDEAI bancodes explaination [Here](https://t.me/DahuaEngine/11)"
#             )
#         # Space For Rest Codes for direct bancode explaination
# 
#         async with borg.conversation("@MissRose_Bot") as conv:  # AnonymousArmy
#             await conv.send_message("/start")
#             await conv.get_response()
#             await conv.send_message(
#                 f"/fbanstat {sysarg} 21029270-28da-425c-9a4a-8f0514624ef0"
#             )
#             msg = await conv.get_response()
#             anon = await ok.edit(
#                 msg.text
#                 + "\n\nAnonymousArmy bancodes explaination [Here](https://t.me/TheAnonymousArmy/24)"
#             )
#             # Space For Rest Codes for direct bancode explaination
# 
#         async with borg.conversation("@MissRose_Bot") as conv:  # PaperPlaneAntiSpam
#             await conv.send_message("/start")
#             await conv.get_response()
#             await conv.send_message(
#                 f"/fbanstat {sysarg} 967c79d3-5924-42f0-860b-5cdb037586b5"
#             )
#             msg = await conv.get_response()
#             await msg.text
# 
#         async with borg.conversation("@MissRose_Bot") as conv:  # Rose Official
#             await conv.send_message("/start")
#             await conv.get_response()
#             await conv.send_message(
#                 f"/fbanstat {sysarg} 86718661-6bfc-4bd0-9447-7c419eb08e69"
#             )
#             msg = await conv.get_response()
#             await msg.text
# 
#         async with borg.conversation("@MissRose_Bot") as conv:  # SibylSystemGbans
#             await conv.send_message("/start")
#             await conv.get_response()
#             await conv.send_message(
#                 f"/fbanstat {sysarg} 5dcc7db0-0fbc-46c9-bbe7-5700ef47a0d5"
#             )
#             msg = await conv.get_response()
#             await msg.text
# 
#     # SpamWatch
# 
#     import spamwatch
# 
#     SPAMWATCH_API = os.environ.get("SPAMWATCH_API")
#     client = spamwatch.Client(SPAMWATCH_API)
#     client.get_ban(sysarg)
# 
# 
#         # SpamProtection [Might Not Work]
# 
#    spurl = f"https://api.intellivoid.net/spamprotection/v1/lookup?query={sysarg}"
#    r = requests.get(spurl)
#    jsonn = r.json()
#    if jsonn["success"]:
#         text = ""
#         if jsonn["results"]["attributes"]["is_potential_spammer"]:
# 
#            text += "\n- <b>Potential Spammer:</b> Yes\n"
# 
#         if jsonn["results"]["private_telegram_id"]:
#             sed = jsonn['results']['private_telegram_id']
#             text += f"\n- <b>PTID:</b>  {sed}"
# 
#         if json["results"]["language_prediction"]["language"]:
#             text += f'\n- <b>Language Prediction:</b> {jsonn["results"]["language_prediction"]["language"]}   - <b>Language Prediction Probability:</b> {jsonn["results"]["language_prediction"]["probability"]}'
#         if json["results"]["attributes"]["is_blacklisted"]:
#             text += f'\n- <b>Blacklist Flag:</b> {jsonn["results"]["attributes"]["blacklist_flag"]}- <b>Blacklist Reason:</b> {jsonn["results"]["attributes"]["blacklist_reason"]}'
#         if json["results"]["attributes"]["original_private_id"]:
#             text += f'\n- <b>Original Private ID:</b> {jsonn["results"]["attributes"]["original_private_id"]}'
#         if json["results"]["spam_prediction"]["spam_prediction"]:
#                text += f'\n- Spam Prediction:</br> {jsonn["results"]["spam_prediction"]["spam_prediction"]}'
#         spamprotection = text
# 
#         # End Of Checking
# 
# REPLY_MSG = f"""
# **✗Checked User✗** : {sysarg}
# 
# **✗ @TheAnonymousArmy ✗** : {anon}
# 
# **✗ Rose Support Official ✗** : {rose}
# 
# **✗ @SpamWatch ✗** : {swban}
# 
# **✗ @DahuaEngine [DEAI] ✗** : {deai}
# 
# **✗ Gbanned by @SibylSystem ✗** : {sibyl}
# 
# **✗ @PaperPlaneAntiSpam ✗** : {paperplane}
# 
# **✗ Spam Protection ✗** : {spamprotection}
# 
# """
# await ok.edit(REPLY_MSG)
# 
# 
# 
# 
# @Freaky.on(Freaky_on_cmd(pattern="anon (.*)"))
# @Freaky.on(sudo_cmd(pattern="anon (.*)", allow_sudo=True))
# async def _(event):
#     ok = await event.edit("Searching in @TheAnonymousArmy...")
#     await ok.edit(anon)
# 
# 
# @Freaky.on(Freaky_on_cmd(pattern="deai (.*)"))
# @Freaky.on(sudo_cmd(pattern="deai (.*)", allow_sudo=True))
# async def _(event):
#     ok = await event.edit("Searching in @DahuaEngine...")
#     await ok.edit(deai)
# 
# 
# @Freaky.on(Freaky_on_cmd(pattern="sw (.*)"))
# @Freaky.on(sudo_cmd(pattern="sw (.*)", allow_sudo=True))
# async def _(event):
#     ok = await event.edit("Searching in @SpamWatch...")
#     await ok.edit(swban)
# 
# 
# @Freaky.on(Freaky_on_cmd(pattern="ppln (.*)"))
# @Freaky.on(sudo_cmd(pattern="ppln (.*)", allow_sudo=True))
# async def _(event):
#     ok = await event.edit("Searching in @PaperPlaneAntiSpam...")
#     await ok.edit(paperplane)
# 
# 
# @Freaky.on(Freaky_on_cmd(pattern="sibyl (.*)"))
# @Freaky.on(sudo_cmd(pattern="sibyl (.*)", allow_sudo=True))
# async def _(event):
#     ok = await event.edit("Searching for Gbans in @SibylSystem...")
#     await ok.edit(sibyl)
# 
# 
# @Freaky.on(Freaky_on_cmd(pattern="rose (.*)"))
# @Freaky.on(sudo_cmd(pattern="rose (.*)", allow_sudo=True))
# async def _(event):
#     ok = await event.edit("Searching in Rose Support...")
#     await ok.edit(rose)
# 
# 
# @Freaky.on(Freaky_on_cmd(pattern="spb (.*)"))
# @Freaky.on(sudo_cmd(pattern="spb (.*)", allow_sudo=True))
# async def _(event):
#  ok = await event.edit("Searching in @SpamProtectionLogs...")
#  await ok.edit(spamprotection)
# 
# CMD_HELP.update(
#     {
#         "userbanstatus": "**UserBanStatus**\
# \n\n**Syntax : **`.ubs <reply to a user / mention their ID>`\
# \n**Usage :** Checks his status in some of the Anti-Spam Systems.\
# \n\n**Syntax : **`.sw / .ppln / .anon / .deai / .sibyl / .rose / .spb / .cas <reply to a user / mention their ID>`\
# \n**Usage :** Checks his Status in Indivisual Systems."
#     }
# )
# 
# (C) Swonit // Kang With Credits
