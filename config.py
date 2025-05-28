from dotenv import load_dotenv
import os

load_dotenv()

BOT_TOKEN = os.getenv("Bot_token")

if not BOT_TOKEN:
    print("Botni tokeni topilmadi.... ❎")                                                                           