from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import CommandStart
from src.config import settings
from src.keyboards.common import subscribe_keyboard

router = Router()

@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer(
        "Assalomu alaykum 👋\n"
        "Men sizga Instagram va YouTube havolalari orqali videolarni yuklab beraman.\n"
        "Shuningdek:\n"
        "🎥 Videoni yuklab olishingiz mumkin\n"
        "🎶 To‘liq musiqasini yuklab olishingiz mumkin\n"
        "🎧 Videodagi audioni ajratib olishingiz mumkin\n\n"
        "Menga havola yuboring ⬇️",
    )
