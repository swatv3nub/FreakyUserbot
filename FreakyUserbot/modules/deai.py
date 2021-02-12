# Under Development
# By Swonit for @FreakyUserbot


from telethon.errors.rpcerrorlist import YouBlockedUserError

from FreakyUserbot import CMD_HELP
from FreakyUserbot.utils import Freaky_on_cmd

bot = "@rSophieBot"

# DEAI_BAN_CODES = {
#     "0x00": "Gban",
#     "0x01": "Joinspam",
#     "0x02": "Spambot",
#     "0x03": "Generic spam",
#     "0x04": "Scam",
#     "0x05": "Illegal",
#     "0x06": "Pornography",
#     "0x07": "Nonsense",
#     "0x08": "Chain bans",
#     "0x09": "Special",
#     "0x10": "Preemptive",
#     "0x11": "Copyright",
#     "0x12": "Admin rights abuse",
#     "0x13": "Toxicity",
#     "0x14": "Flood",
#     "0x15": "Detected but not classified",
#     "0x16": "Advanced detection",
#     "0x17": "Reported",
#     "0x18": "AI association",
#     "0x19": "Impersonation",
#     "0x20": "Malware",
#     "0x21": "Ban evasion",
#     "0x22": "PM spam",
#     "0x23": "Spam adding members",
#     "0x24": "RESERVED",
#     "0x25": "RESERVED",
#     "0x26": "Raid initiation",
#     "0x27": "Raid participation"
# }
# DEAI_MODULE_CODES = {
#     "X0": "Gban",
#     "X1": "Database parser",
#     "X2": "Realtime",
#     "X3": "Profiler",
#     "X4": "Scraper",
#     "X5": "Association analytics",
#     "X6": "Codename Autobahn",
#     "X7": "Codename Polizei",
#     "X8": "Codename Gestapo"
# }


@Freaky.on(Freaky_on_cmd(pattern="deai ?(.*)"))
async def _(event):
    if event.fwd_from:
        return
    ok = await event.edit("`Checking for DEAI Bans...`")
    if event.reply_to_msg_id:
        previous_message = await event.get_reply_message()
        sysarg = str(previous_message.sender_id)
        user = f"[user](tg://user?id={sysarg})"
    else:
        sysarg = event.pattern_match.group(1)
    if sysarg == "":
        await ok.edit(
            "`Give me someones id, or reply to somones message to check his/her deai stats.`"
        )
        return
    else:
        async with borg.conversation(bot) as conv:
            try:
                await conv.send_message("/start")
                await conv.get_response()
                await conv.send_message(
                    f"/fcheck {sysarg} 845d33d3-0961-4e44-b4b5-4c57775fbdac"
                )
                audio = await conv.get_response()
                await ok.edit(
                    audio.text
                    + "\n\nDEAI Ban Info Extracted using FreakyUserbot [[bancodes explaination]](https://t.me/DahuaEngine/11)"
                )
            # Space For Rest Codes for direct bancode explaination
            except YouBlockedUserError:
                await ok.edit("**Error**\n `Unblock` @rSophieBot `and try again!")


CMD_HELP.update(
    {
        "DEAI stats": ".deai <username/userid/reply to user>\nUse - To check the persons DEAI status in @rSophieBot."
    }
)
