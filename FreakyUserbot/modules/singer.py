"""
command: .singer singer name - song name 
by @quiec
"""
from PyLyrics import *

from FreakyUserbot import CMD_HELP
from FreakyUserbot.utils import Freaky_on_cmd


@Freaky.on(Freaky_on_cmd(pattern="singer (.*)"))
async def _(event):
    if event.fwd_from:
        return

    input_str = event.pattern_match.group(1)

    try:
        song = input_str.split("-")
        if len(song) == 1:
            await event.edit("Usage: .singer Duman - Haberin Yok Ölüyorum")
        else:
            await event.edit("🔍︎Searching lyrics By Freaky")
            lyrics = PyLyrics.getLyrics(song[0].strip(), song[1].strip()).split("\n")
            lyric_message = f"Singing {song[0].strip()} from {song[1].strip()} 🎙"
            lyric_message += "\n\n" + "\n".join(lyrics)
            try:
                await event.edit(lyric_message)
            except:
                # TODO: send as file
                logger.info(lyric_message)
    except ValueError:
        await event.edit("Song not found")


CMD_HELP.update(
    {
        "singer": "Singer\
\n\nSyntax : .singer <Artist>-<Song>\
\nUsage : First Letter Should Be Capital"
    }
)
