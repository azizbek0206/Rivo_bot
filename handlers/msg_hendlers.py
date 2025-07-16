from aiogram import Router
from aiogram.types import Message
from aiogram.filters import CommandStart

msg_router = Router()

@msg_router.message()
async def msg_start(message: Message):
    text = f"Siz yozgan xabar --> {message.text}"
    await message.answer(text)

from aiogram.exceptions import TelegramForbiddenError

@dp.message(CommandStart())
async def msg_start(message: Message):
    try:
        await message.answer("Salom!")
    except TelegramForbiddenError:
        print(f"Foydalanuvchi botni bloklagan: {message.from_user.id}")
