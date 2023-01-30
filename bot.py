import logging
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(lineno)d - %(module)s - %(levelname)s - %(message)s'
)
logging.getLogger().setLevel(logging.INFO)
logging.getLogger("pyrogram").setLevel(logging.WARNING)

import uvloop
uvloop.install()
import sys
from config import Config, ADMINS
from pyrogram import Client 
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery

class channelforward(Client, Config):
    def __init__(self):
        super().__init__(
            name="CHANNELFORWARD",
            bot_token=self.BOT_TOKEN,
            api_id=self.API_ID,
            api_hash=self.API_HASH,
            workers=20,
            plugins={'root': 'Plugins'}
        )

    async def start(self):
        await super().start()
        me = await self.get_me()
        print(f"Bot Started for {me.first_name}")
        try:
            db_channel = await self.get_chat(CHANNEL_ID)
            self.db_channel = db_channel
            test = await self.send_message(chat_id = db_channel.id, text = "Test Message")
            await test.delete()

    async def stop(self):
        await super().stop()
        print("Bot Stopped. Bye!!")


if __name__ == "__main__" :
    channelforward().run()
