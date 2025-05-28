from aiogram import Router
from aiogram.types import Message


msg_router = Router()

@msg_router.message()
async def msg_start(message: Message):
    text = f"Siz yozgan xabar --> {message.text}"
    await message.answer(text)