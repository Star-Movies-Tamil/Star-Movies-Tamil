import os
import logging
from os import getenv
from os import environ

class Config(object):
      API_HASH = getenv("API_HASH", "5264bf4663e9159565603522f58d3c18")
      API_ID = int(getenv("API_ID", 11973721))
      BOT_TOKEN = getenv("BOT_TOKEN", "5949999646:AAGNAzsUTMutsqtnSk2R4MkGgCQ0uMtqbIU")
DB_URI = environ.get('DATABASE_URI', "mongodb+srv://umeshnamo:8907711426@cluster0.mbtdc.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
DB_NAME = environ.get('DATABASE_NAME', "Cluster0")
ADMINS = int(os.environ.get("ADMINS", "1391556668"))
