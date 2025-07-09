from dotenv import load_dotenv
import os

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")

if not BOT_TOKEN:
    print("❌ Botni tokeni topilmadi.")
    exit(1)

print("Bot tokeni:", BOT_TOKEN)
