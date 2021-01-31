import requests
from telethon.tl.types import MessageMediaPhoto

from FreakyUserbot import CMD_HELP
from FreakyUserbot.utils import Freaky_on_cmd, sudo_cmd


@Freaky.on(Freaky_on_cmd(pattern=r"pcheck"))
@Freaky.on(sudo_cmd(pattern=r"pcheck", allow_sudo=True))
async def pcheck(event):
    url = "https://nsfw-categorize.it/api/upload"
    await event.edit("`Processing..`")
    replymsg = await event.get_reply_message()
    photo = None
    if replymsg and replymsg.media:
        if isinstance(replymsg.media, MessageMediaPhoto):
            photo = await borg.download_media(message=replymsg.photo)
        elif "image" in replymsg.media.document.mime_type.split("/"):
            photo = await borg.download_file(replymsg.media.document)
        else:
            await event.edit("`Reply To Image.`")
    if photo:
        files = {"image": (f"{photo}", open(f"{photo}", "rb"))}
        r = requests.post(url, files=files).json()
        if r["status"] == "OK":
            await event.edit(
                "This image is classified as " + str(r["data"]["classification"])
            )
        else:
            await event.edit("Response UnsucessFull. Try Again.")


CMD_HELP.update(
    {
        "pcheck": "PCheck**\
\n\n**Syntax : .pcheck <reply to image>\
\nUsage : Check If The Image Is Related To Porn"
    }
)
