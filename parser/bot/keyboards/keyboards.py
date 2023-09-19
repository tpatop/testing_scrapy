from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types import (
    InlineKeyboardButton
)

from bot.lexicon.ru import LEXICON_COMMAND


start_kb: InlineKeyboardBuilder = InlineKeyboardBuilder(
    [[
        InlineKeyboardButton(
            text=LEXICON_COMMAND[f'{cmd}'],
            callback_data=cmd) for cmd in LEXICON_COMMAND
    ]]
).adjust(1, repeat=True).as_markup()
