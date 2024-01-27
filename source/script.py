import sqlite3
from lib.parser import Parser
from lib.db import DB


class DataProcessor:

    def __init__(self, avito_url=None, drom_url=None, database_path=None) -> None:
        self.avito_url = avito_url
        self.drom_url = drom_url
        self.parser = Parser()
        self.db = DB(url=r'sqlite:///F:/Parsing_with_db/source/lib/my_database.db')
        self.database_path = database_path

    def push_bd_avito(self) -> None:
        return self._bd_owner_avito()

    def push_bd_drom(self) -> None:
        return self._bd_owner_drom()

    def _process_data_avito(self) -> list[dict]:
        all_offers = self.parser.get_parsing_avito(self.avito_url)
        return all_offers

    def _get_data_from_database_avito(self):
        conn = sqlite3.connect(database_path)
        cursor = conn.cursor()
        cursor.execute("SELECT avito_id FROM pars_avito")
        data_avito = cursor.fetchall()

        cursor.close()
        conn.close()

        return data_avito

    def _get_data_from_database_drom(self):
        conn = sqlite3.connect(database_path)
        cursor = conn.cursor()
        cursor.execute("SELECT url_cars FROM pars_drom")
        data_drom = cursor.fetchall()
        cursor.close()
        conn.close()
        return data_drom

    def _see_change_avito(self) -> list[dict]:
        new_offers_avito = []
        for i in self._process_data_avito():
            if i['avito_id'] in [x[0] for x in self._get_data_from_database_avito()]:
                continue
            else:
                new_offers_avito.append(i)
        return new_offers_avito

    def _see_change_drom(self) -> list[dict]:
        new_offers_drom = []
        for i in self._process_data_drom():
            if i['url_cars'] in [x[0] for x in self._get_data_from_database_drom()]:
                continue
            else:
                new_offers_drom.append(i)
        return new_offers_drom

    def _process_data_drom(self) -> list[dict]:
        cars_list = self.parser.get_parsing_drom(self.drom_url)
        return cars_list

    def _bd_owner_avito(self) -> None:
        return self.db.insert_avito(self._see_change_avito())

    def _bd_owner_drom(self) -> None:
        return self.db.insert_drom(self._see_change_drom())


if __name__ == '__main__':
    avito_url = 'https://www.avito.ru/balashiha/kvartiry/sdam-ASgBAgICAUSSA8gQ?p=5'
    drom_url = 'https://auto.drom.ru/'
    database_path = "F:/Parsing_with_db/source/lib/my_database.db"

    avito = DataProcessor(avito_url=avito_url)
    drom = DataProcessor(drom_url=drom_url)

    drom.push_bd_drom()
    avito.push_bd_avito()
