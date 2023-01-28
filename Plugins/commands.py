import logging
logger = logging.getLogger(__name__)

from pyrogram import filters
from bot import channelforward
from config import Config
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
from translation import Translation
import random
import os
import asyncio

################################################################################################################################################################################################################################################
# Start Command

START = "Translation.START"
START_BUTTON = [
    [
        InlineKeyboardButton('😁 Help', callback_data="help")
    ]
]
@channelforward.on_message(filters.command("start") & filters.private & filters.incoming)
async def start(client, message):
    await message.reply_photo(
        caption = Translation.START.format(
                mention = message.from_user.mention
            ),
        photo="https://telegra.ph/file/8bfb25704003a8b181400.jpg",
        quote=True,
        reply_markup = InlineKeyboardMarkup(START_BUTTON)
    )
@channelforward.on_callback_query()
def callback_query(Client, CallbackQuery):
    if CallbackQuery.data == "help":

         HELP = "Translation.HELP"
         HELP_BUTTON = [
    [
        InlineKeyboardButton('🏠 Home', callback_data="home"),
        InlineKeyboardButton('😎 About', callback_data="about")
    ]
]
CallbackQuery.edit_message_text(
            HELP,
            reply_markup = InlineKeyboardMarkup(HELP_BUTTON)
        )
    if CallbackQuery.data == "home":
CallbackQuery.edit_message_text(
            START,
            reply_markup = InlineKeyboardMarkup(START_BUTTON)
        )
    if CallbackQuery.data == "about":
         ABOUT = "Translation.ABOUT"
         ABOUT_BUTTON = [
    [
        InlineKeyboardButton('🏠 Home', callback_data="home"),
        InlineKeyboardButton('😁 Help', callback_data="help")
    ]
]
CallbackQuery.edit_message_text(
            ABOUT,
            reply_markup = InlineKeyboardMarkup(ABOUT_BUTTON)
        )
    if CallbackQuery.data == "start":
         START = "Translation.START"
         START_BUTTON = [
    [
        InlineKeyboardButton('😎 About', callback_data="about")
    ]
]
CallbackQuery.edit_message_text(
            START,
            reply_markup = InlineKeyboardMarkup(START_BUTTON)
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
