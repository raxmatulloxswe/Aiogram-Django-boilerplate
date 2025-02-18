from aiogram.utils.keyboard import InlineKeyboardBuilder


def inline():
    inline_keyboard = InlineKeyboardBuilder()

    inline_keyboard.button(text='Text')

    return inline_keyboard.as_markup()


def inline_subscribe():
    inline_keyboard = InlineKeyboardBuilder()

    inline_keyboard.button(text='Subscribe', url='https://t.me/+GRx6sKGZLn83YWEy')

    return inline_keyboard.as_markup()
