# Создайте программу для игры с конфетами человек против бота(интелект). (Дополнительно)

from cgitb import text
from telegram import Bot, Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

bot = Bot(token='5700652825:AAG2k3uHgn8mkUuFHgh9rC1f17SlXcS9Y84')
updater = Updater(token='5700652825:AAG2k3uHgn8mkUuFHgh9rC1f17SlXcS9Y84')
dispatcher = updater.dispatcher


def start(update, context):
    context.bot.send_message(update.effective_chat.id, '')


def message(update, context):
    text = update.message.text
    context.bot.send_message(update.effective_chat.id, text)


start_handler = CommandHandler('start', start)
message_handler = MessageHandler(Filters.text, message)


dispatcher.add_handler(start_handler)
dispatcher.add_handler(message_handler)

print('|Bot started|')

updater.start_polling()
updater.idle()
