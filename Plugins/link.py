from pyrogram import filters

################################################################################################################################################################################################################################################
# Varisu (2023)

def ns_filter(_,__,message):
   if str(message.text)[1:6] == "start":
     if str(message.text)[7:].lower() == "Varisu":
       return True
     else:
       return False
   else:
      return False

Varisu_filter = filters.create(ns_filter)

################################################################################################################################################################################################################################################
# Thunivu (2023)

def ns_filter(_,__,message):
   if str(message.text)[1:6] == "start":
     if str(message.text)[7:].lower() == "Thunivu":
       return True
     else:
       return False
   else:
      return False

Thunivu_filter = filters.create(ns_filter)

# Thunivu (2023) Page 2
def ns_filter(_,__,message):
   if str(message.text)[1:6] == "start":
     if str(message.text)[7:].lower() == "Thunivu_Page2":
       return True
     else:
       return False
   else:
      return False

Thunivu_Page2_filter = filters.create(ns_filter)

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

