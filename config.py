from decouple import config
from aiogram import Bot, Dispatcher

TOKEN = config("TOKEN")
bot = Bot(token=TOKEN)
dp = Dispatcher(bot=bot)
ADMIN_ID = 1150258083
BOT_PIC = '/Users/adiletsaparbek/PycharmProjects/geek_33_1_bot/media/bot_pic.jpeg'
ANIMATION_PIC = '/Users/adiletsaparbek/PycharmProjects/geek_33_1_bot/media/joinblink-blink.gif'
GROUP_ID = -4021056833