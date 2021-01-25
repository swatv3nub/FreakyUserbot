import asyncio
import io
import os
import re

from telethon import Button, custom, events
from telethon.tl.functions.users import GetFullUserRequest

from HackfreaksUserbot import bot
from HackfreaksUserbot.Configs import Config
from HackfreaksUserbot.modules.sql_helper.blacklist_assistant import (
    add_nibba_in_db,
    is_he_added,
    removenibba,
)
from HackfreaksUserbot.modules.sql_helper.botusers_sql import add_me_in_db, his_userid
from HackfreaksUserbot.modules.sql_helper.idadder_sql import (
    add_usersid_in_db,
    already_added,
    get_all_users,
)


@assistant_cmd("start", is_args=False)
async def start(event):
    dayambot = await hackfreaksbot.get_me()
    bot_id = dayambot.first_name
    bot_username = dayambot.username
    replied_user = await event.client(GetFullUserRequest(event.sender_id))
    firstname = replied_user.user.first_name
    devlop = await bot.get_me()
    hmmwow = devlop.first_name
    vent = event.chat_id
    mypic = Config.ASSISTANT_START_PIC
    starttext = f"Hello, {firstname} ! Nice To Meet You, Well I Am {bot_id}, An Powerfull Assistant Bot. \n\nMy Master [{hmmwow}](tg://user?id={bot.uid}) \nYou Can Talk/Contact My Master Using This Bot. \n\nIf You Want Your Own Assistant You Can Deploy From Button Below. \n\nPowered By [Hackfreaks Userbot](t.me/HackfreaksUserbot)"
    if event.sender_id == bot.uid:
        await hackfreaksbot.send_message(
            vent,
            message=f"Hi Master, It's Me {bot_id}, Your Assistant ! \nWhat You Wanna Do today ?",
            buttons=[
                [custom.Button.inline("Show Users 🔥", data="users")],
                [custom.Button.inline("Commands For Assistant", data="gibcmd")],
                [
                    Button.url(
                        "Add Me to Group 👥", f"t.me/{bot_username}?startgroup=true"
                    )
                ],
            ],
        )
    else:
        if already_added(event.sender_id):
            pass
        elif not already_added(event.sender_id):
            add_usersid_in_db(event.sender_id)
        await hackfreaksbot.send_file(
            event.chat_id,
            file=mypic,
            caption=starttext,
            link_preview=False,
            buttons=[
                [custom.Button.inline("Deploy your Hackfreaks 🇮🇳", data="deploy")],
                [Button.url("Help Me ❓", "t.me/HackfreaksUserbot")],
            ],
        )
        if os.path.exists(mypic):
            os.remove(mypic)


# Data's


@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"deploy")))
async def help(event):
    await event.delete()
    if event.query.user_id is not bot.uid:
        await hackfreaksbot.send_message(
            event.chat_id,
            message="You Can Deploy Hackfreaks In Heroku By Following Steps Bellow, You Can See Some Quick Guides On Support Channel Or On Your Own Assistant Bot. \nThank You For Contacting Me.",
            buttons=[
                [Button.url("Deploy Tutorial 📺", "t.me/HackfreaksUserbot")],
                [Button.url("Need Help ❓", "t.me/HackfreaksSupport")],
            ],
        )


@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"users")))
async def users(event):
    if event.query.user_id == bot.uid:
        await event.delete()
        total_users = get_all_users()
        users_list = "List Of Total Users In Bot. \n\n"
        for freaked in total_users:
            users_list += ("==> {} \n").format(int(freaked.chat_id))
        with io.BytesIO(str.encode(users_list)) as tedt_file:
            tedt_file.name = "userlist.txt"
            await hackfreaksbot.send_file(
                event.chat_id,
                tedt_file,
                force_document=True,
                caption="Total Users In Your Bot.",
                allow_cache=False,
            )
    else:
        pass


@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"gibcmd")))
async def users(event):
    await event.delete()
    grabon = "Hello Here Are Some Commands \n➤ /start - Check if I am Alive \n➤ /ping - Pong! \n➤ /tr <lang-code> \n➤ /broadcast - Sends Message To all Users In Bot \n➤ /id - Shows ID of User And Media. \n➤ /addnote - Add Note \n➤ /notes - Shows Notes \n➤ /rmnote - Remove Note \n➤ /alive - Am I Alive? \n➤ /bun - Works In Group , Bans A User. \n➤ /unbun - Unbans A User in Group \n➤ /prumote - Promotes A User \n➤ /demute - Demotes A User \n➤ /pin - Pins A Message \n➤ /stats - Shows Total Users In Bot"
    await hackfreaksbot.send_message(event.chat_id, grabon)


