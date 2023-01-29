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


# Callback Quary

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
    elif CallbackQuery.data == "home":
         START = "Translation.START"
         START_BUTTON = [
    [
        InlineKeyboardButton('😎 About', callback_data="about"),
        InlineKeyboardButton('😁 Help', callback_data="help")
    ]
]
CallbackQuery.edit_message_text(
            START,
            reply_markup = InlineKeyboardMarkup(START_BUTTON)
        )
    elif CallbackQuery.data == "about":
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
    elif CallbackQuery.data == "start":
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
