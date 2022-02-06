from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
import imp
import re
from data.config import CHANNELS
from aiogram.dispatcher.filters import Command, Text, CommandStart
from aiogram.dispatcher import FSMContext
from aiogram.types import Message, ReplyKeyboardRemove
from yarl import URL
from states.personalData import personalData
from aiogram.types import InputFile
from keyboards.default.mainKeyboard import menu, orqaga

from loader import dp, bot



@dp.message_handler(CommandStart())
async def show_channels(message: types.Message):
    channels_format = str()
    for channel in CHANNELS:
        # logging.info(invite_link)
        channels_format += f"👉 <a href='https://t.me/Academic_number_one'>Academic Number One</a>\n"

    await message.answer(f"Quyidagi kanalga obuna bo'ling: \n"
                         f"{channels_format}\n\n"
                         f"👋 Salom, {message.from_user.full_name}!\n Botimizga xush kelibsiz.\n Bu tugmalardan birin tanlang. 👇", reply_markup=menu                         
                         )

    

@dp.message_handler(text = "Ishdan bo`shash")
async def kurs_answer(message: Message):
    photo_file = "BQACAgIAAxkBAAIDHmH_V_QaRdkuTnumfgNsK7-emqUbAAL4EwAC1voBSA_E3MTqWaQNIwQ"
    await message.answer_document(photo_file, caption="Ishdan_bo`shash_arizasi", reply_markup=orqaga)


@dp.message_handler(text = "🧑‍🏫 O`qituvchilar uchun 🧑‍🏫")
async def kurs_answer(message: Message):
    photo_file = "BQACAgIAAxkBAAIDIGH_WBgvpViqUQxa2MUb5xlhTtx7AAL5EwAC1voBSMD9DObP4Ol6IwQ"
    await message.answer_document(photo_file, caption="O`qituvchilar_shartnomasi", reply_markup=orqaga)


@dp.message_handler(text = "🧒 Bolalar uchun 👧")
async def kurs_answer(message: Message):
    photo_file = "BQACAgIAAxkBAAIDImH_WCDRPqkqDirAZ7jbWUA6FaScAAL6EwAC1voBSHZYdXR-d8OPIwQ"
    await message.answer_document(photo_file, caption="Bolalar_uchun_narxlar", reply_markup=orqaga)


@dp.message_handler(text = "👨‍👨‍👧 Ota-onalar uchun 👨‍👩‍👦‍👦")
async def kurs_answer(message: Message):
    photo_file = "BQACAgIAAxkBAAIDJGH_WCmy4diXhjgliKs8dAt0RtRlAAL7EwAC1voBSCRYh3M8pLYmIwQ"
    await message.answer_document(photo_file, caption="Ota-onalar_uchun", reply_markup=orqaga)


@dp.message_handler(text = "🔙 Orqaga 🔙")
async def kurs_answer(message: Message):
    await message.answer(f"Bu tugmalardan birin tanlang. 👇", reply_markup=menu)
    

