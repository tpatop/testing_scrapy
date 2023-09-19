import asyncio
from aiogram import Router, Bot
from aiogram.types import Message

from bot.lexicon.ru import LEXICON


router = Router()


# Приветствие и открытие начальной страницы /start
@router.message()
async def process_start_command(message: Message, bot: Bot):
    await bot.delete_message(chat_id=message.chat.id,
                             message_id=message.message_id)
    await message.answer(text=LEXICON['bad_answer'])
    await asyncio.sleep(5)
    await bot.delete_message(chat_id=message.chat.id,
                             message_id=message.message_id + 1)
