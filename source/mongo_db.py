from pymongo import MongoClient



class Mongo:
    """Инициализируем ссылку на сервер и название БД"""
    def __init__(self):
        self.uri = 'mongodb://localhost:27017/'
        self.db_name = 'Users_LP31_Pars'
        self.connection = None
        

    """Фнкция запуска, проверяем что сервер работает корректно
    или возвращаем ошибку"""
    def connect(self):
        self.client = MongoClient(self.uri)
        self.db = self.client[self.db_name]


    """Закрытие соединения"""
    def close(self):
        self.client.close()
          

    """Функция проверяет есть ли пользователь в базе, если его нет
    создает в базе по заданым ниже параметрам"""
    def create_user_in_db(self, effective_user, chat_id):    
        self.connect() #-- Пробуем подключтиться
        user = {
                "user_id": effective_user.id,
                "first_name": effective_user.first_name,
                "last_name": effective_user.last_name,
                "username": effective_user.username,
                "chat_id": chat_id
                }
        self.db.users.insert_one(user)
        self.close() #-- Закрываем содинение
        return user


    def get_user(self, user_id):
        self.connect() #-- Пробуем подключтиться
        user = self.db.users.find_one({"user_id": user_id})
        self.close() #-- Закрывам соединение
        return user
        
     
            
