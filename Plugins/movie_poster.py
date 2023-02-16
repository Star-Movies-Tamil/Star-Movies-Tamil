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
from Plugins.link import *
from pyrogram import Client
from pyrogram import StopPropagation, filters
from pyrogram.types import CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup
import config

################################################################################################################################################################################################################################################

                  # Star Movies Tamil

################################################################################################################################################################################################################################################
# Alien Covenant (2017)

ALIEN_COVENANT = "Poster.ALIEN_COVENANT"

ALIEN_COVENANT_BUTTONS = [
            [
                InlineKeyboardButton('👨‍💻 Creator', url='https://t.me/Star_Movies_Karthik'),
                InlineKeyboardButton('📣 Update Channel', url='https://t.me/Star_Moviess_Tamil')
            ]
        ]

@Star_Moviess_Tamil.on_message(filters.command("alien_covenant") & filters.private & filters.incoming)
async def alien_covenant(client, message):
    text = Poster.ALIEN_COVENANT
    reply_markup = InlineKeyboardMarkup(ALIEN_COVENANT_BUTTONS)
    await message.reply_photo(
        caption = Poster.ALIEN_COVENANT.format(
                mention = message.from_user.mention
            ),
        photo="https://telegra.ph/file/206f9013802376b39ad03.jpg",
        quote=True,reply_markup=ALIEN_COVENANT_BUTTONS
    )
@Star_Moviess_Tamil.on_message(alien_covenant_filter)
async def alien_covenant_f(client, message):
    text = Poster.ALIEN_COVENANT
    reply_markup = InlineKeyboardMarkup(ALIEN_COVENANT_BUTTONS)
    await message.reply_photo(
        caption = Poster.ALIEN_COVENANT.format(
                mention = message.from_user.mention
            ),
        photo="https://telegra.ph/file/206f9013802376b39ad03.jpg",
        quote=True,reply_markup=ALIEN_COVENANT_BUTTONS
    )

################################################################################################################################################################################################################################################
# Thunivu (2023)

THUNIVU = "Poster.THUNIVU"

THUNIVU_BUTTONS = [
            [
                InlineKeyboardButton('👨‍💻 Creator', url='https://t.me/Star_Movies_Karthik'),
                InlineKeyboardButton('📣 Update Channel', url='https://t.me/Star_Moviess_Tamil')
            ]
        ]

@Star_Moviess_Tamil.on_message(filters.command("thunivu") & filters.private & filters.incoming)
async def thunivu(client, message):
    text = Poster.THUNIVU
    reply_markup = InlineKeyboardMarkup(THUNIVU_BUTTONS)
    await message.reply_photo(
        caption = Poster.THUNIVU.format(
                mention = message.from_user.mention
            ),
        photo="https://telegra.ph/file/1919c316d8d742d1fa3ab.jpg",
        quote=True,reply_markup=THUNIVU_BUTTONS
    )
@Star_Moviess_Tamil.on_message(thunivu_filter)
async def thunivu_f(client, message):
    text = Poster.THUNIVU
    reply_markup = InlineKeyboardMarkup(THUNIVU_BUTTONS)
    await message.reply_photo(
        caption = Poster.THUNIVU.format(
                mention = message.from_user.mention
            ),
        photo="https://telegra.ph/file/1919c316d8d742d1fa3ab.jpg",
        quote=True,reply_markup=THUNIVU_BUTTONS
    )
@Star_Moviess_Tamil.on_message(thunivu_page2_filter)
async def thunivu_page2_f(client, message):
    text = Poster.THUNIVU_PAGE2
    reply_markup = InlineKeyboardMarkup(THUNIVU_BUTTONS)
    await message.reply_photo(
        caption = Poster.THUNIVU_PAGE2.format(
                mention = message.from_user.mention
            ),
        photo="https://telegra.ph/file/1919c316d8d742d1fa3ab.jpg",
        quote=True,reply_markup=THUNIVU_BUTTONS
    )

################################################################################################################################################################################################################################################
# Varisu (2023)

VARISU = "Poster.VARISU"

VARISU_BUTTONS = [
            [
                InlineKeyboardButton('👨‍💻 Creator', url='https://t.me/Star_Movies_Karthik'),
                InlineKeyboardButton('📣 Update Channel', url='https://t.me/Star_Moviess_Tamil')
            ]
        ]

@Star_Moviess_Tamil.on_message(filters.command("varisu") & filters.private & filters.incoming)
async def varisu(client, message):
    text = Poster.VARISU
    reply_markup = InlineKeyboardMarkup(VARISU_BUTTONS)
    await message.reply_photo(
        caption = Poster.VARISU.format(
                mention = message.from_user.mention
            ),
        photo="https://telegra.ph/file/76ba5435a2983a6c42c80.jpg",
        quote=True,reply_markup=VARISU_BUTTONS
    )
@Star_Moviess_Tamil.on_message(varisu_filter)
async def varisu_f(client, message):
    text = Poster.VARISU
    reply_markup = InlineKeyboardMarkup(VARISU_BUTTONS)
    await message.reply_photo(
        caption = Poster.VARISU.format(
                mention = message.from_user.mention
            ),
        photo="https://telegra.ph/file/76ba5435a2983a6c42c80.jpg",
        quote=True,reply_markup=VARISU_BUTTONS
    )

################################################################################################################################################################################################################################################


