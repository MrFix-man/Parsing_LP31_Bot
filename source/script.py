import sqlite3
from lib.parser import Parser
from selenium.common.exceptions import TimeoutException, StaleElementReferenceException


class DataProcessor:

    def __init__(self, avito_url=None, drom_url=None) -> None:
        self.avito_url = avito_url
        self.drom_url = drom_url
        self.parser = Parser()

    def push_bd(self) -> str:
        return self._bd_owner()

    def _process_data(self) -> tuple[any, any]:
        try:
            if not self.avito_url or not self.drom_url:
                print("Заданный адрес не существует")
            else:
                avito_data = self.parser.get_parsing_avito(self.avito_url)
                drom_data = self.parser.get_parsing_drom(self.drom_url)
        except (TimeoutException, StaleElementReferenceException):
            print("Что то пошло не так, попробуйте позднее")

        return avito_data, drom_data

    def _bd_owner(self) -> str:
        all_offers = []
        car_off = []
        for i in self._process_data():
            for j in i:
                if j['type'] == 'real estate':
                    offer = {
                        "avito_id": j['avito_id'],
                        "price": j['price'],
                        "adress": j['adress'],
                        "district": j['district'],
                        "rooms": j['rooms'],
                        "area": j['area'],
                        "floor_level": j['floor_level'],
                        "url_offer": j['url_offer'],
                        "type": "real estate"
                    }
                    all_offers.append(offer)
                else:
                    cars_dict = {'url_cars': j['url_cars'],
                                 'car_name': j['car_name'],
                                 'car_year': j['car_year'],
                                 'short_descript': j['short_descript'],
                                 'price_int': j['price_int'],
                                 'town': j['town'],
                                 'day_of_announcement': j['day_of_announcement'],
                                 'site_evaluation': j['site_evaluation'],
                                 'type': 'cars'
                                 }
                    car_off.append(cars_dict)
        for offer in all_offers:
            conn = sqlite3.connect("my_database.db")
            c = conn.cursor()
            c.executemany("INSERT INTO avito (avito_id, price, adress, district, rooms, area, floor_level, url_offer, "
                          "type) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)", [(str(offer['avito_id']), str(offer['price']),
                                                                        str(offer['adress']), str(offer['district']),
                                                                        str(offer['rooms']), str(offer['area']),
                                                                        str(offer['floor_level']), str(offer[
                                                                                                           'url_offer']),
                                                                        str(offer['type']))])
            conn.commit()
            conn.close()
        for car in car_off:
            conn = sqlite3.connect("my_database.db", timeout=3)
            c = conn.cursor()
            c.executemany("INSERT INTO cars (url_cars,car_name,car_year,short_descript,price_int,town,"
                          "day_of_announcement,site_evaluation,type) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)",
                          [(str(car['url_cars']), str(car['car_name']), str(car['car_year']),
                            str(car['short_descript']), int(car['price_int']), str(car['town']),
                            str(car['day_of_announcement']), str(car['site_evaluation']), str(car['type']))])
            conn.commit()
            conn.close()
        return f"Запись успешна"


if __name__ == '__main__':
    avito_url = 'https://www.avito.ru/balashiha/kvartiry/sdam-ASgBAgICAUSSA8gQ?p=5'
    drom_url = 'https://moscow.drom.ru/auto/used/all/?unsold=1'

    ekz = DataProcessor(avito_url, drom_url)
    ekz.push_bd()

"""
добавить функцию иф элсе - на урл,
отловить ошибки, 
вызывать в скрипте 
______________________________________________
СОЗДАВАЛ БАЗУ С ДВУМ ТАБЛИЦАМИ... хз зачем.

import sqlite3

conn = sqlite3.connect('my_database.db')
sql = (
    "CREATE TABLE IF NOT EXISTS avito (id INTEGER PRIMARY KEY AUTOINCREMENT, avito_id STRING, price STRING, "
    "adress STRING, district STRING, rooms STRING, area STRING, floor_level STRING, url_offer STRING, type STRING)")
sql1 = (
    "CREATE TABLE IF NOT EXISTS cars(id INTEGER PRIMARY KEY AUTOINCREMENT, url_cars STRING, car_name STRING, "
    "car_year STRING, short_descript STRING, price_int INT, town STRING, day_of_announcement STRING, site_evaluation "
    "STRING, type STRING)")
coursor = conn.cursor()

coursor.execute(sql)

conn.close()

"""