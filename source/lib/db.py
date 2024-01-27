from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.exc import OperationalError, NoSuchModuleError
from .models import ParsAvito, ParsDrom


class DBError(Exception):
    """Ошибка работы с БД"""


class DB:
    def __init__(self, url: str):
        self.url = url
        self.engine = None
        self.session = None
        self._connect = None

    def _connection(self):
        try:
            if self._connect is None:
                self.engine = create_engine(self.url)
                self._connect = self.engine.connect()

        except OperationalError:
            raise DBError('Ошибка в логине, пароле, адресе сервера или самой БД')
        except NoSuchModuleError:
            raise DBError('Неверно задан модуль БД')

    def create_session(self):
        self.session = scoped_session(sessionmaker(bind=self.engine))

    def insert_avito(self, all_offers: list[dict]) -> None:
        self._connection()
        self.create_session()
        base_avito_ids = self.session.query(ParsAvito.avito_id).all()
        for offers in all_offers:
            if offers['avito_id'] not in [flat[0] for flat in base_avito_ids]:
                pars_avito = ParsAvito(
                    avito_id=offers['avito_id'],
                    rooms=offers['rooms'],
                    area=offers['area'],
                    price=offers['price'],
                    adress=offers['adress'],
                    district=offers['district'],
                    floor_level=offers['floor_level'],
                    url_offer=offers['url_offer'],
                    type=offers['type']
                )

                self.session.add(pars_avito)

        self.session.commit()
        self.session.close()

    def query_avito(self):
        self._connection()
        return self.session.query(ParsAvito).all()

    def insert_drom(self, cars_list: list[dict]) -> None:
        self._connection()
        self.create_session()
        base_drom_url = self.session.query(ParsDrom.url_cars).all()
        for cars in cars_list:
            if cars['url_cars'] not in [car[0] for car in base_drom_url]:
                pars_drom = ParsDrom(
                    url_cars=cars['url_cars'],
                    car_name=cars['car_name'],
                    car_year=cars['car_year'],
                    short_descript=cars['short_descript'],
                    price_int=cars['price_int'],
                    town=cars['town'],
                    day_of_announcement=cars['day_of_announcement'],
                    site_evaluation=cars['site_evaluation'],
                    type=cars['type']
                )
                self.session.add(pars_drom)

        self.session.commit()
        self.session.close()

    def query_drom(self):
        self._connection()
        return self.session.query(ParsDrom).all()
