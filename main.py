from aiogram import Bot,Dispatcher
import asyncio
import logging
import sys

from config import BOT_TOKEN
from handlers.start_hendlers import start_router
from handlers.msg_hendlers import msg_router
# from app import app

# gunicorn main:app
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello!"


db = Dispatcher()


async def main():
    print("Botim ishga tushdi....")
    bot = Bot(token=BOT_TOKEN)
    db.include_router(start_router)
    db.include_router(msg_router)

    await db.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO,stream=sys.stdout)
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        logging.info("Bot tuxtadi.... ❌")




