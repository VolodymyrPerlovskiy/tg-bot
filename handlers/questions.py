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
# from data import statistic

router = Router()  # [1]

@router.message(Command("start"))  # [2]
async def cmd_start(message: Message):
    await message.answer(
        f"Привіт, {message.from_user.full_name} !",
        reply_markup=make_choice_kb()
    )

@router.message(F.text.lower() == "перевірити наявність єлектрики в лбц")
async def answer_check_electrisity(message: Message):
    current_datetime = tuple(drift.current_status())
    appropriate_mark = statistic.set_marks()
    await message.answer(
        f"{current_datetime[0]} {appropriate_mark}",       
        reply_markup=make_choice_kb()
    )

@router.message(F.text.lower() == "отримати статистику за тиждень")
async def answer_get_statistic(message: Message):
    ls = scan_cache.arrange_dict(scan_cache.dict_cache)
    await message.answer(
        f"<b>{ls}</b>",
        parse_mode=ParseMode.HTML,
        reply_markup=make_choice_kb()       
    )

# @router.message(F.text.lower() == "отримати статистику за тиждень")
# async def answer_get_statistic(message: Message):
#    await message.answer(
#        "Тут має бути листінг",
#        reply_markup=ReplyKeyboardRemove()
#    )