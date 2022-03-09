from aiogram import executor
from loader import dp


async def on_startup(dispatcher):
    print('Bot has been launched')

if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup)
