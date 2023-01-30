import os
import logging
from os import getenv
from os import environ

class Config(object):
      API_HASH = getenv("API_HASH", "5264bf4663e9159565603522f58d3c18")
      API_ID = int(getenv("API_ID", 11973721))
      BOT_TOKEN = getenv("BOT_TOKEN", "5949999646:AAGNAzsUTMutsqtnSk2R4MkGgCQ0uMtqbIU")
DATABASE_URI = environ.get('DATABASE_URI', "mongodb+srv://umeshnamo:8907711426@cluster0.mbtdc.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
DATABASE_NAME = environ.get('DATABASE_NAME', "Cluster0")
ADMINS = int(os.environ.get("ADMINS", "1391556668"))
FORCE_SUB_CHANNEL = int(os.environ.get("FORCE_SUB_CHANNEL", "-1001589399161"))
FORCE_MSG = os.environ.get("FORCE_SUB_MESSAGE", "Hello 👋🏻 {mention}\n\n<b>You need to join in my Channel/Group to use me\n\nKindly Please join Channel</b>")
