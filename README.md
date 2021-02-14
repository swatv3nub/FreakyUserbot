<p align="center"><a href="https://t.me/ProjectHackfreaks"><img src="https://telegra.ph/file/ab9f85afcdc4ec394f8f6.jpg" width="5000"></a></p> 
<h1 align="center"><b>FreakyUserbot </b></h1>
<h4 align="center">A Powerful, Smart And Simple Userbot In Telethon.</h4>



<img src="https://github-readme-stats.vercel.app/api/pin?username=swatv3nub&show_icons=true&theme=dracula&hide_border=true&repo=FreakyUserbot">

# SUPPORT

<a href="https://t.me/HackfreaksUpdates"><img src="https://img.shields.io/badge/Join-Updates%20Channel-green.svg?logo=Telegram"></a>

<a href="https://t.me/HackfreaksSupport"><img src="https://img.shields.io/badge/Join-Support%20Group-blue.svg?logo=telegram"></a>








# GET APP_ID AND API_HASH

Get API_ID and API_HASH from [@HackfreaksScrapperRobot](https://telegram.dog/HackfreaksScrapperRobot)


# STRING_SESSION

Get STRING_SESSION from [@SessionStringBot](https://t.me/SessionStringBot) From [@TelebotHelp](https://t.me/Telebothelp)

OR

[![Run on Repl.it](https://telegra.ph/file/1b2ca5fd16997b21b4b41.jpg)](https://repl.it/@swatv3nub/UserbotSessionGenerator#main.py)


# DEPLOY

[<img src="https://www.herokucdn.com/deploy/button.svg" alt="Deploy to Heroku" height="40"/>](https://heroku.com/deploy?template=https://github.com/swatv3nub/FreakyUserbot/ "Heroku")


# HARD WAY (For Devs)

Simply clone the repository and run the main file:
```sh
# Install Git First.
git clone https://github.com/swatv3nub/FreakyUserbot
# Open Git Cloned File
cd FreakyUserbot
# Config Virtual Env
virtualenv -p /usr/bin/python3 venv
. ./venv/bin/activate
# Install All Requirements 
pip install -r requirements.txt
# Create local_config.py with variables as given below
# Start Bot 
python3 -m FreakyUserbot
```








# MANDATORY VARS
```
[+] Only three of the environment variables are mandatory.

[+] This is because of telethon.errors.rpc_error_list.ApiIdPublishedFloodError

    [-] APP_ID:   You can get this value from https://my.telegram.org
    [-] API_HASH :   You can get this value from https://my.telegram.org
    [-] STRING_SESSION :   You can get this value from https://repl.it/@swatv3nub/UserbotSessionGenerator#main.py or by running string_gen.py in your device
    
[+] The FreakyUserbot will not work without setting the mandatory vars.
```


# CREDIT'S

FRIDAY - :kissing_heart:

TELEBOT

CATUSERBOT

DARKCOBRA USERBOT

PAPERPLANE REMIX USERBOT



# Simple Plugin Example

```python3
from FreakyUserbot.utils import Freaky_on_cmd, sudo_cmd, edit_or_reply
from FreakyUserbot.Configs import Config
@Freaky.on(Freaky_on_cmd(pattern="devs"))
@Freaky.on(sudo_cmd(pattern="devs", allow_sudo=True))
async def devs(event):
    if event.fwd_from:
        return
    freaky = await edit_or_reply(event, "Listing My Devs....")
    await freaky.edit("**MY DEVS**\n\n1. @Swonit\n2. @jayantkageri\n\nA Part of @PythonDevs")
```



# Licence
[![GNU GPLv3 Image](https://www.gnu.org/graphics/gplv3-127x51.png)](http://www.gnu.org/licenses/gpl-3.0.en.html)  

FreakyUserbot is Free Software: You can use, study share and improve it at your
will. Specifically you can redistribute and/or modify it under the terms of the
[GNU General Public License](https://www.gnu.org/licenses/gpl.html) as
published by the Free Software Foundation, either version 3 of the License, or
(at your option) any later version. 

# IMPORTANT

I am Not Responsible for Anything Happened to your Acc Using this Userbot
