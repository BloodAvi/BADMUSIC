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
    filters.command("repo")
    & filters.group)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://graph.org/file/ad98227d45e81687c3934.jpg",
        caption=f"""🦋 𝐂ʟɪᴄᴋ 𝐁ᴇʟᴏᴡ 𝐁ᴜᴛᴛᴏɴ 𝐓ᴏ 𝐆ᴇᴛ 𝐑ᴇᴘᴏ ❤️""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🗡️ 𝐑ᴇᴘᴏ 🗡️", url=f"https://graph.org/file/ad98227d45e81687c3934.jpg")
                ],
                [
                    InlineKeyboardButton(
                        "🗡️ 𝐑ᴇᴘᴏ  🗡️", url=f"https://graph.org/file/ad98227d45e81687c3934.jpg")
                ],
                 [
                    InlineKeyboardButton(
                        "🗡️ 𝐑ᴇᴘᴏ 🗡️", url=f"https://graph.org/file/ad98227d45e81687c3934.jpg")
                ],
                 [
                    InlineKeyboardButton(
                        "🗡️ 𝐑ᴇᴘᴏ 🗡️", url=f"https://graph.org/file/ad98227d45e81687c3934.jpg")
                 ]
            ]
        ),
    )

@app.on_message(
    filters.command("repo")
    & filters.group)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://graph.org/file/ad98227d45e81687c3934.jpg",
        caption=f"""🦋 𝐂ʟɪᴄᴋ 𝐁ᴇʟᴏᴡ 𝐁ᴜᴛᴛᴏɴ 𝐓ᴏ 𝐆ᴇᴛ 𝐑ᴇᴘᴏ ❤️""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🗡️ 𝐑ᴇᴘᴏ 🗡️", url=f"https://graph.org/file/ad98227d45e81687c3934.jpg")
                ],
                [
                    InlineKeyboardButton(
                        "🗡️ 𝐑ᴇᴘᴏ  🗡️", url=f"https://graph.org/file/ad98227d45e81687c3934.jpg")
                ],
                 [
                    InlineKeyboardButton(
                        "🗡️ 𝐑ᴇᴘᴏ 🗡️", url=f"https://graph.org/file/ad98227d45e81687c3934.jpg)
                ],
                 [
                    InlineKeyboardButton(
                        "🗡️ 𝐑ᴇᴘᴏ 🗡️", url=f"https://graph.org/file/ad98227d45e81687c3934.jpg")
                 ]
            ]
        ),
    )

@app.on_message(
    filters.command("repo")
    & filters.private)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://graph.org/file/ad98227d45e81687c3934.jpg",
        caption=f"""🦋 𝐂ʟɪᴄᴋ 𝐁ᴇʟᴏᴡ 𝐁ᴜᴛᴛᴏɴ 𝐓ᴏ 𝐆ᴇᴛ 𝐑ᴇᴘᴏ ❤️""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🗡️ 𝐑ᴇᴘᴏ 🗡️", url=f"https://graph.org/file/ad98227d45e81687c3934.jpg")
                ],
                [
                    InlineKeyboardButton(
                        "🗡️ 𝐑ᴇᴘᴏ  🗡️", url=f"https://graph.org/file/ad98227d45e81687c3934.jpg")
                ],
                 [
                    InlineKeyboardButton(
                        "🗡️ 𝐑ᴇᴘᴏ 🗡️", url=f"https://graph.org/file/ad98227d45e81687c3934.jpg")
                ],
                 [
                    InlineKeyboardButton(
                        "🗡️ 𝐑ᴇᴘᴏ 🗡️", url=f"https://graph.org/file/ad98227d45e81687c3934.jpg")
                 ]
            ]
        ),
    )
  
