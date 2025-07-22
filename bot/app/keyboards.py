from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

def main_menu_kb():
    markup = ReplyKeyboardMarkup(keyboard=[
        [
            KeyboardButton(text="Книги")
        ],
        [
            KeyboardButton(text="Писатели")
        ]
    ], resize_keyboard=True)
    
    return markup