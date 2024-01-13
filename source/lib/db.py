# from models import ParsDb, Base
from sqlalchemy import select
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base


class Base(declarative_base()): pass


class DB:

    # не могу понять пока почему если __init__ называешь connection, то возникает ошибка
    def __init__(self, engine):
        self.engine = engine
        self.Session = sessionmaker(bind=self.engine)

    def connection(self):
        self.engine = create_engine('sqlite:///pars.db', echo=True)

    def insert_pars(self, all_offers):
        db_session = self.Session()
        # очистка базы перед добавлением новой порции данных
        db_session.query(ParsDb).delete()
        # добавление данных
        for offers in all_offers:
            pars_db = ParsDb(avito_id=offers['avito_id'],
                             rooms=offers['rooms'],
                             area=offers['area'],
                             price=offers['price'],
                             address=offers['address'],
                             district=offers['district'],
                             floor=offers['floor'],
                             url=offers['url'],
                             type=offers['type'])

            db_session.add(pars_db)
        db_session.commit()

    def query_pars(self):
        db_session = self.Session()
        # получение всех данных
        all_data = db_session.execute(select(ParsDb)).scalars().all()
        return all_data
        # можно попробовать реализовать получение данных по id


if __name__ == '__main__':


# self.sqlite_database = 'sqlite:///pars.db'
# self.engine = create_engine(self.sqlite_database)
# self.db_session = scoped_session(sessionmaker(bind=self.engine))
