from aiogram.types import (InlineKeyboardMarkup, InlineKeyboardButton)

main = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Начать', callback_data='begin')],
    [InlineKeyboardButton(text='Помощь', callback_data='help')]
    ])
 
settings = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='YouTube', url='https://www.youtube.com/watch?v=dQw4w9WgXcQ')]
    ])