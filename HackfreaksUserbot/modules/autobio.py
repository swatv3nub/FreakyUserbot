# AutoBio plugin for Freaky
# Using this might lead to ban of your account, use at your own risk.
# Re-Written by @swatv3nub

import asyncio
import time

from telethon.errors import FloodWaitError
from telethon.tl import functions

from FreakyUserbot import CMD_HELP
from FreakyUserbot.utils import Freaky_on_cmd

DEL_TIME_OUT = 60


@Freaky.on(Freaky_on_cmd(pattern="autobio"))  # pylint:disable=E0602
async def _(event):
    if event.fwd_from:
        return
    while True:
        DMY = time.strftime("%d.%m.%Y")
        HM = time.strftime("%H:%M:%S")
        bio = f"📅 {DMY} | This is my bio, I guess.. 😁 | ⌚️ {HM}"
        logger.info(bio)
        try:
            await borg(
                functions.account.UpdateProfileRequest(  # pylint:disable=E0602
                    about=bio
                )
            )
        except FloodWaitError as ex:
            logger.warning(str(e))
            await asyncio.sleep(ex.seconds)
        # else:
        # logger.info(r.stringify())
        await borg.send_message(
            Var.PRIVATE_GROUP_ID, "#Auto_Bio\nSuccessfully enabled auto-bio."
        )
        await asyncio.sleep(DEL_TIME_OUT)


CMD_HELP.update({"autobio": ".autobio\nUse - Auto-changing profile bio, with time"})
