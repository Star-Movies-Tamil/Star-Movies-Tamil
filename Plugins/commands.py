import logging
logger = logging.getLogger(__name__)

from pyrogram import Client, filters
from bot import Star_Moviess_Tamil
from config import ADMINS, AUTH_USERS, FILE_STORE_CHANNEL
from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, CallbackQuery
from translation import Translation
from pyrogram.errors import MessageNotModified, UserIsBlocked, InputUserDeactivated, FloodWait
import random
import os
import asyncio
import traceback
import base64

from pyrogram import Client
from pyrogram import StopPropagation, filters
from pyrogram.types import CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup

import config
from handlers.broadcast import broadcast
from handlers.check_user import handle_user_status
from handlers.database import Database

async def allowed(_, __, message):
    if PUBLIC_FILE_STORE:
        return True
    if message.from_user and message.from_user.id in ADMINS:
        return True
    return False

LOG_CHANNEL = config.LOG_CHANNEL
AUTH_USERS = config.AUTH_USERS
DB_URL = config.DB_URL
DB_NAME = config.DB_NAME

db = Database(DB_URL, DB_NAME)

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

@Star_Moviess_Tamil.on_message(filters.private)
async def _(bot, cmd):
    await handle_user_status(bot, cmd)

    chat_id = message.from_user.id
    if not await db.is_user_exist(chat_id):
        data = await client.get_me()
        BOT_USERNAME = data.username
        await db.add_user(chat_id)
        if LOG_CHANNEL:
            await client.send_message(
                LOG_CHANNEL,
                f"**#New_User :- \n\nNew User [{message.from_user.first_name}](tg://user?id={message.from_user.id}) started @{BOT_USERNAME} !!**",
            )
        else:
            logging.info(f"New User :- Name :- {message.from_user.first_name} ID :- {message.from_user.id}")

@Star_Moviess_Tamil.on_message(filters.command('start') & filters.private)
async def start(client, message):
    reply_markup = InlineKeyboardMarkup(TELETIPS_MAIN_MENU_BUTTONS)
    await message.reply_text(
        text = Translation.START.format(
                mention = message.from_user.mention
            ),
        reply_markup=reply_markup,
        disable_web_page_preview=True,
        quote=True
    )
    raise StopPropagation

@Star_Moviess_Tamil.on_callback_query()
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
                text = Translation.HELP.format(
                        mention = query.from_user.mention
                    ),
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
                text = Translation.SUPPORT.format(
                        mention = query.from_user.mention
                    ),
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
                text = Translation.ABOUT.format(
                        mention = query.from_user.mention
                    ),
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

@Star_Moviess_Tamil.on_message(filters.command("help") & filters.private & filters.incoming)
async def help(client, message):
    text = Translation.HELP
    reply_markup = InlineKeyboardMarkup(HELP_BUTTONS)
    await message.reply_text(
        text = Translation.HELP.format(
                mention = message.from_user.mention
            ),
        reply_markup=reply_markup,
        disable_web_page_preview=True,
        quote=True
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

@Star_Moviess_Tamil.on_message(filters.command("about") & filters.private & filters.incoming)
async def about(client, message):
    text = Translation.ABOUT
    reply_markup = InlineKeyboardMarkup(ABOUT_BUTTONS)
    await message.reply_text(
        text = Translation.ABOUT.format(
                mention = message.from_user.mention
            ),
        reply_markup=reply_markup,
        disable_web_page_preview=True,
        quote=True
    )

################################################################################################################################################################################################################################################

REPLY_ERROR = """<b>Use This Command as a Reply to any Telegram Message Without any Spaces.</b>"""

################################################################################################################################################################################################################################################
# Bot Settings

@Star_Moviess_Tamil.on_message(filters.command("settings"))
async def opensettings(bot, cmd):
    user_id = cmd.from_user.id
    await cmd.reply_text(
        f"**Here You Can Set Your Settings :-\n\nSuccessfully setted Notifications to {await db.get_notif(user_id)}**",
        quote=True,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        f"NOTIFICATION  {'🔔' if ((await db.get_notif(user_id)) is True) else '🔕'}",
                        callback_data="notifon",
                    )
                ],
                [InlineKeyboardButton("❎", callback_data="closeMeh")],
            ]
        ),
    )

