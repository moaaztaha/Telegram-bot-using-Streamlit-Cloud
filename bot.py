import os
import streamlit as st
import telebot


bot = telebot.TeleBot(os.environ['SIMPLE_EGY_TOK'])


@bot.message_handler(func=lambda message: True)
def echo_message(message):
    bot.reply_to(message, message.text)


st.success("Bot is running...")
bot.polling()
