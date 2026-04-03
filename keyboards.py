from aiogram import types

# Inline Keyboard Example
inline_keyboard = [[
    types.InlineKeyboardButton(text='Button 1', callback_data='button1'),
    types.InlineKeyboardButton(text='Button 2', callback_data='button2')
], [
    types.InlineKeyboardButton(text='Button 3', callback_data='button3')
]]
inline_kb = types.InlineKeyboardMarkup(inline_keyboard)

# Reply Keyboard Example
reply_keyboard = [[
    types.KeyboardButton(text='Button A'),
    types.KeyboardButton(text='Button B')
], [
    types.KeyboardButton(text='Button C')
]]
reply_kb = types.ReplyKeyboardMarkup(reply_keyboard, resize_keyboard=True)

# Example function to send a message with keyboards
async def send_message_with_keyboards(message):
    await message.answer('Choose an option:', reply_markup=reply_kb)
    await message.answer('Choose an inline option:', reply_markup=inline_kb)