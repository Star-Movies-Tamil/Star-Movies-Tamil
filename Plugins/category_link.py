from pyrogram import filters

################################################################################################################################################################################################################################################
# Tamil Movies

def ns_filter(_,__,message):
   if str(message.text)[1:6] == "start":
     if str(message.text)[7:].lower() == "tamil_movies":
       return True
     else:
       return False
   else:
      return False

tamil_movies_filter = filters.create(ns_filter)
