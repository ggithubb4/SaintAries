from telethon import Button

from aries import telethn as tbot
from aries.events import register

PHOTO = "https://te.legra.ph/file/5c4479cce9c1ca4d0c1b2.png"


@register(pattern=("/alive|/ALIVE"))
async def awake(event):
    event.sender.first_name
    ARIES = "**Hello im Saint Aries** \n\n"
    ARIES += "**ALL SYSTEM WORKING PROPERLY**\n\n"
    ARIES += " ☬ ⌊ **Python :** __3.9.7__ ⌉\n\n"
    ARIES += " ☬ ⌊ **Pyrogram :** __1.2.9__ ⌉\n\n"
    ARIES += " ☬ ⌊ **MongoDB :** __2.5.1__ ⌉\n\n"
    ARIES += " ☬ ⌊ **Platform :** __linux__ ⌉\n\n"
    ARIES += " ☬ ⌊ **My Lord** : [Artezid](https://t.me/{geronimo1234}) ☠⌉\n\n"
    ARIES += " ☬ ⌊ **ℝ𝕠𝕔𝕜𝕖𝕥** ⌉\n\n"
    ARIES += " ☬ ⌊ **TELETHON : 6.6.6 Latest** ⌉\n\n"
    ARIES += " |||| || ||| |||| || |||||| ||||| || || ||"
    BUTTON = [
        [
            Button.url("Updates", "https://t.me/check_this_channel"),
            Button.url("Channel", "https://t.me/international_free_movies"),
        ]
    ]
    await tbot.send_file(event.chat_id, PHOTO, caption=ARIES, buttons=BUTTON)


__mod_name__ = "Alive"
