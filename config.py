import os
import logging
from os import getenv
from os import environ

class Config(object):
      API_HASH = getenv("API_HASH", "5264bf4663e9159565603522f58d3c18")
      API_ID = int(getenv("API_ID", 11973721))
      BOT_TOKEN = getenv("BOT_TOKEN", "5949999646:AAGNAzsUTMutsqtnSk2R4MkGgCQ0uMtqbIU")
DB_URL = environ.get('DATABASE_URI', "mongodb+srv://umeshnamo:8907711426@cluster0.mbtdc.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
DB_NAME = environ.get('DATABASE_NAME', "Cluster0")
ADMINS = int(os.environ.get("ADMINS", "1391556668"))
LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1001342411240"))
AUTH_USERS = set(int(x) for x in os.environ.get("AUTH_USERS", "1391556668").split())
BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", True))
FILE_STORE_CHANNEL = [int(ch) for ch in (environ.get('FILE_STORE_CHANNEL', '-1001819496419')).split()]
