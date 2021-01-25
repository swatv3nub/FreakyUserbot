#    Hackfreaks - UserBot
#    Copyright (C) 2020 Hackfreaks @ProjectHackfreaks



import logging
from pathlib import Path
from sys import argv

import telethon.utils
from telethon import TelegramClient

from HackfreaksUserbot import bot
from HackfreaksUserbot.Configs import Config
from HackfreaksUserbot.utils import load_module, start_assistant
from var import Var

sed = logging.getLogger("Hackfreaks")


async def add_bot(bot_token):
    await bot.start(bot_token)
    bot.me = await bot.get_me()
    bot.uid = telethon.utils.get_peer_id(bot.me)


if len(argv) not in (1, 3, 4):
    bot.disconnect()
else:
    bot.hackfreaksbot = None
    if Var.TG_BOT_USER_NAME_BF_HER is not None:
        bot.hackfreaksbot = TelegramClient(
            "TG_BOT_TOKEN", api_id=Var.APP_ID, api_hash=Var.API_HASH
        ).start(bot_token=Var.TG_BOT_TOKEN_BF_HER)
        bot.loop.run_until_complete(add_bot(Var.TG_BOT_USER_NAME_BF_HER))
    else:
        bot.start()


import glob

path = "HackfreaksUserbot/modules/*.py"
files = glob.glob(path)
for name in files:
    with open(name) as f:
        path1 = Path(f.name)
        shortname = path1.stem
        load_module(shortname.replace(".py", ""))

if Config.ENABLE_ASSISTANTBOT == "ENABLE":
    path = "HackfreaksUserbot/modules/assistant/*.py"
    files = glob.glob(path)
    for name in files:
        with open(name) as f:
            path1 = Path(f.name)
            shortname = path1.stem
            start_assistant(shortname.replace(".py", ""))
    sed.info("""\n @ProjectHackfreaks   """)
else:
    sed.info("Hackfreaks Has Been Installed Sucessfully !")
    sed.info("You Can Visit @HackfreaksUserbot For Any Support Or Doubts")

if len(argv) not in (1, 3, 4):
    bot.disconnect()
else:
    bot.run_until_disconnected()
