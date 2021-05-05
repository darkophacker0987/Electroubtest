from userbot import *
from userbot.utils import *
from userbot.Config import Config
from userbot.helpers.functions import *
from userbot.cmdhelp import CmdHelp



# =================== CONSTANT ===================

USERID = bot.uid if Config.OWNER_ID == 0 else Config.OWNER_ID
ALIVE_NAME = Config.ALIVE_NAME
AUTONAME = Config.AUTONAME
DEFAULT_BIO = Config.DEFAULT_BIO
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "cat"
BOT_USERNAME = Config.TG_BOT_USERNAME
# mention user
mention = f"[{DEFAULTUSER}](tg://user?id={USERID})"
hmention = f"<a href = tg://user?id={USERID}>{DEFAULTUSER}</a>"