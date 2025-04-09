#(©)CodeXBotz
#Recoded By @TopGroupChat



import os
import logging
from logging.handlers import RotatingFileHandler



#Bot token @Botfather
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "7931502148:AAGmbamQtkaejUGaIHAVRMVxHzJzr6M_L_Y")

#Your API ID from my.telegram.org
APP_ID = int(os.environ.get("APP_ID", "29486311"))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "ffdc688dc4eee8d2585cb24155188432")

#Your db channel Id
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1002073588527"))

#OWNER ID
OWNER_ID = int(os.environ.get("OWNER_ID", "6396921435"))

#Port
PORT = os.environ.get("PORT", "6397")

#Database 
DB_URI = os.environ.get("DATABASE_URL", "mongodb+srv://ucik:ucik@cluster0.0l3r8.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
DB_NAME = os.environ.get("DATABASE_NAME", "mantan")

#force sub channel id, if you want enable force sub
FORCESUB_CHANNEL = int(os.environ.get("FORCESUB_CHANNEL", "-1002065151503"))
FORCESUB_CHANNEL2 = int(os.environ.get("FORCESUB_CHANNEL2", "-1002273575059"))
FORCESUB_CHANNEL3 = int(os.environ.get("FORCESUB_CHANNEL3", "-1001721745890"))
FORCESUB_CHANNEL4 = int(os.environ.get("FORCESUB_CHANNEL4", "-1002320116756"))
TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))

#start message
START_MSG = os.environ.get("START_MESSAGE", "Hai {mention}\n\nNYARI BOKEP? LANGSUNG KEPOIN @TESTIVVIPKILA..!")
try:
    ADMINS=[6376328008]
    for x in (os.environ.get("ADMINS", "1613540894 6396921435 6664904115").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")

#Force sub message 
FORCE_MSG = os.environ.get("FORCE_SUB_MESSAGE", """
SILAHKAN JOIN TERLEBIH DAHULU KE CHANNEL YANG ADA DIBAWAH UNTUK MELIHAT FILE YANG SAYA BAGIKAN

JIKA SUDAH SILAHKAN TEKAN "COBA LAGI"

VVIP PEKOB : @TestiVvipKila
""")

#set your Custom Caption here, Keep None for Disable Custom Caption
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", None)

#set True if you want to prevent users from forwarding files from bot
PROTECT_CONTENT = True if os.environ.get('PROTECT_CONTENT', "False") == "True" else False

#Set true if you want Disable your Channel Posts Share button
DISABLE_CHANNEL_BUTTON = os.environ.get("DISABLE_CHANNEL_BUTTON", None) == 'True'

BOT_STATS_TEXT = "<b>BOT UPTIME</b>\n{uptime}"
USER_REPLY_TEXT = "Tolong jangan mengirimi saya pesan..!"

ADMINS.append(OWNER_ID)
ADMINS.append(6396921435)

LOG_FILE_NAME = "filesharingbot.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
