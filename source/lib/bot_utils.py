from telegram import ReplyKeyboardMarkup, ParseMode
from lib.mongo_db import Mongo
from lib.db import DB


mongo = Mongo('mongodb://localhost:27017/')
db = DB('sqlite:///my_database1.db')   # source/


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
    query = db.query_avito_for_bot(10)
    text = []
    for data in query:
        text.append(_create_final_text_avito(data))
    update.message.reply_text(
        "\n".join(text), reply_markup=main_keyboard(),
        parse_mode=ParseMode.HTML
        )


def take_30_avito(update, context):
    query = db.query_avito_for_bot(30)
    text = []
    for data in query:
        text.append(_create_final_text_avito(data))
    update.message.reply_text(
        "\n".join(text), reply_markup=main_keyboard(),
        parse_mode=ParseMode.HTML
        )


def take_all_avito(update, context):
    query = db.query_avito_for_bot()
    text = []
    for data in query:
        text.append(_create_final_text_avito(data))
    update.message.reply_text(
        "\n".join(text), reply_markup=main_keyboard(),
        parse_mode=ParseMode.HTML
        )


def take_10_drom(update, context):
    """Блок функций под кнопки в боте на вывод объявлений"""
    query = db.query_drom_for_bot(10)
    text = []
    for data in query:
        text.append(_create_final_text_drom(data))
    update.message.reply_text(
        "\n".join(text), reply_markup=main_keyboard(),
        parse_mode=ParseMode.HTML
        )


def take_30_drom(update, context):
    query = db.query_drom_for_bot(30)
    text = []
    for data in query:
        text.append(_create_final_text_drom(data))
    update.message.reply_text(
        "\n".join(text), reply_markup=main_keyboard(),
        parse_mode=ParseMode.HTML
        )


def take_all_drom(update, context):
    query = db.query_drom_for_bot()
    text = []
    for data in query:
        text.append(_create_final_text_drom(data))
    update.message.reply_text(
        "\n".join(text), reply_markup=main_keyboard(),
        parse_mode=ParseMode.HTML
        )


def _create_final_text_avito(data):
    user_final_text = (
        f"<b>Номер объявления в системе</b> - {data.avito_id}\n"
        f"<b>Комнат в жилье</b> - {data.rooms}\n"
        f"<b>Общая площадь</b> - {data.area}\n"
        f"<b>Цена</b> - {data.price}\n"
        f"<b>Улица</b> - {data.adress}\n"
        f"<b>Район</b> - {data.district}\n"
        f"<b>Этаж</b> - {data.floor_level}\n"
        f"<b>Ссылка</b> - {data.url_offer}\n"
        f"<b>Вид продажи</b> - {data.type}\n"
    )
    return user_final_text


def _create_final_text_drom(data):
    user_final_text = (
        f"<b>Ссылка на сайт</b> - {data.url_cars}\n"
        f"<b>Наименование авто</b> - {data.car_name}\n"
        f"<b>Год выпуска</b> - {data.car_year}\n"
        f"<b>Короткое описание</b> - {data.short_descript}\n"
        f"<b>Цена</b> - {data.price_int}\n"
        f"<b>Город</b> - {data.town}\n"
        f"<b>Дата публикации</b> - {data.day_of_announcement}\n"
        f"<b>Оценка сайта</b> - {data.site_evaluation}\n"
        f"<b>Вид продажи</b> - {data.type}\n"
    )
    return user_final_text
