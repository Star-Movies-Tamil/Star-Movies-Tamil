import logging
logger = logging.getLogger(__name__)

from pyrogram import Client, filters
from bot import channelforward
from config import ADMINS
from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, CallbackQuery
from translation import Translation
from pyrogram.errors import MessageNotModified, UserIsBlocked, InputUserDeactivated, FloodWait
from database.database import add_user, del_user, full_userbase, present_user
import random
import os
import asyncio

from Database import (
    get_users,
    del_from_userbase
)
from pyrogram.errors import (
    FloodWait,
    PeerIdInvalid,
    UserIsBlocked,
    InputUserDeactivated
)


################################################################################################################################################################################################################################################
# Start Command

START = "Translation.START"

TELETIPS_MAIN_MENU_BUTTONS = [
            [
                InlineKeyboardButton('👨‍💻 Creator', url='https://t.me/Star_Movies_Karthik')
            ],
            [
                InlineKeyboardButton('😎 About', callback_data="TUTORIAL_CALLBACK"),
                InlineKeyboardButton('👥 Support', callback_data="GROUP_CALLBACK"),
                InlineKeyboardButton('😁 Help', callback_data="HELP_CALLBACK")
            ],
            [
                InlineKeyboardButton('📣 Update Channel', url='https://t.me/Star_Moviess_Tamil')
            ]
        ]

@channelforward.on_message(filters.command('start') & filters.private)
async def start(client, message):
    reply_markup = InlineKeyboardMarkup(TELETIPS_MAIN_MENU_BUTTONS)
    await message.reply_text(
        text = Translation.START.format(
                mention = message.from_user.mention
            ),
        reply_markup=reply_markup,
        disable_web_page_preview=True
    )

@channelforward.on_callback_query()
async def callback_query(client: Client, query: CallbackQuery):
    if query.data=="HELP_CALLBACK":
        TELETIPS_HELP_BUTTONS = [
            [
                InlineKeyboardButton("⬅️ BACK", callback_data="START_CALLBACK")
            ]
            ]
        reply_markup = InlineKeyboardMarkup(TELETIPS_HELP_BUTTONS)
        try:
            await query.edit_message_text(
                Translation.HELP,
                disable_web_page_preview=True,
                reply_markup=reply_markup
            )
        except MessageNotModified:
            pass

    elif query.data=="GROUP_CALLBACK":
        TELETIPS_GROUP_BUTTONS = [
            [
                InlineKeyboardButton("Star Movies Feedback", url="https://t.me/Star_Movies_Feedback_Bot")
            ],
            [
                InlineKeyboardButton("⬅️ BACK", callback_data="START_CALLBACK"),
            ]
            ]
        reply_markup = InlineKeyboardMarkup(TELETIPS_GROUP_BUTTONS)
        try:
            await query.edit_message_text(
                Translation.SUPPORT,
                disable_web_page_preview=True,
                reply_markup=reply_markup
            )
        except MessageNotModified:
            pass    

    elif query.data=="TUTORIAL_CALLBACK":
        TELETIPS_TUTORIAL_BUTTONS = [
            [
                InlineKeyboardButton("🤵 Admin", url="https://t.me/Star_Movies_Karthik")
            ],
            [
                InlineKeyboardButton("⬅️ BACK", callback_data="START_CALLBACK"),
            ]
            ]
        reply_markup = InlineKeyboardMarkup(TELETIPS_TUTORIAL_BUTTONS)
        try:
            await query.edit_message_text(
                Translation.ABOUT,
                disable_web_page_preview=True,
                reply_markup=reply_markup
            )
        except MessageNotModified:
            pass      
          
    elif query.data=="START_CALLBACK":
        TELETIPS_START_BUTTONS = [
            [
                InlineKeyboardButton('👨‍💻 Creator', url='https://t.me/Star_Movies_Karthik')
            ],
            [
                InlineKeyboardButton('😎 About', callback_data="TUTORIAL_CALLBACK"),
                InlineKeyboardButton('👥 Support', callback_data="GROUP_CALLBACK"),
                InlineKeyboardButton('😁 Help', callback_data="HELP_CALLBACK")
            ],
            [
                InlineKeyboardButton('📣 Update Channel', url='https://t.me/Star_Moviess_Tamil')
            ]
        ]

        reply_markup = InlineKeyboardMarkup(TELETIPS_START_BUTTONS)
        try:
            await query.edit_message_text(
                text = Translation.START.format(
                        mention = query.from_user.mention
                    ),
                disable_web_page_preview=True,
                reply_markup=reply_markup
            )
        except MessageNotModified:
            pass    
        return


################################################################################################################################################################################################################################################
# Help Command

HELP = "Translation.HELP"

HELP_BUTTONS = [
            [
                InlineKeyboardButton('👨‍💻 Creator', url='https://t.me/Star_Movies_Karthik'),
                InlineKeyboardButton('📣 Update Channel', url='https://t.me/Star_Moviess_Tamil')
            ]
        ]

