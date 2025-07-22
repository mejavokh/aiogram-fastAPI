from aiogram import Router, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, FSInputFile
from pathlib import Path

from app import keyboards, states
import api_client

router = Router()
BASE_DIR = Path(__file__).resolve().parent.parent.parent
IMAGES_DIR = BASE_DIR / "images"

@router.message(CommandStart())
async def start(message: Message):
    await message.answer(f"Добро пожаловать! Выберите один из пунктов",
                        reply_markup=keyboards.main_menu_kb())

@router.message(F.text == "Книги")
async def show_books(message: Message):
    books = api_client.get_all_books()
    
    if not books:
        await message.answer("Нет доступных книг")
    else:
        for book in books:
            image_path = IMAGES_DIR / book['image'].split("/")[-1]
            photo = FSInputFile(image_path)
            caption = f"<b>{book['title']}</b>\n{book['summary']}"
            
            await message.answer_photo(photo, caption, parse_mode="HTML")

@router.message(F.text == "Писатели")
async def show_authors(message: Message):
    authors = api_client.get_all_authors()
    
    if not authors:
        await message.answer("Нет доступных писателей")
    else:
        for author in authors:
            image_path = IMAGES_DIR / author['image'].split("/")[-1]
            
            caption = f"{author['name']}"
            
            if image_path.exists():
                photo = FSInputFile(image_path)
                await message.answer_photo(photo, caption)
            else:
                await message.answer(caption)