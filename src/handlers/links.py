from aiogram import Router
from aiogram.types import Message
from src.config import settings
from src.keyboards.common import subscribe_keyboard
import re

router = Router()

LINK_RE = re.compile(r"https?://(www\.)?(instagram\.com|youtu\.be|youtube\.com)/[\w\-\?=&#%/\.]+", re.I)

@router.message()
async def handle_links(message: Message):
    if not message.text:
        return
    match = LINK_RE.search(message.text)
    if not match:
        return
    await message.answer(
        "Davom etishdan oldin bizning kanalimizga obuna bo‘ling 📢\n"
        f"{settings.channel_username}\n\n"
        "✅ Obuna bo‘lgach, \"Tekshirish\" tugmasini bosing",
        reply_markup=subscribe_keyboard(settings.channel_username),
    )
