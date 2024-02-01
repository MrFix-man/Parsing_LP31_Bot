from lib.parser import Parser
from lib.db import DB


class DataProcessor:

    def __init__(self, avito_url=None, drom_url=None, database_path=None) -> None:
        self.avito_url = avito_url
        self.drom_url = drom_url
        self.parser = Parser()
        self.db = DB(url=database_path)

    def start_pars(self) -> tuple:
        return self._check_url_avito(), self._check_url_drom()

    def _check_url_avito(self) -> any:
        if self.avito_url is not None:
            return self._push_bd_avito()
        return f'Заданный адрес не существует'

    def _check_url_drom(self) -> any:
        if self.drom_url is not None:
            return self._push_bd_drom()
        return f'Заданный адрес не существует'

    def _push_bd_avito(self) -> None:
        return self._bd_owner_avito()

    def _push_bd_drom(self) -> None:
        return self._bd_owner_drom()

    def _process_data_avito(self) -> list[dict]:
        all_offers = self.parser.get_parsing_avito(self.avito_url)
        return all_offers

    def _process_data_drom(self) -> list[dict]:
        cars_list = self.parser.get_parsing_drom(self.drom_url)
        return cars_list

    def _bd_owner_avito(self) -> None:
        return self.db.insert_avito(self._process_data_avito())

    def _bd_owner_drom(self) -> None:
        return self.db.insert_drom(self._process_data_drom())


if __name__ == '__main__':
    avito_url = "https://www.avito.ru/balashiha/kvartiry/sdam-ASgBAgICAUSSA8gQ?p=5"
    drom_url = 'https://auto.drom.ru/'
    database_path = r'sqlite:///F:/Parsing_with_db/source/lib/my_database.db' 
    parsing_on = DataProcessor(avito_url=avito_url, drom_url=drom_url, database_path=database_path)

    parsing_on.start_pars()
