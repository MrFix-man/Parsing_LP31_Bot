from telegram.ext import (
    Updater,
    MessageHandler,
    CommandHandler,
    Filters
)

from telegram import ReplyKeyboardMarkup, ParseMode

from lib.mongo_db import Mongo


class Bot:

    """Основные данные бота, команды для бота и логика работы"""
    def __init__(self, token: str, mongo_url: str):
        self.mybot = Updater(token, use_context=True)
        dp = self.mybot.dispatcher
        self.mongo = Mongo(mongo_url)

        dp.add_handler(CommandHandler('start', self.hello_user))

        """Команды на кнопки для уточнения интересующей категории объявлений"""
        dp.add_handler(MessageHandler(
            Filters.regex('^(Аренда жилья)$'),
            self.rent
        ))
        dp.add_handler(
            MessageHandler(Filters.regex('^(Покупка авто)$'), self.buy))
        dp.add_handler(
            MessageHandler(Filters.regex('^(Аренда жилья)$'), self.rent))

        """Команды на кнопки при запросе нужного количества объявлений"""
        dp.add_handler(
            MessageHandler(Filters.regex('^(Сделать запрос объявлений - 10)$'),
                           self.take_10))
        dp.add_handler(
            MessageHandler(Filters.regex('^(Сделать запрос объявлений - 30)$'),
                           self.take_30))
        dp.add_handler(
            MessageHandler(Filters.regex('^(Сделать запрос всех объявлений)$'),
                           self.take_all))

    def start(self):
        """Функция для запуска бота"""
        self.mybot.start_polling()
        self.mybot.idle()

    def main_keyboard(self):
        """Разметка кнопок клавиатуры в боте"""
        return ReplyKeyboardMarkup([
            ['Аренда жилья'],
            ['Покупка авто']
        ])

    def keyboard_requests(self):
        return ReplyKeyboardMarkup([
            ['Сделать запрос объявлений - 10'],
            ['Сделать запрос объявлений - 30'],
            ['Сделать запрос всех объявлений']
            ])

    def hello_user(self, update, context):
        """Функция приветсвует пользователя по имени"""
        self.check_user_in_db(update.effective_user, update.message.chat_id)
        self.name = update.message.from_user.first_name
        update.message.reply_text(f'Привет, {self.name}! Очень рад.',
                                  reply_markup=self.main_keyboard())
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

    """Запрос пользователя сколько нужно объявлений
    в зависимости от типа (аренда/покупка)"""
    def rent(self, update, context):
        update.message.reply_text(
            'Отлично, смотрим аренду жилья на авито'
            )
        update.message.reply_text(
            'Выбери сколько показать объявлений',
            reply_markup=self.keyboard_requests())

    def buy(self, update, context):
        update.message.reply_text(
            'Отлично, смотрим автомобили на дроме'
            )
        update.message.reply_text(
            'Выбери сколько показать объявлений',
            reply_markup=self.keyboard_requests())

    def take_10(self, update, context):
        """Блок функций под кнопки в боте на вывод объявлений"""
        # num_of_requests = 10
        update.message.reply_text(self._get_data(update, context))

    def take_30(self, update, context):
        # num_of_requests = 30
        update.message.reply_text(self._get_data(update, context))

    def take_all(self, update, context):
        update.message.reply_text(self._get_data(update, context))

    def _get_data(self, update, context):
        """Функции для отправки пользователю финального текста"""
        data = [{
            'id': 'id объявления',
            'room': 'Количество комнат',
            'area': 'Площадь жилья',
            'price': 'Цена жилья',
            'adress': 'Улица',
            'distric': 'Район',
            'floor': 'Этаж',
            'url': 'Ссылка на объявление',
            'type': 'Тип объявление - продажа/аренда'
        }]
        update.message.reply_text(
            self._create_final_text(data),
            reply_markup=self.main_keyboard(),
            parse_mode=ParseMode.HTML)

    def _create_final_text(self, data):
        user_final_text = f"""<b>Номер объявления в системе</b> -
{data[0]['id']}
<b>Комнат в жилье</b> - {data[0]['room']}
<b>Общая площадь</b> - {data[0]['area']}
<b>Цена</b> - {data[0]['price']}
<b>Улица</b> - {data[0]['adress']}
<b>Район</b> - {data[0]['distric']}
<b>Этаж</b> - {data[0]['floor']}
<b>Ссылка</b> - {data[0]['url']}
<b>Вид продажи</b> - {data[0]['type']}"""
        return user_final_text

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
