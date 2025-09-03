from aiogram import Router, F
from aiogram.types import CallbackQuery
from aiogram.exceptions import TelegramBadRequest
from src.keyboards.common import options_kb

router = Router()

@router.callback_query(F.data == "check_subscription")
async def on_check_subscription(callback: CallbackQuery):
    # Placeholder: real check implemented later
    try:
        await callback.message.edit_text(
            "Kontentni yuklab olish opsiyalari:", reply_markup=options_kb
        )
    except TelegramBadRequest:
        await callback.answer()
