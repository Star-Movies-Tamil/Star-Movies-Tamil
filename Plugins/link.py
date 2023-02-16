from pyrogram import filters

################################################################################################################################################################################################################################################
# Varisu (2023)

def ns_filter(_,__,message):
   if str(message.text)[1:6] == "start":
     if str(message.text)[7:].lower() == "varisu":
       return True
     else:
       return False
   else:
      return False

varisu_filter = filters.create(ns_filter)

################################################################################################################################################################################################################################################
# Thunivu (2023)

def ns_filter(_,__,message):
   if str(message.text)[1:6] == "start":
     if str(message.text)[7:].lower() == "thunivu":
       return True
     else:
       return False
   else:
      return False

thunivu_filter = filters.create(ns_filter)

# Thunivu (2023) Page 2
def ns_filter(_,__,message):
   if str(message.text)[1:6] == "start":
     if str(message.text)[7:].lower() == "thunivu_page2":
       return True
     else:
       return False
   else:
      return False

thunivu_page2_filter = filters.create(ns_filter)

################################################################################################################################################################################################################################################
# Alien Covenant (2017)

def ns_filter(_,__,message):
   if str(message.text)[1:6] == "start":
     if str(message.text)[7:].lower() == "alien_covenant":
       return True
     else:
       return False
   else:
      return False

alien_covenant_filter = filters.create(ns_filter)

################################################################################################################################################################################################################################################

