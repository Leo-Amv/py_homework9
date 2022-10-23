# Напишите бота, удаляющего из текста все слова, содержащие "абв". (текст вводит пользователь)

from cgitb import text
from telegram import Bot, Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

bot = Bot(token='5700652825:AAG2k3uHgn8mkUuFHgh9rC1f17SlXcS9Y84')
updater = Updater(token='5700652825:AAG2k3uHgn8mkUuFHgh9rC1f17SlXcS9Y84')
dispatcher = updater.dispatcher


def start(update, context):
    context.bot.send_message(update.effective_chat.id,
                             'Enter text with the words "абв" to delete them')


def message(update, context):
    text = update.message.text
    modified_text = ' '.join(
        list(filter(lambda x: 'абв' not in x.lower(), text.split())))
    context.bot.send_message(update.effective_chat.id, modified_text)


start_handler = CommandHandler('start', start)
message_handler = MessageHandler(Filters.text, message)


dispatcher.add_handler(start_handler)
dispatcher.add_handler(message_handler)

print('|Bot started|')

updater.start_polling()
updater.idle()
