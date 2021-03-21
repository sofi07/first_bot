from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

start_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Пройти регистрацию', callback_data='1-1'),
            InlineKeyboardButton(text='Начать играть', callback_data='1-2')
        ]
    ]
)

admin_start = InlineKeyboardMarkup(
    [
        InlineKeyboardButton(text='Рассылка', callback_data='2-1'),
        InlineKeyboardButton(text='Cколько подписчиков?', callback_data='2-2')
    ]
)
