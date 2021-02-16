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


import os

from telethon.errors.rpcerrorlist import YouBlockedUserError

from FreakyUserbot import CMD_HELP
from FreakyUserbot.utils import Freaky_on_cmd

mytoken = os.environ.get("NOSPAMPLUS_TOKEN")


@Freaky.on(Freaky_on_cmd(pattern="deai ?(.*)"))
async def _(event):
    if event.fwd_from:
        return
    ok = await event.edit("`Checking for @DahuaEngine [DEAI] Bans...`")
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
        async with borg.conversation("@rSophieBot") as conv:  # DEAI
            try:
                await conv.send_message("/start")
                await conv.get_response()
                await conv.send_message(
                    f"/fcheck {sysarg} 845d33d3-0961-4e44-b4b5-4c57775fbdac"
                )
                audio = await conv.get_response()
                await ok.edit(
                    audio.text
                    + "\n\nDEAI bancodes explaination [here](https://t.me/DahuaEngine/11)"
                )
            # Direct bancodes explaination later
            except YouBlockedUserError:
                await ok.edit("**Error**\n `Unblock` @rSophieBot `and try again!")


@Freaky.on(Freaky_on_cmd(pattern="anon ?(.*)"))
async def _(event):
    if event.fwd_from:
        return
    ok = await event.edit("`Checking for @TheAnonymousArmy Bans...`")
    if event.reply_to_msg_id:
        previous_message = await event.get_reply_message()
        sysarg = str(previous_message.sender_id)
        user = f"[user](tg://user?id={sysarg})"
    else:
        sysarg = event.pattern_match.group(1)
    if sysarg == "":
        await ok.edit(
            "`Give me someones id, or reply to somones message to check his/her stats.`"
        )
        return
    else:
        async with borg.conversation("@MissRose_Bot") as conv:  # AnonymousArmy
            try:
                await conv.send_message("/start")
                await conv.get_response()
                await conv.send_message(
                    f"/fbanstat {sysarg} 21029270-28da-425c-9a4a-8f0514624ef0"
                )
                msg = await conv.get_response()
                await ok.edit(
                    msg.text
                    + "\n\nAnonymousArmy bancodes explaination [Here](https://t.me/TheAnonymousArmy/24)"
                )
            # Direct bancodes explaination later
            except YouBlockedUserError:
                await ok.edit("**Error**\n `Unblock` @MissRose_Bot `and try again!")


@Freaky.on(Freaky_on_cmd(pattern="ppas ?(.*)"))
async def _(event):
    if event.fwd_from:
        return
    ok = await event.edit("`Checking for @PaperPlaneAntiSpam Bans...`")
    if event.reply_to_msg_id:
        previous_message = await event.get_reply_message()
        sysarg = str(previous_message.sender_id)
        user = f"[user](tg://user?id={sysarg})"
    else:
        sysarg = event.pattern_match.group(1)
    if sysarg == "":
        await ok.edit(
            "`Give me someones id, or reply to somones message to check his/her stats.`"
        )
        return
    else:
        async with borg.conversation("@MissRose_Bot") as conv:  # PaperPlane AntiSpam
            try:
                await conv.send_message("/start")
                await conv.get_response()
                await conv.send_message(
                    f"/fbanstat {sysarg} 967c79d3-5924-42f0-860b-5cdb037586b5"
                )
                msg = await conv.get_response()
                await ok.edit(msg.text)
            except YouBlockedUserError:
                await ok.edit("**Error**\n `Unblock` @MissRose_Bot `and try again!")


@Freaky.on(Freaky_on_cmd(pattern="sibyl ?(.*)"))
async def _(event):
    if event.fwd_from:
        return
    ok = await event.edit("`Checking for @SibylSystem GBans...`")
    if event.reply_to_msg_id:
        previous_message = await event.get_reply_message()
        sysarg = str(previous_message.sender_id)
        user = f"[user](tg://user?id={sysarg})"
    else:
        sysarg = event.pattern_match.group(1)
    if sysarg == "":
        await ok.edit(
            "`Give me someones id, or reply to somones message to check his/her stats.`"
        )
        return
    else:
        async with borg.conversation(
            "@MissRose_Bot"
        ) as conv:  # Sibyl System // Using their Fed
            try:
                await conv.send_message("/start")
                await conv.get_response()
                await conv.send_message(
                    f"/fbanstat {sysarg} 5dcc7db0-0fbc-46c9-bbe7-5700ef47a0d5"
                )
                msg = await conv.get_response()
                await ok.edit(msg.text)
            except YouBlockedUserError:
                await ok.edit("**Error**\n `Unblock` @MissRose_Bot `and try again!")


