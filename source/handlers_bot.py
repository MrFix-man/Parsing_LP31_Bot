from utils_bot import main_keyboard

# Тут все функции связанные с хэндлерами



#-- Приветсвуем пользователя(кнопка СТАРТ)
def hello_user(update, context):
    name = update.message.from_user.first_name
    update.message.reply_text(f'Привет, {name}! Очень рад.', reply_markup=main_keyboard())
    