@Star_Moviess_Tamil.on_callback_query()
async def callback_handlers(bot: Client, cb: CallbackQuery):
    user_id = cb.from_user.id
    if cb.data == "notifon":
        notif = await db.get_notif(cb.from_user.id)
        if notif is True:
            await db.set_notif(user_id, notif=False)
        else:
            await db.set_notif(user_id, notif=True)
        await cb.message.edit(
            f"**Here You Can Set Your Settings :-\n\nSuccessfully setted Notifications to {await db.get_notif(user_id)}**",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(
                            f"NOTIFICATION  {'🔔' if ((await db.get_notif(user_id)) is True) else '🔕'}",
                            callback_data="notifon",
                        )
                    ],
                    [InlineKeyboardButton("❎", callback_data="closeMeh")],
                ]
            ),
        )
        await cb.answer(
            f"**Successfully setted Notifications to {await db.get_notif(user_id)}**"
        )
    else:
        await cb.message.delete(True)


################################################################################################################################################################################################################################################
# Broadcast Message 

@Star_Moviess_Tamil.on_message(filters.private & filters.command("broadcast"))
async def broadcast_handler_open(_, m):
    if m.from_user.id not in AUTH_USERS:
        await m.delete()
        return
    if m.reply_to_message is None:
        await m.reply(REPLY_ERROR, quote=True)
    else:
        await broadcast(m, db)

################################################################################################################################################################################################################################################
# Total Users in Database 📂

@Star_Moviess_Tamil.on_message(filters.private & filters.command("stats"))
async def sts(c, m):
    if m.from_user.id not in AUTH_USERS:
        await m.delete()
        return
    await m.reply_text(
        text=f"**Total Users in Database 📂 :- {await db.total_users_count()}\n\nTotal Users with Notification Enabled 🔔 :- {await db.total_notif_users_count()}**",
        quote=True
    )

################################################################################################################################################################################################################################################
# Ban The User

@Star_Moviess_Tamil.on_message(filters.private & filters.command("ban_user"))
async def ban(c, m):
    if m.from_user.id not in AUTH_USERS:
        await m.delete()
        return
    if len(m.command) == 1:
        await m.reply_text(
            f"**Use This Command to Ban 🛑 any User From the Bot 🤖.\n\nUsage:-\n\n/ban_user user_id ban_duration ban_reason\n\n Example :- /ban_user 1234567 28 You Misused me.\n This Will Ban User with ID `1234567` for `28` Days for the Reason `You Misused me`.**",
            quote=True,
        )
        return

    try:
        user_id = int(m.command[1])
        ban_duration = int(m.command[2])
        ban_reason = " ".join(m.command[3:])
        ban_log_text = f"**Banning user {user_id} for {ban_duration} Days for the Reason {ban_reason}.**"

        try:
            await c.send_message(
                user_id,
                f"**You are Banned 🚫 to Use This Bot for {ban_duration} day(s) for the reason __{ban_reason}__ \n\nMessage from the Admin 🤠**",
            )
            ban_log_text += "**\n\nUser Notified Successfully!!**"
        except BaseException:
            traceback.print_exc()
            ban_log_text += (
                f"**\n\n ⚠️ User Notification Failed! ⚠️ \n\n`{traceback.format_exc()}`**"
            )
        await db.ban_user(user_id, ban_duration, ban_reason)
        print(ban_log_text)
        await m.reply_text(ban_log_text, quote=True)
    except BaseException:
        traceback.print_exc()
        await m.reply_text(
            f"**Error Occurred ⚠️! Traceback Given below\n\n`{traceback.format_exc()}`**",
            quote=True
        )

################################################################################################################################################################################################################################################
# Unban User

