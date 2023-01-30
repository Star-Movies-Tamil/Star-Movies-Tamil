import os
import logging
from os import getenv

class Config(object):
      API_HASH = getenv("API_HASH", "5264bf4663e9159565603522f58d3c18")
      API_ID = int(getenv("API_ID", 11973721))
      BOT_TOKEN = getenv("BOT_TOKEN", "5949999646:AAGNAzsUTMutsqtnSk2R4MkGgCQ0uMtqbIU")
DB_URI = os.environ.get("DATABASE_URL", "postgres://udpqqmbqqrkpdq:5e05cd23ce9587cb94844272c62111f2e3fc21d748ae3763abbf24de4ede6693@ec2-35-169-184-61.compute-1.amazonaws.com:5432/d37uqkso189vgg")
DB_NAME = os.environ.get("DATABASE_NAME", "Cluster0")
ADMINS = int(os.environ.get("ADMINS", "1391556668"))
FORCE_SUB_CHANNEL = int(os.environ.get("FORCE_SUB_CHANNEL", "-1001589399161"))
