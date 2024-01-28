import re
import os
from os import getenv, environ
from Script import script 
from dotenv import load_dotenv

load_dotenv()


id_pattern = re.compile(r'^.\d+$')
def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default

API_ID = int(environ.get("API_ID", "29661201"))
API_HASH = environ.get("API_HASH", "ce10f942d9acb7aef82cc1af2f72e914")
ADMINS = int(environ.get("ADMINS", "6655844826"))
CLONE_DB_URI = environ.get("CLONE_DB_URI", "mongodb+srv://haroonhassan5:haroonhassan5@haroonhassan5.3h2pmhk.mongodb.net/?retryWrites=true&w=majority")
CDB_NAME = environ.get("CDB_NAME", "haroonhassan5")
DB_URI = environ.get("DB_URI", "mongodb+srv://haroonhassan5:haroonhassan5@haroonhassan5.3h2pmhk.mongodb.net/?retryWrites=true&w=majority")
DB_NAME = environ.get("DB_NAME", "haroonhassan5")
BOT_TOKEN = environ.get("BOT_TOKEN", "6492431239:AAENl-kRCeN5kwn-6KnAHcQXQXBJDbLvDuU")
BOT_USERNAME = environ.get("BOT_USERNAME", "THE_AI_FILE_STORE_BOT") # your bot username without @
PICS = (environ.get('PICS', 'https://telegra.ph/AI-11-01-4')).split() # Bot Start Picture
AUTO_DELETE = int(environ.get("AUTO_DELETE", "5")) # Time in Minutes
AUTO_DELETE_TIME = int(environ.get("AUTO_DELETE_TIME", "300")) # Time in Seconds
LOG_CHANNEL = int(environ.get("LOG_CHANNEL", "-1002109034059"))
FILE_STORE_CHANNEL = [int(ch) for ch in (environ.get('FILE_STORE_CHANNEL', '-1002109034059')).split()]
CUSTOM_FILE_CAPTION = environ.get("CUSTOM_FILE_CAPTION", f"{script.CAPTION}")
BATCH_FILE_CAPTION = environ.get("BATCH_FILE_CAPTION", CUSTOM_FILE_CAPTION)
PROTECT_CONTENT = is_enabled((environ.get('PROTECT_CONTENT', "False")), False)
PUBLIC_FILE_STORE = is_enabled((environ.get('PUBLIC_FILE_STORE', "True")), True)

class Var(object):
    MULTI_CLIENT = False
    name = str(getenv('name', 'filestorewithlink'))
    SLEEP_THRESHOLD = int(getenv('SLEEP_THRESHOLD', '60'))
    WORKERS = int(getenv('WORKERS', '4'))
    BIN_CHANNEL = int(getenv('BIN_CHANNEL', '-1002132568550'))
    PORT = int(getenv('PORT', 8080))
    BIND_ADRESS = str(getenv('WEB_SERVER_BIND_ADDRESS', '0.0.0.0'))
    PING_INTERVAL = int(environ.get("PING_INTERVAL", "1800"))  # 30 minutes
    NO_PORT = bool(getenv('NO_PORT', False))
    APP_NAME = None
    if 'DYNO' in environ:
        ON_HEROKU = True
        APP_NAME = str(getenv('APP_NAME'))
    
    else:
        ON_HEROKU = False
    FQDN = str(getenv('FQDN', BIND_ADRESS)) if not ON_HEROKU or getenv('FQDN') else APP_NAME+'.koyeb.com'
    HAS_SSL=bool(getenv('HAS_SSL',False))
    if HAS_SSL:
        URL = "https://extreme-bel-hfjeiowkekdkkfk.koyeb.app"
    else:
        URL = "https://extreme-bel-hfjeiowkekdkkfk.koyeb.app"
