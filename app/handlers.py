from aiogram import F, Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, CallbackQuery

import app.keyboards as kb

router = Router()


@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.reply(f'Доброго времени суток, {message.from_user.first_name}, я бот по оценке строительных подрядчиков, отправьте мне договор текстом или файлом!\n\nЕсли вам нужна инструкция выберите Помошь',
                         reply_markup=kb.main)

@router.callback_query(F.data == 'begin')
async def beginned(callback: CallbackQuery):
    await callback.answer("Вы выбрали <Начать>")
    await callback.message.edit_text('Пришлите мне текст или файл с информацией о подрядчике',
                         reply_markup=kb.main)
                         
@router.callback_query(F.data == 'help')
async def help(callback: CallbackQuery):
    await callback.answer("Вы выбрали <Помощь>")
    await callback.message.edit_text('Вам крч просто надо что-то написать, файлик бот пока не умеет обрабатывать так что терпим \n\nЕсли ваши вопросы остались не закрытыми - можете задать их тех. поддержке: \n2200 7009 5288 4079 Т-Банк',
                                     reply_markup=kb.main)
