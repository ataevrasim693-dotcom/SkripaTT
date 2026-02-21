import requests
from aiogram import Bot, Dispatcher, types
from aiogram.types import Message
from aiogram.utils import executor

# Using the token provided by the user
import os
TOKEN = os.getenv("BOT_TOKEN")

if not TOKEN:
    raise ValueError("BOT_TOKEN не найден!")

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

def download_tiktok(url):
    api_url = f"https://www.tikwm.com/api/?url={url}"
    try:
        response = requests.get(api_url).json()
        if response.get("data"):
            return response["data"]["play"]
    except Exception:
        pass
    return None

@dp.message_handler()
async def get_video(message: Message):
    url = message.text
    if "tiktok.com" in url:
        await message.answer("Скачиваю видео...")
        video_url = download_tiktok(url)
        if video_url:
            await message.answer_video(video_url)
        else:
            await message.answer("Не удалось скачать видео. Проверьте ссылку.")
    else:
        await message.answer("Отправь ссылку на TikTok видео")

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
