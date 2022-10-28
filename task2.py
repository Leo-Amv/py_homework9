# Создайте программу для игры с конфетами человек против бота(интелект). (Дополнительно)

from telegram import Bot, Update, ReplyKeyboardRemove
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, ConversationHandler
from random import randint

TOKEN = "5700652825:AAG2k3uHgn8mkUuFHgh9rC1f17SlXcS9Y84"


PLAYER_TURN, BOT_TURN, GAME = range(3)
player = randint(1, 2)
candies = 202


def Smart_AI(candies):
    if candies < 29:
        n = candies
    else:
        n = int(candies % (29))
        if n == 0:
            n = 1
        if n > 28:
            n = 28
    return n


def start(update, _):
    global candies
    global player
    candies = 100
    update.message.reply_text(
        f'\nEnter the number of sweets from 1 to 28 !\n\n\tTotal sweets:\t{candies}')
    if player == 1:
        update.message.reply_text(f'You started!')
        return GAME
    else:
        bot_turn(update, _)
        return GAME


def player_turn(update, _):
    global candies
    turn = update.message.text
    if turn.isdigit():
        turn = int(turn)
        if 0 < turn < 29:
            candies -= turn
            update.message.reply_text(
                f'Your turn:\t{turn}\nLeftover candy:\t{candies}')
            if candies > 0:
                bot_turn(update, _)
            else:
                update.message.reply_text(f'\n\tPLAYER WINS!\n')
                cancel(update, _)
                return ConversationHandler.END
        else:
            update.message.reply_text(
                'You must enter number from 1 to 28, try again !')
            return GAME
    else:
        update.message.reply_text('You must enter number!')
        return GAME


def game(update, _):
    global candies
    if candies > 0:
        player_turn(update, _)
    else:
        return ConversationHandler.END


def bot_turn(update, _):
    global candies
    turn = Smart_AI(candies)
    candies -= turn
    update.message.reply_text(
        f'BOT turn:\t{turn}\nLeftover candy:\t{candies}')
    if candies > 0:
        update.message.reply_text('Your turn!')
        return GAME
    else:
        update.message.reply_text(f'\n\tBOT WINS!\n')
        cancel(update, _)
        return ConversationHandler.END


def cancel(update, _):
    update.message.reply_text(
        '|GAME OVER|\nIf you want to play again, then write "/start"',
        reply_markup=ReplyKeyboardRemove()
    )
    return ConversationHandler.END


if __name__ == '__main__':
    updater = Updater(TOKEN)
    dispatcher = updater.dispatcher
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('start', start)],
        states={
            GAME: [MessageHandler(Filters.text, game)]
        },
        fallbacks=[CommandHandler('cancel', cancel)]
    )

    dispatcher.add_handler(CommandHandler('exit', cancel))
    dispatcher.add_handler(conv_handler)
    print('|BOT STARTED|')
    updater.start_polling()
    updater.idle()
