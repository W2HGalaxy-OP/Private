import asyncio
from time import time
from datetime import datetime
from helpers.filters import command
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton



@Client.on_message(command("start") & filters.private & ~filters.edited)
async def start_(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://te.legra.ph/file/ca3727869034e09621b51.jpg",
        caption=f"""**𝐓𝐡𝐢𝐬 𝐈𝐬 𝐀𝐝𝐯𝐚𝐧𝐜𝐞 🥀𝐓𝐞𝐥𝐞𝐠𝐫𝐚𝐦 𝐌𝐮𝐬𝐢𝐜 🎶 𝐁𝐨𝐭 𝐑𝐮𝐧 𝐎𝐧 𝐏𝐫𝐢𝐯𝐚𝐭𝐞 🥀 𝐕𝐩𝐬 💫𝐒𝐞𝐫𝐯𝐞𝐫 🌎 𝐅𝐞𝐞𝐥 ❤️ 𝐇𝐢𝐠𝐡 𝐐𝐮𝐚𝐥𝐢𝐭𝐲 𝐌𝐮𝐬𝐢𝐜 🎧 𝐈𝐧 𝐕𝐜 𝐃𝐞𝐯𝐞𝐥𝐨𝐩𝐞𝐝 𝐁𝐲 = [𝐆𝐚𝐥𝐚𝐱𝐲_𝐎𝐩 ❤️](https://t.me/david99q)

𝐂𝐫𝐞𝐚𝐭𝐨𝐫 :- [✨ 𝗥𝗮𝘃𝗮𝗻_𝗢𝗽 💜](https://t.me/w2h_ravan)
𝐒𝐮𝐩𝐩𝐨𝐫𝐭 :- [✨ 𝗖𝗵𝗮𝗻𝗻𝗲𝗹 🌎🎸](https://t.me/W2H_Userbot)
𝐃𝐢𝐬𝐜𝐮𝐬𝐬 :- [✨  𝗦𝘂𝗽𝗽𝗼𝗿𝘁 ⚡🎧](https://t.me/w2hsupport)
𝐒𝐨𝐮𝐫𝐜𝐞  :- [✨  𝗖𝗹𝗶𝗰𝗸 ☑️ 𝗥𝗲𝗽𝗼 🌍](https://github.com/EsportMusicX/SmokerMusicX)
𝐂𝐨𝐦𝐦𝐚𝐧𝐝 :- [✨𝗖𝗹𝗶𝗰𝗸 ☑️ 𝗡𝗼𝘄 🚩](https://t.me/Ravan_FeeLingS)
𝐅𝐞𝐞𝐋𝐢𝐧𝐠'𝐒 :- [✨ 𝗖𝗵𝗮𝘁𝘁𝗶𝗻𝗴 💫](https://t.me/Ravan_FeeLingS)

𝐈𝐟 𝐘𝐨𝐮 𝐇𝐚𝐯𝐞 𝐀𝐧𝐲 𝐐𝐮𝐞𝐬𝐭𝐢𝐨𝐧𝐬 𝐀𝐧𝐝 𝐇𝐞𝐥𝐩 𝐓𝐡𝐞𝐧 𝐃𝐦 𝐌𝐲 𝐁𝐨𝐬𝐬 = [𝗥𝗮𝘃𝗮𝗻_𝗢𝗽 🚬 ❤️](https://t.me/w2h_ravan)**""",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🥀 Jᴏɪɴ Hᴇʀᴇ & Sᴜᴘᴘᴏʀᴛ ✨", url=f"https://t.me/W2H_Userbot")
                ]
                
           ]
        ),
    )
    

@Client.on_message(command(["repo"]) & filters.group & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://te.legra.ph/file/5f3af650e4c26e68287a8.jpg",
        caption=f"""""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "💥 Cʟɪᴄᴋ Mᴇ Tᴏ Gᴇᴛ Rᴇᴘᴏ 💞", url=f"https://github.com/EsportMusicX/SmokerMusicX")
                ]
            ]
        ),
    )
