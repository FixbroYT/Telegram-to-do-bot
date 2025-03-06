from app.database.models import db_main
from app.handlers import router
from config import BOT_TOKEN
from aiogram import Dispatcher, Bot
import asyncio


dp = Dispatcher()
bot = Bot(BOT_TOKEN)

async def main():
    print("Bot started!")
    dp.include_router(router)
    await db_main()
    await dp.start_polling(bot)

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Exit.")