# import asyncio
from aiogram import Router, Bot
from aiogram.filters import CommandStart
from aiogram.types import Message

from bot.lexicon.ru import LEXICON
from bot.keyboards.keyboards import start_kb


router = Router()


# Приветствие и открытие начальной страницы /start
@router.message(CommandStart())
async def process_start_command(message: Message, bot: Bot):
    await bot.delete_message(chat_id=message.chat.id,
                             message_id=message.message_id)
    await message.answer(text=LEXICON['/start'],
                         reply_markup=start_kb)
    # await asyncio.sleep(5)
    # await bot.delete_message(chat_id=message.chat.id,
    #                          message_id=message.message_id + 1)
