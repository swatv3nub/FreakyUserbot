"""Syntax: .meaning <word>"""

from PyDictionary import PyDictionary

from HackfreaksUserbot import CMD_HELP
from HackfreaksUserbot.utils import Hackfreaks_on_cmd, edit_or_reply, sudo_cmd


@Hackfreaks.on(Hackfreaks_on_cmd("meaning (.*)"))
@Hackfreaks.on(sudo_cmd("meaning (.*)", allow_sudo=True))
async def _(event):
    dayam = await edit_or_reply(event, "Finding Meaning.....")
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    dictionary = PyDictionary()
    a = dictionary.meaning(input_str)
    b = a.get("Noun")
    kaif = ""
    for x in b:
        kaif += x + "\n"
    await dayam.edit(
        f"<b> meaning of {input_str} is:-</b>\n {kaif}",
        parse_mode="HTML",
    )


CMD_HELP.update(
    {
        "dictionary": "**Dictionary**\
\n\n**Syntax : **`.meaning <word>`\
\n**Usage :** Get meaning and pronunciation of a word."
    }
)
