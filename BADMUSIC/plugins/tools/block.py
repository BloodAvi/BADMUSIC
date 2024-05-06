from pyrogram import Client, filters
import requests
import random
import os
import re
import asyncio
import time
from BADMUSIC import app

from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton


app.on_message(
    filters.command("donate")
    & filters.group)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://graph.org/file/ad98227d45e81687c3934.jpg",
        caption=f"""🥀 𝐂𝐥𝐢𝐜𝐤 𝐇𝐞𝐫𝐞 𝐅𝐨𝐫 𝐃𝐨𝐧𝐚𝐭𝐞 🥀""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🎁 𝐃ᴏɴᴀᴛᴇ 🎁", url=f"https://t.me/The_Coder_Network")
                ]
            ]
        ),
    )

@app.on_message(
    filters.command("donate")
    & filters.group)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://graph.org/file/ad98227d45e81687c3934.jpg",
        caption=f"""🥀 𝐂𝐥𝐢𝐜𝐤 𝐇𝐞𝐫𝐞 𝐅𝐨𝐫 𝐃𝐨𝐧𝐚𝐭𝐞 🥀""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🎁 𝐃ᴏɴᴀᴛᴇ 🎁", url=f"https://t.me/The_Coder_Network")
                ]
            ]
        ),
    )

@app.on_message(
    filters.command("donate")
    & filters.private)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://graph.org/file/ad98227d45e81687c3934.jpg",
        caption=f"""🥀 𝐂𝐥𝐢𝐜𝐤 𝐇𝐞𝐫𝐞 𝐅𝐨𝐫 𝐃𝐨𝐧𝐚𝐭𝐞 🥀""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🎁 𝐃ᴏɴᴀᴛᴇ 🎁", url=f"https://t.me/The_Coder_Network")
                ]
            ]
        ),
    )
