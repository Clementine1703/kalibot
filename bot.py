from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
# from aiogram.utils import executor
from aiogram.utils.executor import start_webhook

from config import token

bot = Bot(token=token)
dp = Dispatcher(bot)

WEBHOOK_HOST = f'https://vk.com'
WEBHOOK_PATH = f'/webhook/{token}'
WEBHOOK_URL = f'{WEBHOOK_HOST}{WEBHOOK_PATH}'

WEBAPP_HOST = '0.0.0.0'
WEBAPP_PORT = 8000

async def on_startup(dispatcher):
    await bot.set_webhook(WEBHOOK_URL, drop_pending_updates=True)

async def on_shutdown(dispatcher):
    await bot.delete_webhook()


@dp.message_handler(content_types=['text'])
async def main(message: types.Message):
    if message.text == 'пососи':
        await bot.send_message(message.from_user.id, 'У, у, у, у, у, да я - богатый уебок. АА!')
    else:
        await bot.send_message(message.from_user.id, "don't understood")

if __name__ == '__main__':
    start_webhook(
        dispatcher=dp,
        webhook_path=WEBHOOK_PATH,
        skip_updates=True,
        on_startup=on_startup,
        on_shutdown=on_shutdown,
        host=WEBAPP_HOST,
        port=WEBAPP_PORT,
    )