@Freaky.on(Freaky_on_cmd(pattern="rose ?(.*)"))
async def _(event):
    if event.fwd_from:
        return
    ok = await event.edit("`Checking for Rose Support Bans...`")
    if event.reply_to_msg_id:
        previous_message = await event.get_reply_message()
        sysarg = str(previous_message.sender_id)
        user = f"[user](tg://user?id={sysarg})"
    else:
        sysarg = event.pattern_match.group(1)
    if sysarg == "":
        await ok.edit(
            "`Give me someones id, or reply to somones message to check his/her stats.`"
        )
        return
    else:
        async with borg.conversation("@MissRose_Bot") as conv:  # Rose Official
            try:
                await conv.send_message("/start")
                await conv.get_response()
                await conv.send_message(
                    f"/fbanstat {sysarg} 86718661-6bfc-4bd0-9447-7c419eb08e69"
                )
                msg = await conv.get_response()
                await ok.edit(msg.text)
            except YouBlockedUserError:
                await ok.edit("**Error**\n `Unblock` @MissRose_Bot `and try again!")


# NoSpamPlus

# @Freaky.on(Freaky_on_cmd(pattern="nsp ?(.*)"))
# async def _(event):
#     if event.fwd_from:
#         return
#     ok = await event.edit("`Checking For NoSpamPlus Bans`")
#     if event.reply_to_msg_id:
#         previous_message = await event.get_reply_message()
#         sysarg = str(previous_message.sender_id)
#         user = f"[user](tg://user?id={sysarg})"
#     else:
#         sysarg = event.pattern_match.group(1)
#     if sysarg == "":
#         await ok.edit(
#             "`Give me someones id, or reply to somones message to check his/her stats.`"
#         )
#         return
#     else:
#         token_connect = Connect(mytoken)
#         user = token_connect.is_banned({sysarg})
#         msgx = user.ban_code
#         msgz = user.reason
#         ok.edit(f"**Banned with Ban Code**: {msgx} with reason: {msgz}")

# SpamProtection

# @Freaky.on(Freaky_on_cmd(pattern="spb ?(.*)"))
# async def _(event):
#    if event.fwd_from:
#        return
#    ok = await event.edit("`Checking For Blacklist in SpamProtection`")
#    if event.reply_to_msg_id:
#        previous_message = await event.get_reply_message()
#        sysarg = str(previous_message.sender_id)
#        user = f"[user](tg://user?id={sysarg})"
#    else:
#        sysarg = event.pattern_match.group(1)
#        user = sysarg
#    if sysarg == "":
#        await ok.edit(
#            "`Give me someones id, or reply to somones message to check his/her stats.`"
#        )
#        return
#    else:
#        spurl = f"https://api.intellivoid.net/spamprotection/v1/lookup?query={sysarg}" #SpamProtection Blacklist
#        r = requests.get(spurl)
#        jsonn = r.json()
#        if jsonn["success"]:
#            text = ""
#            if jsonn["results"]["attributes"]["is_potential_spammer"]:
#
#               text += "\n- <b>Potential Spammer:</b> Yes\n"
#
#            if jsonn["results"]["private_telegram_id"]:
#                sed = jsonn['results']['private_telegram_id']
#                text += f"\n- <b>PTID:</b>  {sed}"
#
#            if json["results"]["language_prediction"]["language"]:
#                text += f'\n- <b>Language Prediction:</b> {json["results"]["language_prediction"]["language"]}   - <b>Language Prediction Probability:</b> {jsonn["results"]["language_prediction"]["probability"]}'
#            if json["results"]["attributes"]["is_blacklisted"]:
#                text += f'\n- <b>Blacklist Flag:</b> {json["results"]["attributes"]["blacklist_flag"]}- <b>Blacklist Reason:</b> {jsonn["results"]["attributes"]["blacklist_reason"]}'
#            if json["results"]["attributes"]["original_private_id"]:
#                text += f'\n- <b>Original Private ID:</b> {json["results"]["attributes"]["original_private_id"]}'
#            if json["results"]["spam_prediction"]["spam_prediction"]:
#                   text += f'\n- Spam Prediction:</br> {json["results"]["spam_prediction"]["spam_prediction"]}'
#
#            spamprotection = text
#        await ok.edit(spamprotection)


CMD_HELP.update(
    {
        "userbanstatus": "**UserBanStatus**\
\n\n**Syntax : **`.anon / .ppas / .deai / .sibyl / .rose / .spb[Fixing Soon] / .cas <reply to a user / mention their ID>`\
\n**Usage :** Checks his Status in Indivisual Systems."
    }
)

# (C) Swonit
