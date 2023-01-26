import logging
logger = logging.getLogger(__name__)

from pyrogram import filters
from bot import channelforward
from config import Config
from translation import Translation
import random
import os
import asyncio

################################################################################################################################################################################################################################################
# Start Command

@channelforward.on_message(filters.command("start") & filters.private & filters.incoming)
async def start(client, message):
    await message.reply(
    id = m.from_user.id
    user_name = '@' + message.from_user.username if message.from_user.username else None
    await add_user(id, user_name)
    await message.reply_text(Translation.START.format(message.from_user.mention(),
                       photo="https://telegra.ph/file/8bfb25704003a8b181400.jpg",
                       quote=True
                       )

################################################################################################################################################################################################################################################
# Help Command

@channelforward.on_message(filters.command("help") & filters.private & filters.incoming)
async def help(client, message):
    await message.reply(
        text=Translation.HELP,
        disable_web_page_preview=True,
        quote=True
    )

################################################################################################################################################################################################################################################
# About Command

@channelforward.on_message(filters.command("about") & filters.private & filters.incoming)
async def about(client, message):
    await message.reply(
        text=Translation.ABOUT,
        disable_web_page_preview=True,
        quote=True
    )

################################################################################################################################################################################################################################################

               # Star Movies Tamil

################################################################################################################################################################################################################################################
#Alien Covenant (2017)

@channelforward.on_message(filters.command("alien_covenant") & filters.private & filters.incoming)
async def alien_covenant(client, message):
    await message.reply_photo(
        caption = Translation.ALIEN_COVENANT.format(
                mention = message.from_user.mention
            ),
        photo="https://telegra.ph/file/206f9013802376b39ad03.jpg",
        quote=True
    )

################################################################################################################################################################################################################################################
