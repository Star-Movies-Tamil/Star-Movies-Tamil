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

################################################################################################################################################################################################################################################
# Hollywood Movies

def ns_filter(_,__,message):
   if str(message.text)[1:6] == "start":
     if str(message.text)[7:].lower() == "hollywood_movies":
       return True
     else:
       return False
   else:
      return False

hollywood_movies_filter = filters.create(ns_filter)

################################################################################################################################################################################################################################################
# Web Series

def ns_filter(_,__,message):
   if str(message.text)[1:6] == "start":
     if str(message.text)[7:].lower() == "web_series":
       return True
     else:
       return False
   else:
      return False

web_series_filter = filters.create(ns_filter)

################################################################################################################################################################################################################################################
# Movie Collection

def ns_filter(_,__,message):
   if str(message.text)[1:6] == "start":
     if str(message.text)[7:].lower() == "movie_collection":
       return True
     else:
       return False
   else:
      return False

movie_collection_filter = filters.create(ns_filter)

################################################################################################################################################################################################################################################
# Cartoon Movies

def ns_filter(_,__,message):
   if str(message.text)[1:6] == "start":
     if str(message.text)[7:].lower() == "cartoon_movies":
       return True
     else:
       return False
   else:
      return False

cartoon_movies_filter = filters.create(ns_filter)

################################################################################################################################################################################################################################################
# TV Shows

def ns_filter(_,__,message):
   if str(message.text)[1:6] == "start":
     if str(message.text)[7:].lower() == "tv_shows":
       return True
     else:
       return False
   else:
      return False

tv_shows_filter = filters.create(ns_filter)

################################################################################################################################################################################################################################################