# Bot Permit.
@tgbot.on(events.NewMessage(func=lambda e: e.is_private))
async def all_messages_catcher(event):
    if is_he_added(event.sender_id):
        return
    if event.raw_text.startswith("/"):
        pass
    elif event.sender_id == bot.uid:
        return
    else:
        await event.get_sender()
        event.chat_id
        sed = await event.forward_to(bot.uid)
        # Add User To Database ,Later For Broadcast Purpose
        # (C) @SpecHide
        add_me_in_db(sed.id, event.sender_id, event.id)


@tgbot.on(events.NewMessage(func=lambda e: e.is_private))
async def sed(event):
    msg = await event.get_reply_message()
    if msg is None:
        return
    msg.id
    msg_s = event.raw_text
    user_id, reply_message_id = his_userid(msg.id)
    if event.sender_id == Config.OWNER_ID:
        if event.raw_text.startswith("/"):
            return
        if event.text is not None and event.media:
            bot_api_file_id = pack_bot_file_id(event.media)
            await hackfreaksbot.send_file(
                user_id,
                file=bot_api_file_id,
                caption=event.text,
                reply_to=reply_message_id,
            )
        else:
            msg_s = event.raw_text
            await hackfreaksbot.send_message(
                user_id,
                msg_s,
                reply_to=reply_message_id,
            )


@assistant_cmd("broadcast", is_args=True)
@god_only
async def sedlyfsir(event):
    msgtobroadcast = event.pattern_match.group(1)
    userstobc = get_all_users()
    error_count = 0
    sent_count = 0
    hmmok = ""
    if msgtobroadcast == None:
        await event.reply("`Wait. What? Broadcast None?`")
        return
    elif msgtobroadcast == " ":
        await event.reply("`Wait. What? Broadcast None?`")
        return
    for freakcast in userstobc:
        try:
            sent_count += 1
            await hackfreaksbot.send_message(
                int(freakcast.chat_id),
                "**Hey, You Have Received A New Broadcast Message**",
            )
            await hackfreaksbot.send_message(int(freakcast.chat_id), msgtobroadcast)
            await asyncio.sleep(0.2)
        except Exception as e:
            hmmok += f"Errors : {e} \n"
            error_count += 1
    await hackfreaksbot.send_message(
        event.chat_id,
        f"Broadcast Done in {sent_count} Group/Users and I got {error_count} Error and Total Number Was {len(userstobc)}",
    )


@assistant_cmd("stats", is_args=False)
@peru_only
async def freakispro(event):
    dayamispro = get_all_users()
    await event.reply(
        f"**Stats Of Your Bot** \nTotal Users In Bot => {len(dayamispro)}"
    )


@assistant_cmd("help", is_args=False)
@peru_only
async def dayamislub(event):
    grabonx = "Hello Here Are Some Commands \n➤ /start - Check if I am Alive \n➤ /ping - Pong! \n➤ /tr <lang-code> \n➤ /broadcast - Sends Message To all Users In Bot \n➤ /id - Shows ID of User And Media. \n➤ /addnote - Add Note \n➤ /notes - Shows Notes \n➤ /rmnote - Remove Note \n➤ /alive - Am I Alive? \n➤ /bun - Works In Group , Bans A User. \n➤ /unbun - Unbans A User in Group \n➤ /prumote - Promotes A User \n➤ /demute - Demotes A User \n➤ /pin - Pins A Message \n➤ /stats - Shows Total Users In Bot"
    await event.reply(grabonx)


@assistant_cmd("block", is_args=False)
@god_only
async def dayamisnoob(event):
    if event.sender_id == bot.uid:
        msg = await event.get_reply_message()
        msg.id
        event.raw_text
        user_id, reply_message_id = his_userid(msg.id)
    if is_he_added(user_id):
        await event.reply("Already Blacklisted")
    elif not is_he_added(user_id):
        add_nibba_in_db(user_id)
        await event.reply("Blacklisted This Dumb Person")
        await hackfreaksbot.send_message(
            user_id, "You Have Been Blacklisted And You Can't Message My Master Now."
        )


@assistant_cmd("unblock", is_args=False)
@god_only
async def dayamisnoob(event):
    if event.sender_id == bot.uid:
        msg = await event.get_reply_message()
        msg.id
        event.raw_text
        user_id, reply_message_id = his_userid(msg.id)
    if not is_he_added(user_id):
        await event.reply("Not Even. Blacklisted 🤦🚶")
    elif is_he_added(user_id):
        removenibba(user_id)
        await event.reply("DisBlacklisted This Dumb Person")
        await hackfreaksbot.send_message(
            user_id, "Congo! You Have Been Unblacklisted By My Master."
        )
