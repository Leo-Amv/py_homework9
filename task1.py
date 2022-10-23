from telegram import Bot, Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

bot = Bot(token='')
updater = Updater(token='')
dispatcher = updater.dispatcher


def message(update, context):
    text = update.message.text
    context.bot.send_message(update.effective_chat.id,
                             f'{text * 10}\n Я повторюшка :)')


message_handler = MessageHandler(Filters.text, message)


dispatcher.add_handler(message_handler)

updater.start_polling()
updater.idle()  # ctrl + c
