from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, CallbackQuery

# Callback Query

START = """<b>Hi 👋🏻 {mention},
I'm UK Studios Official a Bot to Maintain Your Channels. I am very useful for the Channel Admin who have many Channels.

See /help for More Details.

Maintained By : [Karthik](https://t.me/HMTD_Karthik)</b>"""

START_BUTTON = [
            [
                InlineKeyboardButton('❓ HELP', callback_data="HELP_CALLBACK")
            ],
            [
                InlineKeyboardButton('👥 SUPPORT', callback_data="GROUP_CALLBACK"),
                InlineKeyboardButton('📣 CHANNEL', url='https://t.me/teletipsofficialchannel'),
                InlineKeyboardButton('👨‍💻 CREATOR', url='https://t.me/teIetips')
            ],
            [
                InlineKeyboardButton('➕ CREATE YOUR BOT ➕', callback_data="TUTORIAL_CALLBACK")
            ]
        ]

@bot.on_message(filters.command("start") & filters.private)
def start(bot, message):
    message.reply(
        text = START,
        mention = message.from_user.mention,
        quote=True,
        reply_markup = InlineKeyboardMarkup(START_BUTTON)
    )

@bot.on_callback_query()
def callback_query(Client, CallbackQuery):
    if CallbackQuery.data == "START READING":

         PAGE1_TEXT = "ithu Help Message"
         PAGE1_BUTTON = [
    [
        InlineKeyboardButton('BACK TO MENU', callback_data="GO TO MENU"),
        InlineKeyboardButton('READ PAGE 2', callback_data="GO TO PAGE 2")
    ]
]

        CallbackQuery.edit_message_text(
            PAGE1_TEXT,
            reply_markup = InlineKeyboardMarkup(PAGE1_BUTTON)
        )
    elif CallbackQuery.data == "GO TO MENU":
            CallbackQuery.edit_message_text(
            START,
            reply_markup = InlineKeyboardMarkup(START_BUTTON)
        )

    elif CallbackQuery.data == "GO TO PAGE 2":
         PAGE2_TEXT = "Translation.ABOUT"
         PAGE2_BUTTON = [
    [
        InlineKeyboardButton('BACK TO PAGE 1', callback_data="START READING"),
        InlineKeyboardButton('😁 Help', callback_data="help")
    ]
]