@Star_Moviess_Tamil.on_message(filters.private & filters.command("unban_user"))
async def unban(c, m):
    if m.from_user.id not in AUTH_USERS:
        await m.delete()
        return
    if len(m.command) == 1:
        await m.reply_text(
            f"**Use this Command to Unban 😃 Any user.\n\nUsage:\n\n`/unban_user user_id`\n\nEg: `/unban_user 1234567`\n This will unban user with id `1234567`.**",
            quote=True,
        )
        return

    try:
        user_id = int(m.command[1])
        unban_log_text = f"Unbanning user 🤪 {user_id}"

        try:
            await c.send_message(user_id, f"Your ban was lifted!")
            unban_log_text += "**\n\n✅ User Notified Successfully!! ✅**"
        except BaseException:
            traceback.print_exc()
            unban_log_text += (
                f"**\n\n⚠️ User Notification Failed! ⚠️\n\n`{traceback.format_exc()}`**"
            )
        await db.remove_ban(user_id)
        print(unban_log_text)
        await m.reply_text(unban_log_text, quote=True)
    except BaseException:
        traceback.print_exc()
        await m.reply_text(
            f"**⚠️ Error Occurred ⚠️! Traceback Given below\n\n`{traceback.format_exc()}`**",
            quote=True,
        )

################################################################################################################################################################################################################################################
# Banned Users

@Star_Moviess_Tamil.on_message(filters.private & filters.command("banned_users"))
async def _banned_usrs(c, m):
    if m.from_user.id not in AUTH_USERS:
        await m.delete()
        return
    all_banned_users = await db.get_all_banned_users()
    banned_usr_count = 0
    text = ""
    async for banned_user in all_banned_users:
        user_id = banned_user["id"]
        ban_duration = banned_user["ban_status"]["ban_duration"]
        banned_on = banned_user["ban_status"]["banned_on"]
        ban_reason = banned_user["ban_status"]["ban_reason"]
        banned_usr_count += 1
        text += f"> **User ID :- `{user_id}`, Ban Duration :- `{ban_duration}`, Banned on :- `{banned_on}`, Reason :- `{ban_reason}`\n\n**"
    reply_text = f"**Total banned user(s) 🤭: `{banned_usr_count}`\n\n{text}**"
    if len(reply_text) > 4096:
        with open("banned-users.txt", "w") as f:
            f.write(reply_text)
        await m.reply_document("banned-users.txt", True)
        os.remove("banned-users.txt")
        return
    await m.reply_text(reply_text, True)


@Star_Moviess_Tamil.on_callback_query()
async def callback_handlers(bot: Client, cb: CallbackQuery):
    user_id = cb.from_user.id
    if cb.data == "notifon":
        notif = await db.get_notif(cb.from_user.id)
        if notif is True:
            await db.set_notif(user_id, notif=False)
        else:
            await db.set_notif(user_id, notif=True)
        await cb.message.edit(
            f"**Here You Can Set Your Settings :-\n\nSuccessfully setted Notifications to {await db.get_notif(user_id)}**",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(
                            f"NOTIFICATION  {'🔔' if ((await db.get_notif(user_id)) is True) else '🔕'}",
                            callback_data="notifon",
                        )
                    ],
                    [InlineKeyboardButton("❎", callback_data="closeMeh")],
                ]
            ),
        )
        await cb.answer(
            f"**Successfully setted Notifications to {await db.get_notif(user_id)}**"
        )
    else:
        await cb.message.delete(True)

################################################################################################################################################################################################################################################
# Reply to a Message or a File 📂. I Will Give You a Sharable Permanent Link

@Star_Moviess_Tamil.on_message(filters.command('link') & filters.create(allowed))
async def gen_link_s(client, message):
    replied = message.reply_to_message
    if not replied:
        return await message.reply('**Reply to a Message or a File. I Will Give You a Sharable Permanent Link**')
    file_type = replied.media
    if file_type not in [enums.MessageMediaType.VIDEO, enums.MessageMediaType.AUDIO, enums.MessageMediaType.DOCUMENT]:
        return await message.reply("**Reply to a Support Media")
    if message.has_protected_content and message.chat.id not in ADMINS:
        return await message.reply("**Ok Bro**")
    file_id, ref = unpack_new_file_id((getattr(replied, file_type.value)).file_id)
    string = 'filep_' if message.text.lower().strip() == "/plink" else 'file_'
    string += file_id
    outstr = base64.urlsafe_b64encode(string.encode("ascii")).decode().strip("=")
    await message.reply(f"<b>⪼ Here is Your File Link :\nhttps://telegram.me/{temp.U_NAME}?start={outstr}</b>")
    
################################################################################################################################################################################################################################################
# Get Multiple Files 📂 in One Link

