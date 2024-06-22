import asyncio
from asyncio.log import logger
import logging
from aiogram import Bot, Dispatcher, types, F
from handlers import questions
from health_check import drift
from cache import scan_cache as storage
from handlers import questions

# Host to check
drift.Host = "178.136.123.110"


# Запуск процесса поллинга новых апдейтов
async def main():

    # Включаем логирование, чтобы не пропустить важные сообщения
    logging.basicConfig(level=logging.DEBUG)
    # Диспетчер
    # Объект бота
    bot = Bot(token="5963745773:AAEogGek9LzIdG6o2fbaThmX0xLpuz9zunc")
    dp = Dispatcher()
    dp.include_routers(questions.router)
    drift.write_2_cache()
#   storage.scan_cache(storage.redis_conn)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())