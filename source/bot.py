from telegram.ext import (
    Updater,
    MessageHandler,
    CommandHandler,
    Filters,
    ConversationHandler
)

from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove, ParseMode


class Bot:

    """Основные данные бота, команды для бота и логика работы"""
    def __init__(self, token, num_req=0):
        self.mybot = Updater(token, use_context=True)
        dp = self.mybot.dispatcher
        self.num_req = num_req
    
    
        user_req = ConversationHandler(
            entry_points=[MessageHandler(Filters.regex('^(Сделать запрос объявлений)$'), self.start_req)],

        states={
            'num_req': [MessageHandler(Filters.text, self.take_num_req)],
            'final': [MessageHandler(Filters.regex('^(Показать)$'), self.get_data)]
        },
        fallbacks= [
            MessageHandler(Filters.text | Filters.photo | Filters.video | Filters.document | Filters.location,
            self.dont_know)
        ]
        )

        dp.add_handler(user_req)
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
        return ReplyKeyboardMarkup([
        ['Начало работы'], ['Найти квартиру'],
        ['Сделать запрос объявлений']
        ])
    

    """Функция приветсвует пользователя по имени"""
    def hello_user(self, update, context):
        self.name = update.message.from_user.first_name
        update.message.reply_text(f'Привет, {self.name}! Очень рад.', reply_markup=self.main_keyboard())


    """Пока кнопка выводит в консоль данные, получаемые от пользователя бота"""
    def search(self, update, context):
        print(update.message.from_user)


    """Предположительно функция для обработки БД"""
    def make_user_list(self, update, context):
        pass

    def start_req(self, update, context):
        update.message.reply_text(
            'Привет, сколько объявлений нужно отобразить?',
            reply_markup=ReplyKeyboardRemove() #-- тормозим основную клавиатуру в боте
        )
        return 'num_req'
    
    def take_num_req(self, update, context):
        try:
            update.message.reply_text('Записал, подбираю варианты...')
            reply_keyboard = [['Показать']]
            update.message.reply_text('Нажмите на кнопку ниже для отображения результата.', 
            reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)
            )
            num_req = int(update.message.text)
            context.user_data['user_req'] = {'num_req': num_req}
        except(ValueError, TypeError):
            user_text = f'Вы не ввели число, введите пожалуйста желаемое число запросов.'
            update.message.reply_text(user_text)
            return 'num_req'
        return 'final' 
        
    
    def dont_know(self, update, context):
        update.message.reply_text(f'Не целевое дейсвие, я понятия не имею что с этим делать...')


    def get_data(self, update, context):
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
        user_final_text = f"""<b>Номер объявления в системе</b> - {data[0]['id']}
<b>Комнат в жилье</b> - {data[0]['room']}
<b>Общая площадь</b> - {data[0]['area']}
<b>Цена</b> - {data[0]['price']}
<b>Улица</b> - {data[0]['adress']}
<b>Район</b> - {data[0]['distric']}
<b>Этаж</b> - {data[0]['floor']}
<b>Ссылка</b> - {data[0]['url']}
<b>Вид продажи</b> - {data[0]['type']}
Было введено ранее число запросов - {self.num_req}"""
        update.message.reply_text(user_final_text, parse_mode=ParseMode.HTML)
        return ConversationHandler.END

if __name__ == '__main__':           
    bot1 = Bot('6478111175:AAHKn0haLwAn7dnCEIdDIkUxAhCSPuSmy64')
    bot1.start()

