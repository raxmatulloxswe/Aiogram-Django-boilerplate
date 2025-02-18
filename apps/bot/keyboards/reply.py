from aiogram.utils.keyboard import ReplyKeyboardBuilder


def reply_():
    reply_keyboard = ReplyKeyboardBuilder()

    reply_keyboard.button(text="Reply Text")

    return reply_keyboard.as_markup()
