import handlers
from util.misc import logging
from aiogram import executor
from loader import dp


async def on_startup(dispatcher):
    pass

if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup)
