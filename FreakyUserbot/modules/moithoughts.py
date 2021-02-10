# BY Swonit [@swatv3nub]
# Some Of Moi Englis, Hindi, INGLIS and Den-Shit Mode Thoughts
# command .mts

import asyncio
import random

from FreakyUserbot import CMD_HELP
from FreakyUserbot.utils import Freaky_on_cmd


@Freaky.on(Freaky_on_cmd(pattern="mts (.*)"))
async def _(event):

    if event.fwd_from:

        return

    await event.edit("Typing...")

    await asyncio.sleep(2)

    x = random.randrange(1, 34)

    if x == 1:

        await event.edit(
            '`"Don\'t underestimate the Kid Who is Time Rich and Money Poor!"`'
        )

    if x == 2:

        await event.edit('`"An Angry Guy is More Dangerous than the Devil himself!"`')

    if x == 3:

        await event.edit('`"Love, Ok. Love!"`')

    if x == 4:

        await event.edit(
            '`"What will you do first if you became invisible for 1 day?"`'
        )

    if x == 5:

        await event.edit('`"Learn First, then remove the L and Earn."`')

    if x == 6:

        await event.edit(
            '`"Once you’ve accepted your flaws, no one can use them against you."`'
        )

    if x == 7:

        await event.edit('`"Stay Quiet."`')

    if x == 8:

        await event.edit('`"Be Good, Stay Good."`')

    if x == 9:

        await event.edit('`"Make Peace, Not War."`')

    if x == 10:

        await event.edit('`"Do You Know what God Of Death Loves?\n\nApples!"`')

    if x == 11:

        await event.edit('`"Die Today to Rise Tomorrow."`')

    if x == 12:

        await event.edit('`"Weep Not for Roads Untravelled."`')

    if x == 13:

        await event.edit('`"What, If you can\'t love yourself....Better Die."`')

    if x == 14:

        await event.edit(
            '`"And the Shadow Of the Day, Will Embrace your World in Grey."`'
        )

    if x == 15:

        await event.edit(
            '`"I am.........Dying....wait NO..LOL No....I am.....Dyi----Fuck No wait.....I am a Shit...OK"`'
        )

    if x == 16:

        await event.edit('`"Mein Hertz Brent."`')

    if x == 17:

        await event.edit('`"My Heart Breaks...SHIT!"`')

    if x == 18:

        await event.edit('`"Hack IT!!"`')

    if x == 19:

        await event.edit('`"Y u do dis?\nI Cri Evri Tyme!"`')

    if x == 20:

        await event.edit('`"Do you know God Of Death Love Apples"`')

    if x == 21:

        await event.edit('`"Be a Warrior not a Worrier"`')

    if x == 22:

        await event.edit('`"SHUT UP!"`')

    if x == 23:

        await event.edit('`"Eat, Sleep, Code<<Kang>>, Repeat"`')

    if x == 24:

        await event.edit('`"Ever Thought of Using Baby Drags in Place of Drags?"`')

    # Hindi Time

    if x == 25:

        await event.edit('`"Har Kutta Apne Gali ka Sher Hota he!"`')

    if x == 26:

        await event.edit(
            '`"Kya Be PilPili Gaand, Bohot Shauk he Apna Gaand Chudwane ka?"`'
        )

    if x == 27:

        await event.edit('`"Murgi Pehle Ayi ya Anda?."`')

    if x == 28:

        await event.edit(
            '`"If you think this has a happy ending, you haven\'t been paying attention."`'
        )

    if x == 29:

        await event.edit('`"GirlFriend Banegi Meri?."`')

    # INGLIS MODE

    if x == 30:

        await event.edit('`"Whu is thet Fuking Beech?."`')

    if x == 31:

        await event.edit('`"U so Randi....Diye Soomn"`')

    if x == 32:

        await event.edit('`"Hey Romdi, When Sex."`')

    if x == 33:

        await event.edit('`"What Gunda Bonega re You?!"`')

    # Den-Shit Mode ON

    if x == 34:

        await event.edit(
            '`"Boda Boda Groups ka Admeme Hu Moi\nPonga Nohi Leneka Else Tumhore Group Me Super Purn Spammers Bhej Dunga\nMere Hi alt IDs He waise\nFirbhi\nKorbo Lorbo Gend me Lobo Lagbo Re\n\n~ Some Denzid(Dense-SHIT) Things"`'
        )


CMD_HELP.update(
    {
        "moithoughts": "**Moi Thoughts**\
\n\n**Syntax : **`.mts`\
\n**Usage :** Gives you Some Of Moi Englis, Hindi, INGLIS and Den-Shit [With Ganja] Mode Thoughts."
    }
)
