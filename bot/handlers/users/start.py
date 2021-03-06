from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from bot.loader import dp
from bot.data.config import ADMINS


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer(
        f"Привет, {message.from_user.full_name}!\n" f"Твой id: {message.from_user.id}"
    )
