from telegram.ext import (
    Updater,
    MessageHandler,
    CommandHandler,
    Filters
)

from telegram import ReplyKeyboardMarkup, KeyboardButton
import sqlite3


class Bot:

    """Основные данные бота, команды для бота и логика работы"""
    def __init__(self, token: str):
        self.mybot = Updater(token, use_context=True)
        dp = self.mybot.dispatcher

        dp.add_handler(CommandHandler('start', self.hello_user))
        dp.add_handler(CommandHandler('search', self.search))
        # кнопки

        dp.add_handler(MessageHandler(Filters.regex('^(Начало работы)$'), self.hello_user))
        dp.add_handler(MessageHandler(Filters.regex('^(Найти квартиру)$'), self.search))  
        
    """Функция для запуска"""
    def start(self):       
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


    """Предположительно функция для обработки БД"""
    def read_sql_db(records):
        try:
            sqlite_connection = sqlite3.connect('sqlite_python.db')
            cursor = sqlite_connection.cursor()
            print("Подключен к SQLite")

            sqlite_select_query = """тут пока ХЗ"""
            cursor.execute(sqlite_select_query)
            records = cursor.fetchall()
            for row in records:
                ("id:", row[0])
                print("area:", row[1])
                print("price:", row[2])
                print("address:", row[3])
                print("district:", row[4])
                print("floor:", row[5])
                print("url:", row[6])
                print("type:", row[7], end="\n\n")

            cursor.close()

        except sqlite3.Error as error:
            print("Ошибка при работе с SQLite", error)
        finally:
            if sqlite_connection:
                sqlite_connection.close()
                print("Соединение с SQLite закрыто")

if __name__ == '__main':           
    bot1 = Bot('6478111175:AAHKn0haLwAn7dnCEIdDIkUxAhCSPuSmy64')
    bot1.start()
