"""
Syntax : .gps <location name>
credits :@mrconfused
"""

# help from @sunda005 and @SpEcHIDe
# don't edit credits

from geopy.geocoders import Nominatim
from telethon.tl import types

from FreakyUserbot import CMD_HELP
from FreakyUserbot.utils import Freaky_on_cmd, edit_or_reply, sudo_cmd


@Freaky.on(Freaky_on_cmd(pattern="gps ?(.*)"))
@Freaky.on(sudo_cmd(pattern="gps ?(.*)", allow_sudo=True))
async def gps(event):
    freakybot = await edit_or_reply(event, "Processing")
    if event.fwd_from:
        return
    reply_to_id = event.message
    if event.reply_to_msg_id:
        reply_to_id = await event.get_reply_message()
    input_str = event.pattern_match.group(1)

    if not input_str:
        return await freakybot.edit("what should i find give me location.")

    await freakybot.edit("finding")

    geolocator = Nominatim(user_agent="FreakyUserbot")
    geoloc = geolocator.geocode(input_str)

    if geoloc:
        lon = geoloc.longitude
        lat = geoloc.latitude
        await reply_to_id.reply(
            input_str, file=types.InputMediaGeoPoint(types.InputGeoPoint(lat, lon))
        )
        await event.delete()
    else:
        await freakybot.edit("i coudn't find it")


CMD_HELP.update(
    {
        "gps": "**Gps**\
\n\n**Syntax : **`.gps <location>`\
\n**Usage :** this plugin gives gps to the location."
    }
)
