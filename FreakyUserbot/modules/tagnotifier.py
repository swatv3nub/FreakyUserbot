# (c) Shrimadhav U K
#
# This file is part of @UniBorg
#
# from telethon import custom, events
# from telethon.tl.types import Chat
# from telethon.utils import get_display_name
#
# from FreakyUserbot.Configs import Config
#
#
# @Freaky.on(
#     events.NewMessage(
#         incoming=True,
#         blacklist_chats=Config.UB_BLACK_LIST_CHAT,
#         func=lambda e: (e.mentioned),
#     )
# )
# async def all_messages_catcher(event):
#     if Config.NEEDTOLOG == "DISABLE":
#         return
#     # the bot might not have the required access_hash to mention the appropriate PM
#     lol_spechide = await tgbot.get_me()
#     sedbruh = lol_spechide.username
#     await event.forward_to(sedbruh)
#     # construct message
#     # the message format is stolen from @MasterTagAlertBot
#     ammoca_message = ""
#
#     who_ = await event.client.get_entity(event.sender_id)
#     if who_.bot or who_.verified or who_.support:
#         return
#
#     who_m = f"[{get_display_name(who_)}](tg://user?id={who_.id})"
#
#     where_ = await event.client.get_entity(event.chat_id)
#
#     where_m = get_display_name(where_)
#     button_text = "✗ Go to Message ✗"
#
#     if isinstance(where_, Chat):
#         message_link = f"https://t.me/c/{where_.id}/{event.id}"
#     else:
#
#     ammoca_message += f"User {who_m} Have Tagged You Here -> [{where_m}]({message_link}) \nCheck Message 👇 "
#     log_chat = Config.TAG_LOG
#     await tgbot.send_message(
#         log_chat,
#         message=ammoca_message,
#         link_preview=False,
#         buttons=[[custom.Button.url(button_text, message_link)]],
#     )
