from pyrogram import filters

def ns_filter(_,__,message):
   if str(message.text)[:4] == "start":
      return True
   else:
      return False

not_start_filter = filters.create(ns_filter)
