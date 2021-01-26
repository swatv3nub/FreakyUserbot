# Hackfreaks - Userbot

# Written by @HeisenbergTheDanger, @xditya for Telebot ->> @TelebotSupport
# Ported to HackfreaksUserbot by @swatv3nub ->> @ProjectHackfreaks

# import asyncio
#
# from HackfreaksUserbot import CMD_HELP
# from HackfreaksUserbot.utils import Hackfreaks_on_cmd
#
#
# @Hackfreaks.on(Hackfreaks_on_cmd("superfban ?(.*)"))
# async def _(event):
#     if event.fwd_from:
#         return
#     await event.edit("Starting a Mass-FedBan...")
#     fedList = []
#     if event.reply_to_msg_id:
#         previous_message = await event.get_reply_message()
#         if previous_message.media:
#             downloaded_file_name = await hackfreaksuserbot.download_media(
#                 previous_message, "fedlist"
#             )
#             await asyncio.sleep(6)
<<<<<<< HEAD
#            file = open(downloaded_file_name, "r")
#            lines = file.readlines()
#            for line in lines:
#                try:
#                    fedList.append(line[:36])
#                except BaseException:
#                    pass
#            arg = event.text.split(" ", maxsplit=2)
#            if len(arg) > 2:
#                FBAN = arg[1]
#                REASON = arg[2]
#            else:
#                FBAN = arg[1]
#                REASON = " MassBanned #HackfreaksUserbot "
#        else:
#            FBAN = previous_message.sender_id
#            REASON = event.text.split(" ", maxsplit=1)[1]
#            if REASON.strip() == "":
#                REASON = " MassBanned #HackfreaksUserbot "
#    else:
#        arg = event.text.split(" ", maxsplit=2)
#        if len(arg) > 2:
#            FBAN = arg[1]
#            REASON = arg[2]
#        else:
#            FBAN = arg[1]
#            REASON = " MassBanned #HackfreaksUserbot "
#    try:
#        int(FBAN)
#        if int(FBAN) == 1228116248 or int(FBAN) == 719195224 or int(FBAN) == 1167145475:
#            await event.edit("Error, Can't Fban Dev.")
#            return
#    except BaseException:
#        if FBAN == "@TheFuckErGuy" or FBAN == "@xditya" or FBAN == "@TheFSociety2_0":
#            await event.edit("Error, can't Fban Dev.")
#            return
#    if Config.FBAN_GROUP_ID:
#        chat = Config.FBAN_GROUP_ID
#    else:
#        chat = await event.get_chat()
#    if not len(fedList):
#        for a in range(3):
#            async with hackfreaksuserbot.conversation("@MissRose_bot") as bot_conv:
#                await bot_conv.send_message("/start")
#                await bot_conv.send_message("/myfeds")
#                await asyncio.sleep(3)
#                response = await bot_conv.get_response()
#                await asyncio.sleep(3)
#                if "make a file" in response.text:
#                    await asyncio.sleep(6)
#                    await response.click(0)
#                    await asyncio.sleep(6)
#                    fedfile = await bot_conv.get_response()
#                    await asyncio.sleep(3)
#                    if fedfile.media:
#                        downloaded_file_name = await hackfreaksuserbot.download_media(
#                            fedfile, "fedlist"
#                        )
#                        await asyncio.sleep(6)
#                        file = open(downloaded_file_name, "r")
#                        lines = file.readlines()
#                        for line in lines:
#                            try:
#                                fedList.append(line[:36])
#                            except BaseException:
#                                pass
#                    else:
#                        return
#                if len(fedList) == 0:
#                    await event.edit(f"Something went wrong. Retrying ({a+1}/3)...")
#                else:
#                    break
#        else:
#            await event.edit(f"Error")
#        if "You can only use fed commands once every 5 minutes" in response.text:
#            await event.edit("Try again after 5 mins.")
#            return
#        In = False
#        tempFedId = ""
#        for x in response.text:
#            if x == "`":
#                if In:
#                    In = False
#                    fedList.append(tempFedId)
#                    tempFedId = ""
#                else:
#                    In = True
#
#            elif In:
#                tempFedId += x
#        if len(fedList) == 0:
#            await event.edit("Something went wrong.")
#            return
#    await event.edit(f"Fbaning in {len(fedList)} feds.")
#    try:
#        await hackfreaksuserbot.send_message(chat, f"/start")
#    except BaseException:
#        await event.edit("FBAN_GROUP_ID is incorrect.")
#        return
#    await asyncio.sleep(3)
#    if Config.EXCLUDE_FED:
#        excludeFed = Config.EXCLUDE_FED.split("|")
#        for n in range(len(excludeFed)):
#            excludeFed[n] = excludeFed[n].strip()
#    exCount = 0
#    for fed in fedList:
#        if Config.EXCLUDE_FED and fed in excludeFed:
#            await hackfreaksuserbot.send_message(chat, f"{fed} Excluded.")
#            exCount += 1
#            continue
#        await hackfreaksuserbot.send_message(chat, f"/joinfed {fed}")
#        await asyncio.sleep(3)
#        await hackfreaksuserbot.send_message(chat, f"/fban {FBAN} {REASON}")
#        await asyncio.sleep(3)
#    await event.edit(
#        f"MassFedBan Completed. Affected {len(fedList) - exCount} feds.\n#HackfreaksUserbot"
#    )
=======
#             file = open(downloaded_file_name, "r")
#             lines = file.readlines()
#             for line in lines:
#                 try:
#                     fedList.append(line[:36])
#                 except BaseException:
#                     pass
#             arg = event.text.split(" ", maxsplit=2)
#             if len(arg) > 2:
#                 FBAN = arg[1]
#                 REASON = arg[2]
#             else:
#                 FBAN = arg[1]
#                 REASON = " MassBanned #HackfreaksUserbot "
#         else:
#             FBAN = previous_message.sender_id
#             REASON = event.text.split(" ", maxsplit=1)[1]
#             if REASON.strip() == "":
#                 REASON = " MassBanned #HackfreaksUserbot "
#     else:
#         arg = event.text.split(" ", maxsplit=2)
#         if len(arg) > 2:
#             FBAN = arg[1]
#             REASON = arg[2]
#         else:
#             FBAN = arg[1]
#             REASON = " MassBanned #HackfreaksUserbot "
#     try:
#         int(FBAN)
#         if int(FBAN) == 1228116248 or int(FBAN) == 719195224 or int(FBAN) == 1167145475:
#             await event.edit("Error, Can't Fban Dev.")
#             return
#     except BaseException:
#         if FBAN == "@TheFuckErGuy" or FBAN == "@xditya" or FBAN == "@TheFSociety2_0":
#             await event.edit("Error, can't Fban Dev.")
#             return
#     if Config.FBAN_GROUP_ID:
#         chat = Config.FBAN_GROUP_ID
#     else:
#         chat = await event.get_chat()
#     if not len(fedList):
#         for a in range(3):
#             async with hackfreaksuserbot.conversation("@MissRose_bot") as bot_conv:
#                 await bot_conv.send_message("/start")
#                 await bot_conv.send_message("/myfeds")
#                 await asyncio.sleep(3)
#                 response = await bot_conv.get_response()
#                 await asyncio.sleep(3)
#                 if "make a file" in response.text:
#                     await asyncio.sleep(6)
#                     await response.click(0)
#                     await asyncio.sleep(6)
#                     fedfile = await bot_conv.get_response()
#                     await asyncio.sleep(3)
#                     if fedfile.media:
#                         downloaded_file_name = await hackfreaksuserbot.download_media(
#                             fedfile, "fedlist"
#                         )
#                         await asyncio.sleep(6)
#                         file = open(downloaded_file_name, "r")
#                         lines = file.readlines()
#                         for line in lines:
#                             try:
#                                 fedList.append(line[:36])
#                             except BaseException:
#                                 pass
#                     else:
#                         return
#                 if len(fedList) == 0:
#                     await event.edit(f"Something went wrong. Retrying ({a+1}/3)...")
#                 else:
#                     break
#         else:
#             await event.edit(f"Error")
#         if "You can only use fed commands once every 5 minutes" in response.text:
#             await event.edit("Try again after 5 mins.")
#             return
#         In = False
#         tempFedId = ""
#         for x in response.text:
#             if x == "`":
#                 if In:
#                     In = False
#                     fedList.append(tempFedId)
#                     tempFedId = ""
#                 else:
#                     In = True
#
#             elif In:
#                 tempFedId += x
#         if len(fedList) == 0:
#             await event.edit("Something went wrong.")
#             return
#     await event.edit(f"Fbaning in {len(fedList)} feds.")
#     try:
#         await hackfreaksuserbot.send_message(chat, f"/start")
#     except BaseException:
#         await event.edit("FBAN_GROUP_ID is incorrect.")
#         return
#     await asyncio.sleep(3)
#     if Config.EXCLUDE_FED:
#         excludeFed = Config.EXCLUDE_FED.split("|")
#         for n in range(len(excludeFed)):
#             excludeFed[n] = excludeFed[n].strip()
#     exCount = 0
#     for fed in fedList:
#         if Config.EXCLUDE_FED and fed in excludeFed:
#             await hackfreaksuserbot.send_message(chat, f"{fed} Excluded.")
#             exCount += 1
#             continue
#         await hackfreaksuserbot.send_message(chat, f"/joinfed {fed}")
#         await asyncio.sleep(3)
#         await hackfreaksuserbot.send_message(chat, f"/fban {FBAN} {REASON}")
#         await asyncio.sleep(3)
#     await event.edit(
#         f"MassFedBan Completed. Affected {len(fedList) - exCount} feds.\n#HackfreaksUserbot"
#     )
>>>>>>> 738420e4abbe1c18b11c533089d73f0c00737e76
#
#
# @Hackfreaks.on(Hackfreaks_on_cmd("superunfban ?(.*)"))
# async def _(event):
<<<<<<< HEAD
#    if event.fwd_from:
#        return
#    await event.edit("Starting a Mass-UnFedBan...")
#    if event.reply_to_msg_id:
#        previous_message = await event.get_reply_message()
#        FBAN = previous_message.sender_id
#    else:
#        FBAN = event.pattern_match.group(1)
#
#    if Config.FBAN_GROUP_ID:
#        chat = Config.FBAN_GROUP_ID
#    else:
#        chat = await event.get_chat()
#    fedList = []
#    for a in range(3):
#        async with hackfreaksuserbot.conversation("@MissRose_bot") as bot_conv:
#            await bot_conv.send_message("/start")
#            await bot_conv.send_message("/myfeds")
#            response = await bot_conv.get_response()
#            if "make a file" in response.text:
#                await asyncio.sleep(3)
##                await response.click(0)
##                fedfile = await bot_conv.get_response()
##                if fedfile.media:
##                    downloaded_file_name = await hackfreaksuserbot.download_media(
##                        fedfile, "fedlist"
##                   )
##                   file = open(downloaded_file_name, "r")
##                   lines = file.readlines()
##                   for line in lines:
##                       fedList.append(line[: line.index(":")])
##               else:
##                   return
##               if len(fedList) == 0:
##                   await event.edit(f"Something went wrong. Retrying ({a+1}/3)...")
##               else:
##                   break
##   else:
##       await event.edit(f"Error")
##   if "You can only use fed commands once every 5 minutes" in response.text:
##       await event.edit("Try again after 5 mins.")
##       return
##   In = False
##   tempFedId = ""
##   for x in response.text:
##       if x == "`":
##           if In:
##               In = False
#                fedList.append(tempFedId)
#                tempFedId = ""
#            else:
#                In = True
#
#        elif In:
#            tempFedId += x
#
#    await event.edit(f"UnFbaning in {len(fedList)} feds.")
#    try:
#        await hackfreaksuserbot.send_message(chat, f"/start")
#    except BaseException:
#        await event.edit("FBAN_GROUP_ID is incorrect.")
#        return
#    await asyncio.sleep(5)
#    for fed in fedList:
#        await hackfreaksuserbot.send_message(chat, f"/joinfed {fed}")
#        await asyncio.sleep(5)
#        await hackfreaksuserbot.send_message(chat, f"/unfban {FBAN}")
#        await asyncio.sleep(5)
#    await event.edit(
#        f"SuperUnFBan Completed. Affected {len(fedList)} feds.\n#HackfreaksUserbot"
#    )
#
#
# CMD_HELP.update(
#    {
#        "superban": ".superfban <username/userid> <reason>\
#        \n**Usage**: Mass-Ban in all feds you are admin in.\
#        \nSet `EXCLUDE_FED fedid1|fedid2` in heroku vars to exclude those feds.\
#        \nSet var `FBAN_GROUP_ID` to the group with rose, where you want FBan to take place.\
#        \n\nGet help - @HackfreaksUserbot."
#    }
# )
#
=======
#     if event.fwd_from:
#         return
#     await event.edit("Starting a Mass-UnFedBan...")
#     if event.reply_to_msg_id:
#         previous_message = await event.get_reply_message()
#         FBAN = previous_message.sender_id
#     else:
#         FBAN = event.pattern_match.group(1)
#
#     if Config.FBAN_GROUP_ID:
#         chat = Config.FBAN_GROUP_ID
#     else:
#         chat = await event.get_chat()
#     fedList = []
#     for a in range(3):
#         async with hackfreaksuserbot.conversation("@MissRose_bot") as bot_conv:
#             await bot_conv.send_message("/start")
#             await bot_conv.send_message("/myfeds")
#             response = await bot_conv.get_response()
#             if "make a file" in response.text:
#                 await asyncio.sleep(3)
#                 await response.click(0)
#                 fedfile = await bot_conv.get_response()
#                 if fedfile.media:
#                     downloaded_file_name = await hackfreaksuserbot.download_media(
#                         fedfile, "fedlist"
#                     )
#                     file = open(downloaded_file_name, "r")
#                     lines = file.readlines()
#                     for line in lines:
#                         fedList.append(line[: line.index(":")])
#                 else:
#                     return
#                 if len(fedList) == 0:
#                     await event.edit(f"Something went wrong. Retrying ({a+1}/3)...")
#                 else:
#                     break
#     else:
#         await event.edit(f"Error")
#     if "You can only use fed commands once every 5 minutes" in response.text:
#         await event.edit("Try again after 5 mins.")
#         return
#     In = False
#     tempFedId = ""
#     for x in response.text:
#         if x == "`":
#             if In:
#                 In = False
#                 fedList.append(tempFedId)
#                 tempFedId = ""
#             else:
#                 In = True
#
#         elif In:
#             tempFedId += x
#
#     await event.edit(f"UnFbaning in {len(fedList)} feds.")
#     try:
#         await hackfreaksuserbot.send_message(chat, f"/start")
#     except BaseException:
#         await event.edit("FBAN_GROUP_ID is incorrect.")
#         return
#     await asyncio.sleep(5)
#     for fed in fedList:
#         await hackfreaksuserbot.send_message(chat, f"/joinfed {fed}")
#         await asyncio.sleep(5)
#         await hackfreaksuserbot.send_message(chat, f"/unfban {FBAN}")
#         await asyncio.sleep(5)
#     await event.edit(
#         f"SuperUnFBan Completed. Affected {len(fedList)} feds.\n#HackfreaksUserbot"
#     )
#
#
# CMD_HELP.update(
#     {
#         "superban": ".superfban <username/userid> <reason>\
#         \n**Usage**: Mass-Ban in all feds you are admin in.\
#         \nSet `EXCLUDE_FED fedid1|fedid2` in heroku vars to exclude those feds.\
#         \nSet var `FBAN_GROUP_ID` to the group with rose, where you want FBan to take place.\
#         \n\nGet help - @HackfreaksUserbot."
#     }
# )
#
>>>>>>> 738420e4abbe1c18b11c533089d73f0c00737e76
