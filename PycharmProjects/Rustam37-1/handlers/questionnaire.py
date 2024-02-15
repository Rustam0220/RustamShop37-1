from aiogram import types, Dispatcher
from config import bot
from database import db
from keyboards import inline_buttons


async def tg_questionnaire(call: types.CallbackQuery):
    await bot.send_message(
        chat_id=call.from_user.id,
        text="Python 🐍 or Mojo 🔥 ?",
        reply_markup=await inline_buttons.questionnaire_first_answers()
    )


async def python_answers(call: types.CallbackQuery):
    await bot.send_message(
        chat_id=call.from_user.id,
        text="Cool u r awesome python developer",
    )


async def mojo_answers(call: types.CallbackQuery):
    await bot.send_message(
        chat_id=call.from_user.id,
        text="Dont lie, Mojo is in alpha version.",
    )

async def football_answers(call: types.CallbackQuery):
    await bot.send_message(
        chat_id=call.from_user.id,
        text="Cool, it is my favourite sport.",
    )


async def basketball_answers(call: types.CallbackQuery):
    await bot.send_message(
        chat_id=call.from_user.id,
        text="Ok, nice.",
    )


async def iphone_answers(call: types.CallbackQuery):
    await bot.send_message(
        chat_id=call.from_user.id,
        text="Cool, good choice.",
    )


async def samsung_answers(call: types.CallbackQuery):
    await bot.send_message(
        chat_id=call.from_user.id,
        text="Good choice, get another Xiaomi.",
    )

def register_questionnaire_handlers(dp: Dispatcher):
    dp.register_callback_query_handler(justice_questionnaire,
                                       lambda call: call.data == "start_questionnaire")
    dp.register_callback_query_handler(python_answers,
                                       lambda call: call.data == "python2")
    dp.register_callback_query_handler(mojo_answers,
                                       lambda call: call.data == "mojo")
    dp.register_callback_query_handler(football_answers,
                                       lambda call: call.data == "football")
    dp.register_callback_query_handler(basketball_answers,
                                       lambda call: call.data == "basketball")
    dp.register_callback_query_handler(iphone_answers,
                                       lambda call: call.data == "iphone")
    dp.register_callback_query_handler(samsung_answers,
                                       lambda call: call.data == "samsung")