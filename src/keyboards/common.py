from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def subscribe_keyboard(channel_username: str) -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Kanalga o'tish", url=f"https://t.me/{channel_username.lstrip('@')}")],
        [InlineKeyboardButton(text="Tekshirish", callback_data="check_subscription")],
    ])

options_kb = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="🎥 Videoni yuklash", callback_data="opt_video")],
    [InlineKeyboardButton(text="🎶 To'liq musiqani yuklash", callback_data="opt_music")],
    [InlineKeyboardButton(text="🎧 Audioni ajratish", callback_data="opt_audio")],
])

qualities_kb = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text=q, callback_data=f"q_{q}") for q in ["144p", "360p", "720p", "1080p", "4K"]]
])
