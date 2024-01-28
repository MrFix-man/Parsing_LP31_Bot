from telegram.ext import (
    Updater, MessageHandler,
    CommandHandler, Filters
)

from lib.bot_utils import (
    main_keyboard, keyboard_requests_avito, keyboard_requests_drom,
    take_10_avito, take_10_drom, take_30_avito, take_30_drom,
    take_all_avito, take_all_drom, check_user_in_db
)
from lib.mongo_db import Mongo
from lib.db import DB


class Bot:

    """Основные данные бота, команды для бота и логика работы"""
    def __init__(self, token: str, mongo_url: str):
        self.mybot = Updater(token, use_context=True)
        dp = self.mybot.dispatcher
        self.mongo = Mongo(mongo_url)
        self.db = DB('sqlite:///pars_db.db')

        dp.add_handler(CommandHandler('start', self.hello_user))

        """Команды на кнопки для уточнения интересующей категории объявлений"""
        dp.add_handler(MessageHandler(
            Filters.regex('^(Аренда жилья)$'),
            self.rent_aparment
        ))
        dp.add_handler(
            MessageHandler(Filters.regex('^(Покупка авто)$'),
                           self.buy_car))
        dp.add_handler(
            MessageHandler(Filters.regex('^(Аренда жилья)$'),
                           self.rent_aparment))

        """
        Команды на кнопки при запросе нужного количества
        объявлений avito или drom
        """
        dp.add_handler(
            MessageHandler(Filters.regex('^(Сделать 10 запросов с авито)$'),
                           take_10_avito))
        dp.add_handler(
            MessageHandler(Filters.regex('^(Сделать 30 запросов с авито)$'),
                           take_30_avito))
        dp.add_handler(
            MessageHandler(Filters.regex('^(Сделать все запросы с авито)$'),
                           take_all_avito))
        dp.add_handler(
            MessageHandler(Filters.regex('^(Сделать 10 запросов с дром)$'),
                           take_10_drom))
        dp.add_handler(
            MessageHandler(Filters.regex('^(Сделать 30 запросов с дром)$'),
                           take_30_drom))
        dp.add_handler(
            MessageHandler(Filters.regex('^(Сделать все запросы с дром)$'),
                           take_all_drom))

    def start(self):
        """Функция для запуска бота"""
        self.mybot.start_polling()
        self.mybot.idle()

    def hello_user(self, update, context):
        """Функция приветсвует пользователя по имени"""
        check_user_in_db(update.effective_user, update.message.chat_id)
        self.name = update.message.from_user.first_name
        update.message.reply_text(f'Привет, {self.name}! Очень рад.',
                                  reply_markup=main_keyboard())
        update.message.reply_text(
            'Расскажу какие есть возможности у этого бота:'
            )
        update.message.reply_text(
            'Можно смотреть объявления на авито по арнеде жилья'
        )
        update.message.reply_text(
            'Или объявления на дром по продаже авто'
        )
        update.message.reply_text(
            'Выбери что смотрим, авто или квартира.'
              )

    def rent_aparment(self, update, context):
        """Запрос пользователя сколько нужно объявлений
        в зависимости от типа (аренда/покупка)"""
        update.message.reply_text(
            'Отлично, смотрим аренду жилья на авито'
            )
        update.message.reply_text(
            'Выбери сколько показать объявлений',
            reply_markup=keyboard_requests_avito())

    def buy_car(self, update, context):
        update.message.reply_text(
            'Отлично, смотрим автомобили на дроме'
            )
        update.message.reply_text(
            'Выбери сколько показать объявлений',
            reply_markup=keyboard_requests_drom())

    def check_user_in_db(self, effective_user, chat_id):
        """Функция работы с МонгоДБ"""
        user = self.mongo.get_user(effective_user.id)
        if not user:
            self.mongo.create_user_in_db(effective_user, chat_id)
        return user


if __name__ == '__main__':
    token = '6478111175:AAHKn0haLwAn7dnCEIdDIkUxAhCSPuSmy64'
    mongo_url = 'mongodb://localhost:27017/'
    bot1 = Bot(token, mongo_url)
    bot1.start()
