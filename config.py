import os
import logging
from os import getenv

class Config(object):
      API_HASH = getenv("API_HASH", "5264bf4663e9159565603522f58d3c18")
      API_ID = int(getenv("API_ID", 11973721))
      AS_COPY = True if getenv("AS_COPY", True) == "True" else False
      BOT_TOKEN = getenv("BOT_TOKEN", "5949999646:AAGNAzsUTMutsqtnSk2R4MkGgCQ0uMtqbIU")
      CHANNEL = list(x for x in getenv("CHANNEL_ID", "-1001861300920:-1001811940117 -1001786688631 -1001436081117 -1001780758150 -1001721348234 -1001780697340 -1001698854544 -1001593574364 -1001519485548").replace("\n", " ").split(' '))
      DB_URI = os.environ.get("DATABASE_URL", "mongodb+srv://KarthikMovies:KarthikUK007@cluster0.4l5byki.mongodb.net/?retryWrites=true&w=majority")
      DB_NAME = os.environ.get("DATABASE_NAME", "Cluster0")
