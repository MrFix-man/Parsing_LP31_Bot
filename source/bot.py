
import logging

from telegram.ext import (
    Updater,
    MessageHandler,
    CommandHandler,
    Filters
)

from telegram import ReplyKeyboardMarkup, KeyboardButton



logging.basicConfig(filename='bot.log', level=logging.INFO)


def main_keyboard():
    return ReplyKeyboardMarkup([['Начало работы']])

#-- Приветсвуем пользователя(кнопка СТАРТ)
def hello_user(update, context):
    name = update.message.from_user.first_name
    update.message.reply_text(f'Привет, {name}! Очень рад.', reply_markup=main_keyboard())



def main():
    mybot = Updater('6478111175:AAHKn0haLwAn7dnCEIdDIkUxAhCSPuSmy64', use_context=True)
    dp = mybot.dispatcher

    dp.add_handler(CommandHandler('start', hello_user))

    # кнопки

    dp.add_handler(MessageHandler(Filters.regex('^(Начало работы)$'), hello_user))

    logging.info('Начало работы бота.')

    mybot.start_polling()
    mybot.idle()

main()
