import logging
logger = logging.getLogger(__name__)

from pyrogram import Client, filters
from bot import Star_Moviess_Tamil
from config import Config
from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, CallbackQuery
from poster import Poster
from pyrogram.errors import MessageNotModified, UserIsBlocked, InputUserDeactivated, FloodWait
import random
import os
import asyncio
import traceback

from pyrogram import Client
from pyrogram import StopPropagation, filters
from pyrogram.types import CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup
import config

################################################################################################################################################################################################################################################

                  # Star Movies Tamil

################################################################################################################################################################################################################################################
# Alien Covenant (2017)

@Star_Moviess_Tamil.on_message(filters.command("alien_covenant") & filters.private & filters.incoming)
async def alien_covenant(client, message):
    await message.reply_photo(
        caption = Poster.ALIEN_COVENANT.format(
                mention = message.from_user.mention
            ),
        photo="https://telegra.ph/file/206f9013802376b39ad03.jpg",
        quote=True,
    )

################################################################################################################################################################################################################################################
# Thunivu (2023)

@Star_Moviess_Tamil.on_message(filters.command("thunivu") & filters.private & filters.incoming)
async def thunivu(client, message):
    await message.reply_photo(
        caption = Poster.THUNIVU.format(
                mention = message.from_user.mention
            ),
        photo="https://telegra.ph/file/1919c316d8d742d1fa3ab.jpg",
        quote=True,
    )

################################################################################################################################################################################################################################################
# Varisu (2023)

@Star_Moviess_Tamil.on_message(filters.command("varisu") & filters.private & filters.incoming)
async def varisu(client, message):
    await message.reply_photo(
        caption = Poster.VARISU.format(
                mention = message.from_user.mention
            ),
        photo="https://telegra.ph/file/76ba5435a2983a6c42c80.jpg",
        quote=True,
    )

################################################################################################################################################################################################################################################


