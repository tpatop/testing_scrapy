import asyncio

from aiogram import Bot, Dispatcher

from bot.config.config import load_config, Config
from bot.handlers.user import router as R1
from bot.handlers.other import router as R2


async def main():
    # загружаем данные конфигурации
    config: Config = load_config()

    # создание объектов бота и диспетчера
    bot: Bot = Bot(token=config.tg_bot.token, parse_mode='HTML')
    dp: Dispatcher = Dispatcher()

    # регистрация роутеров
    dp.include_routers(R1, R2)

    print('Бот был запущен!')
    # запуск обращения к телеграм бот api
    await dp.start_polling(bot, polling_timeout=30)


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Бот был остановлен!')
