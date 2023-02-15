from pyrogram import filters

def ns_filter(_,__,message):
   if str(message.text)[1:6] == "start":
     if str(message.text)[7:] == "varisu":
       return True
     else:
       return False
   else:
      return False

varisu_filter = filters.create(ns_filter)
