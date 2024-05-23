import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
import random

# Replace with your bot token
bot = telebot.TeleBot("6524983876:AAFrw8aKSruzLYSjZsDJ3Svdl5E8yb_RUlo")

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    # Retrieve the user's first name
    user_first_name = message.from_user.first_name

    # Generate a random 6-digit code
    random_code = ''.join(random.choices('0123456789', k=6))

    # Create the inline keyboard markup
    markup = InlineKeyboardMarkup()
    markup.row_width = 2
    markup.add(InlineKeyboardButton("Send Again", callback_data="btn1"))

    # Send the welcome message with the user's first name, random code, and buttons
    bot.send_message(message.chat.id, f"Welcome, {user_first_name}!\n\nYour OTP code is {random_code}, valid for 30 minutes! Do not share this code with anyone!", reply_markup=markup)

@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    if call.data == "btn1":
        # Remove the inline keyboard after Button 1 is clicked
        bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id, reply_markup=None)
        bot.answer_callback_query(call.id, "Button 1 clicked")
        send_welcome(call.message)
    elif call.data == "btn2":
        bot.answer_callback_query(call.id, "Button 2 clicked")
        bot.send_message(call.message.chat.id, "You pressed Button 2")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, message.text)

bot.infinity_polling()
