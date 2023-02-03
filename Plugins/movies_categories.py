import logging
logger = logging.getLogger(__name__)

from pyrogram import Client, filters
from bot import Star_Moviess_Tamil
from config import Config
from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, CallbackQuery
from movies import Movies
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

                  # Movies Categories

################################################################################################################################################################################################################################################

@Star_Moviess_Tamil.on_message(filters.command("tamil_movies") & filters.private & filters.incoming)
async def tamil_movies(client, message):
    await message.reply(
        text = Movies.TAMIL_MOVIES.format(
                mention = message.from_user.mention
            ),
        disable_web_page_preview=True,
        quote=True
    )

################################################################################################################################################################################################################################################
