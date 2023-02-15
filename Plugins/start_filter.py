from pyrogram import filters

def s_filter(_,__,message):
   if message.text == "/start":
      return True
   else:
      return False

start_filter = filters.create(s_filter)
