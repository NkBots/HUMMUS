import sys
import asyncio
import requests
import re
import string
from pyrogram.types import Message
from aiohttp import ClientSession
from pyrogram import filters, Client
from strings import get_command
from pyrogram.types import (InlineKeyboardButton,CallbackQuery,InlineKeyboardMarkup, Message)
from YukkiMusic import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)

#########
#الاوامر
@app.on_message(
    filters.command(["سورس","السورس"],""))
async def khalid(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/7e51929d9635e47097113.jpg",
        caption=f"""✅ مرحبا بك عزيزي {message.from_user.mention}""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                InlineKeyboardButton("𝑫𝒆𝒗𝒆𝒍𝒐𝒑𝒆𝒓", url=f"https://t.me/MIDO_Jr"),
                ],[
                InlineKeyboardButton(
                        "𝑺𝒐𝒖𝒓𝒄𝒆", url=f"https://t.me/Just_Ghosst"),
                ],[
                InlineKeyboardButton("✚ أضفني الى مجموعتك", url=f"https://t.me/{BOT_USERNAME}?startgroup=true"),
            ]
        ]
         ),
     )
@app.on_message(
    filters.command(["مطور","المطور"],""))
async def khalid(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/7e51929d9635e47097113.jpg",
        caption=f"""✅ مرحبا بك عزيزي {message.from_user.mention}""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                InlineKeyboardButton("𝑫𝒆𝒗𝒆𝒍𝒐𝒑𝒆𝒓", url=f"https://t.me/MIDO_Jr"),
                ],[
                InlineKeyboardButton(
                        "𝑺𝒐𝒖𝒓𝒄𝒆", url=f"https://t.me/Just_Ghosst"),
                ],[
                InlineKeyboardButton("✚ أضفني الى مجموعتك", url=f"https://t.me/{BOT_USERNAME}?startgroup=true"),
            ]
        ]
         ),
     )     
@app.on_message(
    filters.command(["ايدي","ا","id"],""))
async def khalid(client: Client, message: Message):
    usr = await client.get_users(message.from_user.id)
    name = usr.first_name
    async for photo in client.iter_profile_photos(message.from_user.id, limit=1):
                    await message.reply_photo(photo.file_id,       caption=f"""أسمك {message.from_user.mention}\n\nمعرفك @{message.from_user.username}\n\nآيديك {message.from_user.id}\n\nآيدي الكروب {message.chat.id}""", 
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "𝑺𝒐𝒖𝒓𝒄𝒆", url=f"https://t.me/MIDO_Jr"),
                ],
            ]
        ),
@app.on_message(
    filters.command(["الاوامر","اوامر"],""))
async def khalid(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/7e51929d9635e47097113.jpg",
        caption=f"""✅ مرحبا بك عزيزي {message.from_user.mention}
     
« اليك قائـمة الاوامــر »
•═════• [⌞ 𝙻𝙾𝚂𝚃 𝚆𝙾𝚁𝙳𝚂 ⌝](https://t.me/FH_KP) •═════•

- لتشغيل اغنيه اكتب : تشغيل او شغل او /play
- لتشغيل فيديو اكتب : فيديو او /video
- لأنهاء الاغنيه اكتب : ايقاف او انهاء او /stop
- لايقاف الاغنيه مؤقت اكتب : قف او /pause
- لتكملة الاغنيه من الايقاف المؤقت اكتب : كمل او /resume
- لتخطي الاغنيه اكتب : تخطي او /skip
- لكتم البوت في المحادثه اكتب : ڪتم او /mute
- لألغاء كتم البوت في المحادثه اكتب : اتكلم او /unmute
- لاعادة تشغيل البوت اكتب : /restart""
 
•═════•م [⌞ 𝙻𝙾𝚂𝚃 𝚆𝙾𝚁𝙳𝚂 ⌝](https://t.me/FH_KP) •═════•
1 ← اوامـر الميـوزك .""",
reply_markup=InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                        "𝑫𝒆𝒗𝒆𝒍𝒐𝒑𝒆𝒓", url=f"https://t.me/MIDO_Jr"),
            ],[
                InlineKeyboardButton("✚ أضفني الى مجموعتك", url=f"https://t.me/{BOT_USERNAME}?startgroup=true"),
            ]
        ]
         ),
     )
     