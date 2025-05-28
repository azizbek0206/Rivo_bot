from aiogram.types import Message
from aiogram import Router
from aiogram.filters import CommandStart

start_router = Router()

@start_router.message(CommandStart())
async def start(message: Message):
    username = message.from_user.username
    await message.answer(
        f"Assalomu alaykum {username} botimizga xush kelibsiz ! ✅ \n\n"
        f"Botimizga nima yozsangiz shuni qaytara oladi ! ✅ \n\n  "
        f"sinash uchun matn yozing "
    )