@channelforward.on_message(filters.command("help") & filters.private & filters.incoming)
async def help(client, message):
    text = Translation.HELP
    reply_markup = InlineKeyboardMarkup(HELP_BUTTONS)
    await message.reply_text(
        text = Translation.HELP.format(
                mention = message.from_user.mention
            ),
        reply_markup=reply_markup,
        disable_web_page_preview=True
    )

################################################################################################################################################################################################################################################
# About Command

ABOUT = "Translation.ABOUT"

ABOUT_BUTTONS = [
            [
                InlineKeyboardButton('👨‍💻 Creator', url='https://t.me/Star_Movies_Karthik'),
                InlineKeyboardButton('📣 Update Channel', url='https://t.me/Star_Moviess_Tamil')
            ]
        ]

@channelforward.on_message(filters.command("about") & filters.private & filters.incoming)
async def about(client, message):
    text = Translation.ABOUT
    reply_markup = InlineKeyboardMarkup(ABOUT_BUTTONS)
    await message.reply_text(
        text = Translation.ABOUT.format(
                mention = message.from_user.mention
            ),
        reply_markup=reply_markup,
        disable_web_page_preview=True
    )

################################################################################################################################################################################################################################################

WAIT_MSG = """"<b>Processing ...</b>"""

REPLY_ERROR = """<b>Use this command as a replay to any telegram message with out any spaces.</b>"""

################################################################################################################################################################################################################################################
# Total Users

@channelforward.on_message(filters.command('users') & filters.private & filters.user(ADMINS))
async def get_users(client, message):
    msg = await client.send_message(chat_id=message.chat.id, text=WAIT_MSG)
    users = await full_userbase()
    await msg.edit(f"<b>{len(users)} users are using this Bot</b>")

################################################################################################################################################################################################################################################
# Broadcast Message 

@channelforward.on_message(filters.private & filters.command('broadcast') & filters.user(ADMINS))
async def send_text(client, message):
    if message.reply_to_message:
        query = await full_userbase()
        broadcast_msg = message.reply_to_message
        total = 0
        successful = 0
        blocked = 0
        deleted = 0
        unsuccessful = 0
        
        pls_wait = await message.reply("<b>Broadcasting Message.. This will Take Some Time</b>")
        for chat_id in query:
            try:
                await broadcast_msg.copy(chat_id)
                successful += 1
            except FloodWait as e:
                await asyncio.sleep(e.x)
                await broadcast_msg.copy(chat_id)
                successful += 1
            except UserIsBlocked:
                await del_user(chat_id)
                blocked += 1
            except InputUserDeactivated:
                await del_user(chat_id)
                deleted += 1
            except:
                unsuccessful += 1
                pass
            total += 1
        
        status = f"""<b><u>Broadcast Completed</u>
Total Users: <code>{total}</code>
Successful: <code>{successful}</code>
Blocked Users: <code>{blocked}</code>
Deleted Accounts: <code>{deleted}</code>
Unsuccessful: <code>{unsuccessful}</code></b>"""
        
        return await pls_wait.edit(status)

    else:
        msg = await message.reply(REPLY_ERROR)
        await asyncio.sleep(8)

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

@channelforward.on_message(filters.private & filters.command('stats') & filters.user(ADMINS))
async def getstatus(client: CodeXBotz, message: Message):
    sts_msg = await message.reply('Getting Details..')
    stats = await get_status()
    await sts_msg.edit(stats)
    
@channelforward.on_message(filters.private & filters.command('broadcast') & filters.user(ADMINS) & filters.reply)
async def broadcast(client: CodeXBotz, message: Message):
    broadcast_msg = message.reply_to_message
    broadcast_msg = await broadcast_msg.copy(
        chat_id = message.chat.id,
        reply_to_message_id = broadcast_msg.message_id
    )
    await broadcast_msg.reply(
        text = 'Are you sure you want Broadcast this..',
        quote = True,
        reply_markup = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(text = 'Yes', callback_data = 'bdcast_cnfrm'),
                    InlineKeyboardButton(text = 'No', callback_data = 'close')
                ]
            ]
        )
    )
    return

@channelforward.on_callback_query(filters.admins & filters.regex('^bdcast_cnfrm$'))
async def broadcast_confrm(client: CodeXBotz, query):
    if not query.message.reply_to_message:
        await query.answer(
            text = 'Message not found',
            show_alert = True
        )
        await query.message.delete()
        return

    message = query.message.reply_to_message
    user_ids = await get_users()
    
    success = 0
    deleted = 0
    blocked = 0
    peerid = 0
    
    await query.message.edit(text = 'Broadcasting message, Please wait', reply_markup = None)
    
    for user_id in user_ids:
        try:
            await message.copy(user_id)
            success += 1
        except FloodWait as e:
            await asyncio.sleep(e.x)
            await message.copy(user_id)
            success += 1
        except UserIsBlocked:
            blocked += 1
        except PeerIdInvalid:
            peerid += 1
        except InputUserDeactivated:
            deleted += 1
            await del_from_userbase(user_id)
            
    text = f"""<b>Broadcast Completed</b>
    
Total users: {str(len(user_ids))}
Blocked users: {str(blocked)}
Deleted accounts: {str(deleted)} (<i>Deleted from Database</i>)
Failed : {str(peerid)}"""

    await query.message.reply(text)
