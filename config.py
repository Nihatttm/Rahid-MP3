import os
from os import getenv
from dotenv import load_dotenv

load_dotenv()
admins = {}
SESSION_NAME = getenv("SESSION_NAME", "session")
BOT_TOKEN = getenv("BOT_TOKEN")
BOT_NAME = getenv("BOT_NAME")
API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")
MONGODB_URL = getenv("MONGODB_URL")
OWNER_NAME = getenv("OWNER_NAME")
ALIVE_NAME = getenv("ALIVE_NAME")
BOT_USERNAME = getenv("BOT_USERNAME")
ASSISTANT_NAME = getenv("ASSISTANT_NAME")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "sohbeti_muhabbet")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "graiflyrics")
SUDO_USERS = list(map(int, getenv("SUDO_USERS").split()))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
ALIVE_IMG = getenv("ALIVE_IMG", "https://telegra.ph//file/189fe27bff1207dd3eb85.jpg")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "100"))
UPSTREAM_REPO = getenv("UPSTREAM_REPO")
IMG_1 = getenv("IMG_1", "https://telegra.ph//file/928cdf4eb56c64b76cc67.jpg")
IMG_2 = getenv("IMG_2", "https://telegra.ph//file/193c6843e05cfbc35a66a.jpg")
IMG_3 = getenv("IMG_3", "https://telegra.ph//file/31308c6d73cc109c298aa.jpg")
IMG_4 = getenv("IMG_4", "https://telegra.ph//file/0b2dd8366589068b2c656.jpg")
IMG_5 = getenv("IMG_5", "https://telegra.ph//file/f9467f8dabec46f589816.jpg")
