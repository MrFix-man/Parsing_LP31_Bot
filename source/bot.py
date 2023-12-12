
import logging

from settings_bot import TOKEN
from handlers_bot import (
    hello_user
)

from telegram.ext import (
    Updater,
    MessageHandler,
    CommandHandler,
    Filters
)

from telegram import ReplyKeyboardMarkup, KeyboardButton

logging.basicConfig(filename='bot.log', level=logging.INFO)




def main():
    mybot = Updater(TOKEN, use_context=True)
    dp = mybot.dispatcher

    dp.add_handler(CommandHandler('start', hello_user))

    # кнопки

    dp.add_handler(MessageHandler(Filters.regex('^(Начало работы)$'), hello_user))

    logging.info('Начало работы бота.')

    mybot.start_polling()
    mybot.idle()

main()
