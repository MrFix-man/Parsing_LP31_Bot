from telegram import ReplyKeyboardMarkup, ParseMode
from lib.mongo_db import Mongo
from lib.db import DB


mongo = Mongo('mongodb://localhost:27017/')
db = DB('sqlite:///pars_db.db')


def main_keyboard():
    """Клавиатура основная в боте"""
    return ReplyKeyboardMarkup([
        ['Аренда жилья'],
        ['Покупка авто']
    ])


def keyboard_requests_avito():
    """Клавиатура количества запросов в боте AVITO"""
    return ReplyKeyboardMarkup([
        ['Сделать 10 запросов с авито'],
        ['Сделать 30 запросов с авито'],
        ['Сделать все запросы с авито']
        ])


def keyboard_requests_drom():
    """Клавиатура количества запросов в боте DROM!!!!"""
    return ReplyKeyboardMarkup([
        ['Сделать 10 запросов с дром'],
        ['Сделать 30 запросов с дром'],
        ['Сделать все запросы с дром']
        ])


def check_user_in_db(effective_user, chat_id):
    """Функция работы с МонгоДБ, проверка пользователя"""
    user = mongo.get_user(effective_user.id)
    if not user:
        mongo.create_user_in_db(effective_user, chat_id)
    return user


def take_10_avito(update, context):
    """Блок функций под кнопки в боте на вывод объявлений"""
    query = db.query_avito(10)
    text = '10 раз авито нихера!!!'
    for data in query:
        text = _create_final_text_avito(data)
    update.message.reply_text(text, reply_markup=main_keyboard())


def take_30_avito(update, context):
    query = db.query_avito(30)
    text = '30 раз авито нихера!!!'
    for data in query:
        text = _create_final_text_avito(data)
    update.message.reply_text(text, reply_markup=main_keyboard())


def take_all_avito(update, context):
    query = db.query_avito()
    text = '50 раз авито нихера!!!'
    for data in query:
        text = _create_final_text_avito(data)
    update.message.reply_text(text, reply_markup=main_keyboard())


def take_10_drom(update, context):
    """Блок функций под кнопки в боте на вывод объявлений"""
    query = db.query_drom(10)
    text = '10 раз дром нихера!!!'
    for data in query:
        text = _create_final_text_drom(data)
    update.message.reply_text(text, reply_markup=main_keyboard())


def take_30_drom(update, context):
    query = db.query_drom(30)
    text = '30 раз дром нихера!!!'
    for data in query:
        text = _create_final_text_drom(data)
    update.message.reply_text(text, reply_markup=main_keyboard())


def take_all_drom(update, context):
    query = db.query_drom()
    text = '50 раз дром нихера!!!'
    for data in query:
        text = _create_final_text_drom(data)
    update.message.reply_text(text, reply_markup=main_keyboard())


def _get_data_avito(update, context):
    """Функции для отправки пользователю финального текста"""
    data = [{
        'avito_id': 'id объявления',
        'room': 'Количество комнат',
        'area': 'Площадь жилья',
        'price': 'Цена жилья',
        'adress': 'Улица',
        'distric': 'Район',
        'floor_level': 'Этаж',
        'url_offer': 'Ссылка на объявление',
        'type': 'Тип объявление - продажа/аренда'
        }]
    update.message.reply_text(
        _create_final_text_avito(data),
        reply_markup=main_keyboard(),
        parse_mode=ParseMode.HTML)


def _get_data_drom(update, context):
    """Функции для отправки пользователю финального текста"""
    data = [{
        'url_cars': 'ссылка на объявление',
        'car_name': 'наименование авто',
        'car_yar': 'год выпуска',
        'short_descript': 'короткое описание',
        'prise_int': 'Цена',
        'town': 'Город',
        'day_of_announcement': 'дата публикации',
        'site_evaluation': 'я хрен его что это',
        'type': 'Тип объявленя'
        }]
    update.message.reply_text(
        _create_final_text_avito(data),
        reply_markup=main_keyboard(),
        parse_mode=ParseMode.HTML)


def _create_final_text_avito(data):
    user_final_text = [
        f"<b>Номер объявления в системе</b> - {data[0]['avito_id']}\n",
        f"<b>Комнат в жилье</b> - {data[0]['room']}\n",
        f"<b>Общая площадь</b> - {data[0]['area']}\n",
        f"<b>Цена</b> - {data[0]['price']}\n",
        f"<b>Улица</b> - {data[0]['adress']}\n",
        f"<b>Район</b> - {data[0]['distric']}\n",
        f"<b>Этаж</b> - {data[0]['floor_level']}\n",
        f"<b>Ссылка</b> - {data[0]['url_offer']}\n",
        f"<b>Вид продажи</b> - {data[0]['type']}"
        ]
    return user_final_text


def _create_final_text_drom(data):
    user_final_text = [
        f"<b>Ссылка на сайт</b> - {data[0]['url_cars']}\n",
        f"<b>Наименование авто</b> - {data[0]['car_name']}\n",
        f"<b>Год выпуска</b> - {data[0]['car_yar']}\n",
        f"<b>Короткое описание</b> - {data[0]['short_descript']}\n",
        f"<b>Цена</b> - {data[0]['prise_int']}\n",
        f"<b>Город</b> - {data[0]['town']}\n",
        f"<b>Дата публикации</b> - {data[0]['day_of_announcement']}\n",
        f"<b>ХЗ</b> - {data[0]['site_evaluation']}\n",
        f"<b>Вид продажи</b> - {data[0]['type']}"
        ]
    return user_final_text
