from aiogram.types import ReplyKeyboardMarkup
from aiogram.utils.keyboard import ReplyKeyboardBuilder

def make_choice_kb() -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardBuilder()
    kb.button(text="Привітатись з ботом")
    kb.button(text="Перевірити наявність єлектрики в ЛБЦ")
    kb.button(text="Отримати статистику за день")
    kb.adjust(1)
    return kb.as_markup(resize_keyboard=True)