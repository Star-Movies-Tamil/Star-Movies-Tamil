import os
import logging
logger = logging.getLogger(__name__)

from pyrogram import filters
from bot import channelforward
from config import Config
from translation import Translation
import asyncio

################################################################################################################################################################################################################################################
# Start Command

@channelforward.on_message(filters.command("start") & filters.private & filters.incoming)
async def start(client, message):
    await message.reply_photo(
            text = Translation.START.format(m.from_user.mention),
                first = message.from_user.first_name,
                last = message.from_user.last_name,
                username = None if not message.from_user.username else '@' + message.from_user.username,
                mention = message.from_user.mention,
                id = message.from_user.id
            ),
        photo = "https://telegra.ph/file/bfbb76083b53fc50b1337.jpg",
        caption=Translation.START,
        reply_markup = reply_markup,
        quote = True
    )

################################################################################################################################################################################################################################################
# help command

@channelforward.on_message(filters.command("help") & filters.private & filters.incoming)
async def help(client, message):
    await message.reply(
        text=Translation.HELP,
        disable_web_page_preview=True,
        quote=True
    )

################################################################################################################################################################################################################################################
# about command

@channelforward.on_message(filters.command("about") & filters.private & filters.incoming)
async def about(client, message):
    await message.reply(
        text=Translation.ABOUT,
        disable_web_page_preview=True,
        quote=True
    )

################################################################################################################################################################################################################################################
