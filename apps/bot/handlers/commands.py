from aiogram import Router, types, F
from aiogram.filters import Command, CommandStart

from app.keyboards.inline import inline

router = Router()


@router.message(CommandStart())
async def start_command(message: types.Message):
    await message.answer("Menu", reply_markup=inline())


@router.message(Command('help'))
async def help_command(message: types.Message):
    await message.answer("Available commands:\n/start - Start the bot\n/help - Get help")
