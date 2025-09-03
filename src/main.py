import asyncio
from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from src.config import settings
from src.handlers import start as start_handler
from src.handlers import links as links_handler
from src.handlers import callbacks as callbacks_handler

async def main() -> None:
    bot = Bot(settings.bot_token, parse_mode=ParseMode.HTML)
    dp = Dispatcher()
    dp.include_router(start_handler.router)
    dp.include_router(links_handler.router)
    dp.include_router(callbacks_handler.router)
    await dp.start_polling(bot)

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        pass