@Star_Moviess_Tamil.on_message(filters.command('batch') & filters.create(allowed))
async def gen_link_batch(bot, message):
    if " " not in message.text:
        return await message.reply("**Use Correct Format.**")
    links = message.text.strip().split(" ")
    if len(links) != 3:
        return await message.reply("**Use Correct Format.**")
    cmd, first, last = links
    regex = re.compile("(https://)?(t\.me/|telegram\.me/|telegram\.dog/)(c/)?(\d+|[a-zA-Z_0-9]+)/(\d+)$")
    match = regex.match(first)
    if not match:
        return await message.reply('Invalid link')
    f_chat_id = match.group(4)
    f_msg_id = int(match.group(5))
    if f_chat_id.isnumeric():
        f_chat_id  = int(("-100" + f_chat_id))

    match = regex.match(last)
    if not match:
        return await message.reply('Invalid link')
    l_chat_id = match.group(4)
    l_msg_id = int(match.group(5))
    if l_chat_id.isnumeric():
        l_chat_id  = int(("-100" + l_chat_id))

    if f_chat_id != l_chat_id:
        return await message.reply("**Chat IDs not Matched.**")
    try:
        chat_id = (await bot.get_chat(f_chat_id)).id
    except ChannelInvalid:
        return await message.reply('**This My Be a Private Channel/ Group. Make Me An Admin Over There to Index The Files 📂.**')
    except (UsernameInvalid, UsernameNotModified):
        return await message.reply('Invalid Link specified.')
    except Exception as e:
        return await message.reply(f'Errors - {e}')

    sts = await message.reply("**Generating Link For Your Message.\nThis Maybe Take Time Depending Upon The Number of Messages**")
    if chat_id in FILE_STORE_CHANNEL:
        string = f"{f_msg_id}_{l_msg_id}_{chat_id}_{cmd.lower().strip()}"
        b_64 = base64.urlsafe_b64encode(string.encode("ascii")).decode().strip("=")
        return await sts.edit(f"<b>⪼ 𝙷𝙴𝚁𝙴 𝙸𝚂 𝚈𝙾𝚄𝚁 𝙻𝙸𝙽𝙺 ›› https://t.me/{temp.U_NAME}?start=DSTORE-{b_64}</b>")

    FRMT = "<b>╭━━━━━━━━━━━━━━━➣\n┣⪼Generating Link...\n┣⪼Total Messages : `{total}`\n┣⪼Done : `{current}`\n┣⪼Remaining : `{rem}`\n┣⪼Status : `{sts}`\n╰━━━━━━━━━━━━━━━➣</b>"

    outlist = []

    # file store without db channel
    og_msg = 0
    tot = 0
    async for msg in bot.iter_messages(f_chat_id, l_msg_id, f_msg_id):
        tot += 1
        if msg.empty or msg.service:
            continue
        if not msg.media:
            # only media messages supported.
            continue
        try:
            file_type = msg.media
            file = getattr(msg, file_type.value)
            caption = getattr(msg, 'caption', '')
            if caption:
                caption = caption.html
            if file:
                file = {
                    "file_id": file.file_id,
                    "caption": caption,
                    "title": getattr(file, "file_name", ""),
                    "size": file.file_size,
                    "protect": cmd.lower().strip() == "/pbatch",
                }

                og_msg +=1
                outlist.append(file)
        except:
            pass
        if not og_msg % 20:
            try:
                await sts.edit(FRMT.format(total=l_msg_id-f_msg_id, current=tot, rem=((l_msg_id-f_msg_id) - tot), sts="Saving Messages"))
            except:
                pass
    with open(f"batchmode_{message.from_user.id}.json", "w+") as out:
        json.dump(outlist, out)
    post = await bot.send_document(LOG_CHANNEL, f"batchmode_{message.from_user.id}.json", file_name="Batch.json", caption="<b>👩🏻‍💻 File Store Logs 👩🏻‍💻</b>")
    os.remove(f"batchmode_{message.from_user.id}.json")
    file_id, ref = unpack_new_file_id(post.document.file_id)
    await sts.edit(f"<b>⪼Here is Your Link\nContains `{og_msg}` Files.\n https://telegram.me/{temp.U_NAME}?start=BATCH-{file_id}</b>")
