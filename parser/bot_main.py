import asyncio

from aiogram import Bot, Dispatcher

from .bot.config.config import load_config, Config


async def main():
    # загружаем данные конфигурации
    config: Config = load_config()

    # создание объектов бота и диспетчера
    bot: Bot = Bot(token=config.tg_bot.token, parse_mode='HTML')
    dp: Dispatcher = Dispatcher()

    # запуск обращения к телеграм бот api
    await dp.start_polling(bot, polling_timeout=30)


if __name__ == '__main__':
    asyncio.run(main())
