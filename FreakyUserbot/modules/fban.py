#    Base : Midhun KM [From Friday]

#    Re-Edited by Swonit for FreakyUserbot whitelisting my IDs // Don't Know It will Work or Not BTW.LUL

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

"""Commands Available
.fadd <fedid> = Add Fed in DB
.fadd all = Add All feds in DB
.frm <fedid> = Remove fed from DB
.frm all = Remove All Feds from DB
.fban <id/username> <reason> = Fed Ban the Targetted User in the Feds in DB
.unfban <id/username> = UnFedBan the Targetted user in the Feds in DB
"""

import asyncio

from FreakyUserbot.functions import fetch_feds
from FreakyUserbot.modules.sql_helper.feds_sql import (
    add_fed,
    get_all_feds,
    is_fed_indb,
    rmfed,
)
from FreakyUserbot.utils import Freaky_on_cmd

chnnl_grp = Config.FBAN_GROUP


@Freaky.on(Freaky_on_cmd(pattern="fadd ?(.*)"))
async def _(event):
    nolol = 0
    yeslol = 0
    await event.edit("`Processing..`")
    freakz = event.pattern_match.group(1)
    if freakz == None:
        await event.edit("`Give FeD ID`")
        return
    elif freakz == " ":
        await event.edit("`Give FeD ID`")
        return
    elif freakz == "all":
        hmm = await fetch_feds(event, borg)
        for i in hmm:
            if is_fed_indb(i):
                nolol += 1
            elif not is_fed_indb(i):
                add_fed(i)
                yeslol += 1
        await event.edit(f"`Added {yeslol} Feds To DB, Failed To Add {nolol} Feds.`")
    elif is_fed_indb(freakz):
        await event.edit("`Fed Already Found On DataBase.`")
        return
    elif not is_fed_indb(freakz):
        add_fed(freakz)
        await event.edit("`Done ! Added This Fed To DataBase`")


@Freaky.on(Freaky_on_cmd(pattern="frm ?(.*)"))
async def _(event):
    freakz = event.pattern_match.group(1)
    await event.edit("`Processing..`")
    lol = get_all_feds()
    if freakz == None:
        await event.edit("`Give FeD ID`")
        return
    elif freakz == " ":
        await event.edit("`Give FeD ID`")
        return
    elif freakz == "all":
        for sedm in lol:
            rmfed(sedm.feds)
        await event.edit("`Done, Cleared. All Fed Database.`")
    elif is_fed_indb(freakz):
        rmfed(freakz)
        await event.edit("`Done, Removed This FeD From DB`")
    elif not is_fed_indb(freakz):
        await event.edit("`This Fed Not Found On Db.`")


@Freaky.on(Freaky_on_cmd(pattern="fban ?(.*)"))
async def _(event):
    await event.edit("Starting Fed Bans...")
    arg = event.text.split(" ", maxsplit=2)
    if len(arg) > 2:
        FBAN = arg[1]
        REASON = arg[2]
    else:
        FBAN = arg[1]
        REASON = " MassBanned Kela #FreakyOP."

    try:
        int(FBAN)
        if int(FBAN) == "1228116248" or int(FBAN) == "1167145475":
            await event.edit("Error, Can't Fban Dev.")
            return
    except BaseException:
        if FBAN == "@TheFuckErGuy" or FBAN == "@Swonit":
            await event.edit("Error, can't Fban Dev.")
            return
    else:
        await event.edit("`Something Went Wrong.`")
        return
    all_fed = get_all_feds()
    errors = 0
    len_feds = len(all_fed)
    if len_feds == 0:
        await event.edit(
            "`No Fed IN DB, Add One To Do So. Please Do .fadd all by Tagging your FedAdmin File to Add All Feds IN Database`"
        )
        return
    await event.edit(f"`FBanning in {len_feds} Feds.`")

    try:
        await borg.send_message(chnnl_grp, "/start")
    except Exception as e:
        await event.edit("**Errors** : " + str(e))
        return
    for kela in all_fed:
        try:
            await borg.send_message(chnnl_grp, "/joinfed " + kela.feds)
            await asyncio.sleep(2)
            await borg.send_message(chnnl_grp, "/fban " + {FBAN} + {REASON})
            await asyncio.sleep(5)
        except:
            errors += 1
    await event.edit(
        f"**Fban Completed** \nTotal Sucess : `{len_feds - errors}` \nTotal Errors : `{errors}` \nTotal Fed Len : `{len_feds}`"
    )


@Freaky.on(Freaky_on_cmd(pattern="unfban ?(.*)"))
async def _(event):
    freakz = event.pattern_match.group(1)
    if freakz == None:
        await event.edit("`No User Found To Fban.`")
        return
    all_fed = get_all_feds()
    errors = 0
    len_feds = len(all_fed)
    await event.edit(f"`UnFBanning in {len_feds} Feds.`")
    try:
        await borg.send_message(chnnl_grp, "/start")
    except Exception as e:
        await event.edit("**Errors** : " + str(e))
        return
    for kela in all_fed:
        try:
            await borg.send_message(chnnl_grp, "/joinfed " + kela.feds)
            await asyncio.sleep(2)
            await borg.send_message(chnnl_grp, "/unfban " + freakz)
            await asyncio.sleep(5)
        except:
            errors += 1
    await event.edit(
        f"**Un-Fban Completed** \nTotal Sucess : `{len_feds - errors}` \nTotal Errors : `{errors}` \nTotal Fed Len : `{len_feds}`"
    )
