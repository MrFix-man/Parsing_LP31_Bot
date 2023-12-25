from telegram.ext import (
    Updater,
    MessageHandler,
    CommandHandler,
    Filters
)

from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove, ParseMode


class Bot:

    """Основные данные бота, команды для бота и логика работы"""
    def __init__(self, token):
        self.mybot = Updater(token, use_context=True)
        dp = self.mybot.dispatcher
        
        dp.add_handler(CommandHandler('start', self.hello_user))
   
        """Команды на кнопки для уточнения интересующей категории объявлений"""
        dp.add_handler(MessageHandler(Filters.regex('^(Аренда жилья)$'), self.rent))
        dp.add_handler(MessageHandler(Filters.regex('^(Покупка жилья)$'), self.buy))

        """Команды на кнопки при запросе нужного количества объявлений"""
        dp.add_handler(MessageHandler(Filters.regex('^(Сделать запрос объявлений - 10)$'), self.take_10))
        dp.add_handler(MessageHandler(Filters.regex('^(Сделать запрос объявлений - 30)$'), self.take_30))
        dp.add_handler(MessageHandler(Filters.regex('^(Сделать запрос всех доступных объявлений)$'), self.take_all))   
        
    """Функция для запуска бота"""
    def start(self):       
        self.mybot.start_polling()
        self.mybot.idle()


    """Разметка кнопок клавиатуры в боте"""
    def main_keyboard(self):
        return ReplyKeyboardMarkup([
            ['Аренда жилья'],
            ['Покупка жилья']
        ])


    def keyboard_requests(self):
        return ReplyKeyboardMarkup([
        ['Сделать запрос объявлений - 10'],
        ['Сделать запрос объявлений - 30'],
        ['Сделать запрос всех доступных объявлений']
        ])
    

    """Функция приветсвует пользователя по имени"""
    def hello_user(self, update, context):
        self.name = update.message.from_user.first_name
        update.message.reply_text(f'Привет, {self.name}! Очень рад.', reply_markup=self.main_keyboard())
        update.message.reply_text(f'''В этом боте ты можешь запросить свежие объявления
с сайта авито о покупке или сдаче недвижимости.''')
        update.message.reply_text(f'Что показать? Аренду или покупку жилья?')

    """Запрос пользователя сколько нужно объявлений
    в зависимости от типа (аренда/покупка)"""
    def rent(self, update, context):
        update.message.reply_text(f'Я могу показать 10, 30 или все объявления по аренде жилья, выбери кнопку',
        reply_markup=self.keyboard_requests())

    def buy(self, update, context):
        update.message.reply_text(f'Я могу показать 10, 30 или все объявления по продаже жилья, выбери кнопку',
        reply_markup=self.keyboard_requests())


    """Блок функций под кнопки в боте на вывод объявлений"""
    def take_10(self, update, context):
        num_of_requests = 10
        update.message.reply_text(self._get_data(update, context))

    def take_30(self, update, context):
        num_of_requests = 30
        update.message.reply_text(self._get_data(update, context))

    def take_all(self, update, context):
        update.message.reply_text(self._get_data(update, context))



    """Функции для отправки пользователю финального текста"""
    def _get_data(self, update, context):
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
        update.message.reply_text(self._create_final_text(data), reply_markup=self.main_keyboard(), parse_mode=ParseMode.HTML)
      
    
    
    def _create_final_text(self, data):
        user_final_text = f"""<b>Номер объявления в системе</b> - {data[0]['id']}
<b>Комнат в жилье</b> - {data[0]['room']}
<b>Общая площадь</b> - {data[0]['area']}
<b>Цена</b> - {data[0]['price']}
<b>Улица</b> - {data[0]['adress']}
<b>Район</b> - {data[0]['distric']}
<b>Этаж</b> - {data[0]['floor']}
<b>Ссылка</b> - {data[0]['url']}
<b>Вид продажи</b> - {data[0]['type']}"""
        return user_final_text




if __name__ == '__main__':           
    bot1 = Bot('6478111175:AAHKn0haLwAn7dnCEIdDIkUxAhCSPuSmy64')
    bot1.start()

