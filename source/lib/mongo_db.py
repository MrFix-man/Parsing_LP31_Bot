from pymongo import MongoClient


class Mongo:
    """Инициализируем ссылку на сервер и название БД"""
    def __init__(self, uri: str):
        self.uri = uri
        self.db_name = 'Users_LP31_Pars'
        self._connection = None

    def _connect(self):
        """Фнкция запуска, проверяем что сервер работает корректно
        или возвращаем ошибку"""
        if self._connection is None:
            self._connection = MongoClient(self.uri)
            self.db = self.connection[self.db_name]

    def close(self):
        """Закрытие соединения"""
        self._connection.close()

    def create_user_in_db(self, effective_user, chat_id: int) -> None:
        """Функция проверяет есть ли пользователь в базе, если его нет
        создает в базе по заданым ниже параметрам"""
        self._connect()
        user = {
            "user_id": effective_user.id,
            "first_name": effective_user.first_name,
            "last_name": effective_user.last_name,
            "username": effective_user.username,
            "chat_id": chat_id
        }
        self.db.users.insert_one(user)

    def get_user(self, user_id: int) -> dict:
        self._connect()
        return self.db.users.find_one({"user_id": user_id})
