from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menu = ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
menu2 = ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)

stone_btn = KeyboardButton(text='камень')
paper_btn = KeyboardButton(text='бумага')
scissors_btn = KeyboardButton(text='ножницы')
contact_btn = KeyboardButton(text='контакты', request_contact=True)

menu.insert(stone_btn)
menu.insert(paper_btn)
menu.insert(scissors_btn)
menu2.insert(contact_btn)
