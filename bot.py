import logging
import wikipedia

from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = '5852042604:AAFPbgwc5ZjXIV2EX9_ewBxJEYQQ1ijVIXk'

wikipedia.set_lang('uz')

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/start` or `/help` command
    """
    await message.reply(f"Salom {message.from_user.full_name } Wikipedia botimizga xush kelibsiz! \n\nBo'tdan to'liq foydalanish uchun quyidagi kanalimizga obuna bo'ling! \n\n👉@Olislardagi_Baxtim")


@dp.message_handler()
async def sendwiki(message: types.Message):
    try:
        respond = wikipedia.summary(message.text)
        await message.answer(respond)
    except:
            await message.reply("Uzur bu mavzuga oid maqola topilmadi")


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)