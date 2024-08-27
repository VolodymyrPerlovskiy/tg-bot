from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message, ReplyKeyboardRemove
from keyboards.for_questions import make_choice_kb
from health_check import drift
from data import statistic
from cache import scan_cache
from aiogram.enums import ParseMode
from aiogram.utils.formatting import (
    Bold, as_list, as_marked_section, as_key_value, HashTag
)
from aiogram import Bot
from health_check import drift

bot = Bot(token="5963745773:AAEogGek9LzIdG6o2fbaThmX0xLpuz9zunc")

router = Router()  # [1]

@router.message(Command("start"))  # [2]
async def cmd_start(message: Message):
    await message.answer(
        "Hello Human!",
        reply_markup=make_choice_kb()
    )

@router.message(F.text.lower() == "привітатись з ботом")  # [2]
async def cmd_start(message: Message):
    await message.answer(
        f"Привіт, {message.from_user.full_name} !",
        reply_markup=make_choice_kb()
        )

@router.message(F.text.lower() == "перевірити наявність єлектрики в лбц")
async def answer_check_electrisity(message: Message):
    current_datetime = tuple(drift.current_status())
    appropriate_mark = statistic..set_icons()
    await message.answer(
        f"{current_datetime[0]} {appropriate_mark}",       
        reply_markup=make_choice_kb()
    )

@router.message(F.text.lower() == "отримати статистику за день")
async def answer_get_statistic(message: Message):
    appropriate_mark = statistic.set_icons()
    dict = scan_cache.arrange_dict()

    for key, value in dict.items():
        await message.answer(
            f"{key} {appropriate_mark}",
        reply_markup=make_choice_kb()     
    )
