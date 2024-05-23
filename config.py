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

API_ID = int(environ.get("API_ID", "25443947"))
API_HASH = environ.get("API_HASH", "ab4cd800dac7c9a36314ee83800adba8")
ADMINS = int(environ.get("ADMINS", "6013614984"))
CLONE_DB_URI = environ.get("CLONE_DB_URI", "mongodb+srv://haroonhassan3:haroonhassan3@haroonhassan3.7zzzhoe.mongodb.net/?retryWrites=true&w=majority")
CDB_NAME = environ.get("CDB_NAME", "haroonhassan3")
DB_URI = environ.get("DB_URI", "mongodb+srv://haroonhassan3:haroonhassan3@haroonhassan3.7zzzhoe.mongodb.net/?retryWrites=true&w=majority")
DB_NAME = environ.get("DB_NAME", "haroonhassan3")
BOT_TOKEN = environ.get("BOT_TOKEN", "6836440187:AAG-5yidFRNKRNz9eekr8PJeXhMMHMBQRDQ")
BOT_USERNAME = environ.get("BOT_USERNAME", "Ai_file_store_bot") # your bot username without @
PICS = (environ.get('PICS', 'https://telegra.ph/AI-11-01-4')).split() # Bot Start Picture
AUTO_DELETE = int(environ.get("AUTO_DELETE", "5")) # Time in Minutes
AUTO_DELETE_TIME = int(environ.get("AUTO_DELETE_TIME", "300")) # Time in Seconds
LOG_CHANNEL = int(environ.get("LOG_CHANNEL", "-1001957898674"))
FILE_STORE_CHANNEL = [int(ch) for ch in (environ.get('FILE_STORE_CHANNEL', '-1001957898674')).split()]
CUSTOM_FILE_CAPTION = environ.get("CUSTOM_FILE_CAPTION", f"{script.CAPTION}")
BATCH_FILE_CAPTION = environ.get("BATCH_FILE_CAPTION", CUSTOM_FILE_CAPTION)
PROTECT_CONTENT = is_enabled((environ.get('PROTECT_CONTENT', "False")), False)
PUBLIC_FILE_STORE = is_enabled((environ.get('PUBLIC_FILE_STORE', "True")), True)

class Var(object):
    MULTI_CLIENT = False
    name = str(getenv('name', 'filestorewithlink'))
    SLEEP_THRESHOLD = int(getenv('SLEEP_THRESHOLD', '60'))
    WORKERS = int(getenv('WORKERS', '4'))
    BIN_CHANNEL = int(getenv('BIN_CHANNEL', '-1001957898674'))
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
    FQDN = str(getenv('FQDN', BIND_ADRESS)) if not ON_HEROKU or getenv('FQDN') else APP_NAME+'.herokuapp.com'
    HAS_SSL=bool(getenv('HAS_SSL',False))
    if HAS_SSL:
        URL = "https://ai-file-streaming-e06e5ca94209.herokuapp.com/"
    else:
        URL = "https://ai-file-streaming-e06e5ca94209.herokuapp.com/"
