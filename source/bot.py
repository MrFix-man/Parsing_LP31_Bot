from telegram.ext import (
    Updater,
    MessageHandler,
    CommandHandler,
    Filters
)

from telegram import ReplyKeyboardMarkup, KeyboardButton


# херня


def main_keyboard():
    return ReplyKeyboardMarkup([['Начало работы', 'Найти квартиру']])

#-- Приветсвуем пользователя(кнопка СТАРТ)
def hello_user(update, context):
    name = update.message.from_user.first_name
    update.message.reply_text(f'Привет, {name}! Очень рад.', reply_markup=main_keyboard())

def search():
    pass

def main():
    mybot = Updater('6478111175:AAHKn0haLwAn7dnCEIdDIkUxAhCSPuSmy64', use_context=True)
    dp = mybot.dispatcher

    dp.add_handler(CommandHandler('start', hello_user))
    dp.add_handler(CommandHandler('search', search))
    # кнопки

    dp.add_handler(MessageHandler(Filters.regex('^(Начало работы)$'), hello_user))
    dp.add_handler(MessageHandler(Filters.regex('^(Найти квартиру)$'), search))

    mybot.start_polling()
    mybot.idle()

main()
