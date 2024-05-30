from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message, ReplyKeyboardRemove
from keyboards.for_questions import make_choice_kb

router = Router()  # [1]

@router.message(Command("start"))  # [2]
async def cmd_start(message: Message):
    await message.answer(
        f"Привіт, {message.from_user.full_name} !",
        reply_markup=make_choice_kb()
    )

@router.message(F.text.lower() == "перевірити наявність єлектрики в лбц")
async def answer_check_electrisity(message: Message):
    await message.answer(
        "Перевірка",
        reply_markup=make_choice_kb()
    )

@router.message(F.text.lower() == "отримати статистику за тиждень")
async def answer_get_statistic(message: Message):
    await message.answer(
        "Тут має бути листінг",
        reply_markup=ReplyKeyboardRemove()
    )