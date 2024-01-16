from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.exc import OperationalError, NoSuchModuleError

from models import ParsAvito, ParsDrom


class DBError(Exception):
    """Ошибка работы с БД"""


class DB:
    def __init__(self, url: str):
        self.url = url
        self.engine = None
        self.session = None

    def connection(self):
        try:
            self.engine = create_engine(self.url)
            self.engine.connect()

            self.create_session()

        except OperationalError:
            raise DBError('Ошибка в логине, пароле, адресе сервера или самой БД')
        except NoSuchModuleError:
            raise DBError('Неверно задан модуль БД')

    def create_session(self):
        self.session = scoped_session(sessionmaker(bind=self.engine))

    def insert_avito(self, all_offers: list[dict]) -> None:
        self.connection()

        for offers in all_offers:
            pars_avito = ParsAvito(
                avito_id=offers['avito_id'],
                rooms=offers['rooms'],
                area=offers['area'],
                price=offers['price'],
                address=offers['address'],
                district=offers['district'],
                floor_level=offers['floor'],
                url_offer=offers['url'],
                type=offers['type']
            )

            self.session.add(pars_avito)
        self.session.commit()

    def query_avito(self):
        self.connection()

        return self.session.query(ParsAvito).all()

    def insert_drom(self, cars_list: list[dict]) -> None:
        self.connection()

        for cars in cars_list:
            pars_drom = ParsDrom(
                url_cars=cars['url_cars'],
                car_name=cars['car_name'],
                car_yar=cars['car_yar'],
                short_descript=cars['short_descript'],
                prise_int=cars['prise_int'],
                town=cars['town'],
                day_of_announcement=cars['day_of_announcement'],
                site_evaluation=cars['site_evaluation'],
                type=cars['type']
            )
            self.session.add(pars_drom)
        self.session.commit()


db = DB('sqlite:///pars_db.db')
