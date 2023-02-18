import logging
logger = logging.getLogger(__name__)

from pyrogram import Client, filters
from bot import Star_Moviess_Tamil
from config import Config
from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, CallbackQuery
from categories import Categories
from pyrogram.errors import MessageNotModified, UserIsBlocked, InputUserDeactivated, FloodWait
import random
import os
import asyncio
import traceback
from Plugins.category_link import *
from pyrogram import Client
from pyrogram import StopPropagation, filters
from pyrogram.types import CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup
import config

################################################################################################################################################################################################################################################

                  # Movies Categories

################################################################################################################################################################################################################################################
# Tamil Movies

@Star_Moviess_Tamil.on_message(tamil_movies_filter)
async def tamil_movies(client, message):
    await message.reply(
        text = Categories.TAMIL_MOVIES.format(
                mention = message.from_user.mention
            ),
        disable_web_page_preview=True,
        quote=True
    )

################################################################################################################################################################################################################################################
# Hollywood Movies

@Star_Moviess_Tamil.on_message(hollywood_movies_filter)
async def hollywood_movies(client, message):
    await message.reply(
        text = Categories.HOLLYWOOD_MOVIES.format(
                mention = message.from_user.mention
            ),
        disable_web_page_preview=True,
        quote=True
    )

################################################################################################################################################################################################################################################
# Web Series

@Star_Moviess_Tamil.on_message(web_series_filter)
async def web_series(client, message):
    await message.reply(
        text = Categories.WEB_SERIES.format(
                mention = message.from_user.mention
            ),
        disable_web_page_preview=True,
        quote=True
    )

################################################################################################################################################################################################################################################
# Movie Collection

@Star_Moviess_Tamil.on_message(movie_collection_filter)
async def movie_collection(client, message):
    await message.reply(
        text = Categories.MOVIE_COLLECTION.format(
                mention = message.from_user.mention
            ),
        disable_web_page_preview=True,
        quote=True
    )

################################################################################################################################################################################################################################################
# Cartoon Movies

@Star_Moviess_Tamil.on_message(cartoon_movies_filter)
async def cartoon_movies(client, message):
    await message.reply(
        text = Categories.CARTOON_MOVIES.format(
                mention = message.from_user.mention
            ),
        disable_web_page_preview=True,
        quote=True
    )

################################################################################################################################################################################################################################################
# TV Shows

@Star_Moviess_Tamil.on_message(tv_shows_filter)
async def tv_shows(client, message):
    await message.reply(
        text = Categories.TV_SHOWS.format(
                mention = message.from_user.mention
            ),
        disable_web_page_preview=True,
        quote=True
    )

################################################################################################################################################################################################################################################

