from aiogram.types import (
    InLineKeyboardMarkup,
    InlineKeyboardButton
)


async def start_keyboard():
    markup = InlineKeyboardMarkup()
    questionnaire_button = InlineKeyboardButton(
        "Questionnaire 🔥",
        callback_data="start_questionnaire"
    )
    markup.add(questionnaire_button)
    return markup



async def questionnaire_first_answers():
    markup = InlineKeyboardMarkup()
    python_button = InlineKeyboardButton(
        "Python 🐍",
        callback_data="python2"
    )
    mojo_button = InlineKeyboardButton(
        "Mojo 🔥",
        callback_data="mojo"
    )



    markup.add(python_button)
    markup.add(mojo_button)
    return markup


async def football_button():
        return InlineKeyboardButton(
            "Football ⚽️",
            callback_data="football"
        )

    async def basketball_answers():
        return InlineKeyboardButton(
            "Basketball 🏀",
            callback_data="basketball"
        )

    async def iphone_button():
        return InlineKeyboardButton(
            "iPhone 📱",
            callback_data="iphone"
        )

    async def samsung_button():
        return InlineKeyboardButton(
            "Samsung 📱",
            callback_data="samsung"
        )



async def questionnaire_second_answers():
    markup = InlineKeyboardMarkup()
    football_button = await football_button()
    basketball_button = await basketball_button()
    markup.add(football_button)
    markup.add(basketball_button)
    return markup


async def questionnaire_third_answers():
    markup = InlineKeyboardMarkup()
    iphone_button = await iphone_button()
    samsung_button = await samsung_button()
    markup.add(iphone_button)
    markup.add(samsung_button)
    return markup