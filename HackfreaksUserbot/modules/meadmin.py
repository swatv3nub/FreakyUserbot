# PLUGIN BY @JAYANTKAGERI
# LEECH WITH CREDITS
# © JAYANT KAGERI, ALL RIGHTS RESERVED


from HackfreaksUserbot.utils import Hackfreaks_on_cmd


@Hackfreaks.on(Hackfreaks_on_cmd(pattern="meadmin", outgoing=True))
async def _1(event):
    addall = [
        d.entity
        for d in await event.client.get_dialogs()
        if (d.is_group or d.is_channel)
    ]
    for i in addall:
        try:
            if i.creator or i.admin_rights:
                await bot.send_message(event.chat_id, i.title)
        except BaseException:
            pass
