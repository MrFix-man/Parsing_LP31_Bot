from db_connect import engine
from models import Pars_db
from db_connect import db_session

#Тестовые данные для проверки

data = {'rooms':'3','area':'dfsdsaf', 'price':'3412',
        'address':'asdafa', 'district':'adfadsfa',
        'floor':'234', 'url':'kjbadfkjba', 'type':'safDS'
        }

def insert_pars(data):

    conn = engine.connect()
    result = conn.execute(db_session.query(), data)
    conn.commit
    conn.close

def query_pars():
    conn = engine.connect()
    result = conn.execute(Pars_db.query().all)