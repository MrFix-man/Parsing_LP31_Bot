from telegram.ext import (
    Updater,
    MessageHandler,
    CommandHandler,
    Filters
)

from telegram import ReplyKeyboardMarkup, KeyboardButton


class Bot:

    """Основные данные бота"""
    def __init__(self, token: str):
        self.mybot = Updater(token, use_context=True)
       
        
    """Запуск бота и работа с командами, устанавливаем кнопки"""
    def main(self):
        dp = self.mybot.dispatcher

        dp.add_handler(CommandHandler('start', self.hello_user))
        dp.add_handler(CommandHandler('search', self.search))
        # кнопки

        dp.add_handler(MessageHandler(Filters.regex('^(Начало работы)$'), self.hello_user))
        dp.add_handler(MessageHandler(Filters.regex('^(Найти квартиру)$'), self.search))

        self.mybot.start_polling()
        self.mybot.idle()


    """Разметка кнопок клавиатуры в боте"""
    def main_keyboard(self):
        return ReplyKeyboardMarkup([['Начало работы'], ['Найти квартиру']])
    

    """Функция приветсвует пользователя по имени"""
    def hello_user(self, update, context):
        self.name = update.message.from_user.first_name
        update.message.reply_text(f'Привет, {self.name}! Очень рад.', reply_markup=self.main_keyboard())


    """Пока кнопка выводит в консоль данные, получаемые от пользователя бота"""
    def search(self, update, context):
        print(update.message.from_user)
        
bot1 = Bot('6478111175:AAHKn0haLwAn7dnCEIdDIkUxAhCSPuSmy64')
bot1.main()
