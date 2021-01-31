"""DA.GD helpers in @UniBorg
Available Commands:
.isup URL
.dns google.com
.url <long url>
.unshort <short url>"""
import requests

from FreakyUserbot import CMD_HELP
from FreakyUserbot.utils import Freaky_on_cmd, edit_or_reply, sudo_cmd


@Freaky.on(Freaky_on_cmd("dns (.*)"))
@Freaky.on(sudo_cmd("dns (.*)", allow_sudo=True))
async def _(event):
    freaky = await edit_or_reply(event, "Processing.....")
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    sample_url = "https://da.gd/dns/{}".format(input_str)
    response_api = requests.get(sample_url).text
    if response_api:
        await freaky.edit("DNS records of {} are \n{}".format(input_str, response_api))
    else:
        await freaky.edit("i can't seem to find {} on the internet".format(input_str))


@Freaky.on(Freaky_on_cmd("url (.*)"))
@Freaky.on(sudo_cmd("dns (.*)", allow_sudo=True))
async def _(event):
    sofreaky = await edit_or_reply(event, "Processing....")
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    sample_url = "https://da.gd/s?url={}".format(input_str)
    response_api = requests.get(sample_url).text
    if response_api:
        await sofreaky.edit("Generated {} for {}.".format(response_api, input_str))
    else:
        await sofreaky.edit("something is wrong. please try again later.")


@Freaky.on(Freaky_on_cmd("unshort (.*)"))
async def _(event):
    sadness = await edit_or_reply(event, "Processing...")
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    if not input_str.startswith("http"):
        input_str = "http://" + input_str
    r = requests.get(input_str, allow_redirects=False)
    if str(r.status_code).startswith("3"):
        await sadness.edit(
            "Input URL: {}\nReDirected URL: {}".format(input_str, r.headers["Location"])
        )
    else:
        await sadness.edit(
            "Input URL {} returned status_code {}".format(input_str, r.status_code)
        )


CMD_HELP.update(
    {
        "dns": "**Dns**\
\n\n**Syntax : **`.dns <site link>`\
\n**Usage :** it provides DNS records of given site.\
\n\n**Syntax : **`.url <site link>`\
\n**Usage :** it shortens given URL.\
\n\n**Syntax : **`.unshort <shorten link>`\
\n**Usage :** it unshortens the given short link."
    }
)
