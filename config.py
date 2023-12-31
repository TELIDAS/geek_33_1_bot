from decouple import config
from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage

PROXY_URL = "http://proxy.server:3128"
storage = MemoryStorage()
TOKEN = config("TOKEN")
bot = Bot(token=TOKEN, proxy=PROXY_URL)
dp = Dispatcher(bot=bot, storage=storage)
ADMIN_ID = 1150258083
BOT_PIC = '/Users/adiletsaparbek/PycharmProjects/geek_33_1_bot/media/bot_pic.jpeg'
ANIMATION_PIC = '/Users/adiletsaparbek/PycharmProjects/geek_33_1_bot/media/joinblink-blink.gif'
GROUP_ID = -4021056833
DESTINATION_DIR = "/Users/adiletsaparbek/PycharmProjects/geek_33_1_bot/media"
