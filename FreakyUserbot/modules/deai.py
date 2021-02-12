# Under Development 
# By Swonit for @FreakyUserbot 
# 
#
# import html
# import asyncio
# 
# from telethon.errors.rpcerrorlist import YouBlockedUserError
# 
# from FreakyUserbot.utils import Freaky_on_cmd
# from FreakyUserbot import CMD_HELP
# from FreakyUserbot.Configs import Config
# 
# bot = "@rSophieBot"
# 
# DEAI_BAN_CODES = {
#     "00": "Gban",
#     "01": "Joinspam",
#     "02": "Spambot",
#     "03": "Generic spam",
#     "04": "Scam",
#     "05": "Illegal",
#     "06": "Pornography",
#     "07": "Nonsense",
#     "08": "Chain bans",
#     "09": "Special",
#     "10": "Preemptive",
#     "11": "Copyright",
#     "12": "Admin rights abuse",
#     "13": "Toxicity",
#     "14": "Flood",
#     "15": "Detected but not classified",
#     "16": "Advanced detection",
#     "17": "Reported",
#     "18": "AI association",
#     "19": "Impersonation",
#     "20": "Malware",
#     "21": "Ban evasion",
#     "22": "PM spam",
#     "23": "Spam adding members",
#     "24": "RESERVED",
#     "25": "RESERVED",
#     "26": "Raid initiation",
#     "27": "Raid participation"
# }
# DEAI_MODULE_CODES = {
#     "0": "Gban",
#     "1": "Database parser",
#     "2": "Realtime",
#     "3": "Profiler",
#     "4": "Scraper",
#     "5": "Association analytics",
#     "6": "Codename Autobahn",
#     "7": "Codename Polizei",
#     "8": "Codename Gestapo"
# }
# 
# 
# @Freaky.on(Freaky_on_cmd(pattern="deai ?(.*)"))
# async def _(event):
#     if event.fwd_from:
#         return
#     ok = await event.edit("`Checking for DEAI Bans...`")
#     if event.reply_to_msg_id:
#         previous_message = await event.get_reply_message()
#         sysarg = str(previous_message.sender_id)
#         user = f"[user](tg://user?id={sysarg})"
#     else:
#         sysarg = event.pattern_match.group(1)
#         user = sysarg
#     if sysarg == "":
#         await ok.edit(
#             "`Give me someones id, or reply to somones message to check his/her deai stats.`"
#         )
#         return
#     else:
#         async with borg.conversation(bot) as conv:
#             try:
#                 await conv.send_message("/start")
#                 await conv.get_response()
#                 await conv.send_message("/fcheck" + {sysarg} + "845d33d3-0961-4e44-b4b5-4c57775fbdac")
#                 
# Space For Rest Codes
#             
#             except YouBlockedUserError:
#                 await ok.edit("**Error**\n `Unblock` @rSophieBot `and try again!")
#
#
# CMD_HELP.update(
#   {
#       "DEAI stats": ".deai <username/userid/reply to user>\nUse - To check the persons DEAI status in @rSophieBot.\"
#   }
#)