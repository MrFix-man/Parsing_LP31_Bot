from selenium import webdriver
from selenium.webdriver.common.by import By


class Parser:

    def __init__(self, option=webdriver.ChromeOptions(), driver=webdriver.Chrome()) -> None:
        self.option = option
        self.driver = driver

    def get_parsing_avito(self, url) -> list[dict]:

        self.option.add_argument("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                                 "Chrome/120.0.0.0 Safari/537.36")
        self.option.add_argument('--ignore-certificate-errors-spki-list')
        self.driver.get(url)
        return self._get_info_from_avito()

    def _get_element_avito(self) -> any:
        return self.driver.find_elements(by=By.CSS_SELECTOR, value='div[data-marker="item"]')

    def _get_info_from_avito(self) -> list[dict]:
        all_offers = []
        for elem in self._get_element_avito():
            avito_id = int(elem.get_attribute("id")[1:])
            url_offer = elem.find_element(by=By.CSS_SELECTOR, value='a[itemprop="url"]').get_attribute(
                "href")
            item_address = elem.find_element(by=By.CSS_SELECTOR,
                                             value='div[data-marker="item-address"]').text.split("\n")
            adress = " ".join(item_address)
            advert = elem.text.split("\n")
            district = (item_address[1] if len(item_address) > 1 else "Балашихинский р-н")
            price = round(int(advert[1][:-10].replace(" ", "")))
            rooms = advert[0].split(", ")[0].split()[0]
            floor = int(advert[0].split(', ')[2].split('/')[0])
            floor_level = f"Этаж: {floor}"
            area = float(advert[0].split(", ")[1][:-3].replace(",", "."))
            offer = {
                "avito_id": avito_id,
                "price": price,
                "adress": adress,
                "district": district,
                "rooms": rooms,
                "area": area,
                "floor_level": floor_level,
                "url_offer": url_offer,
                "type": "real estate"
            }
            all_offers.append(offer)
        return all_offers

    def _stop(self) -> None:
        self.driver.close()
        self.driver.quit()

    def get_parsing_drom(self, url) -> list[dict]:

        self.option.add_argument("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                                 "Chrome/120.0.0.0 Safari/537.36")
        self.driver.get(url)
        return self._get_info_from_drom()

    def _get_element_drom(self) -> any:
        return self.driver.find_elements(by=By.CSS_SELECTOR, value='a[class="css-1oas0dk e1huvdhj1"]')

    def _get_info_from_drom(self) -> list[dict]:
        cars_list = []
        for element in self._get_element_drom():
            url_cars = element.get_attribute("href")
            car_name = element.find_element(by=By.CSS_SELECTOR, value='span').text[:-6]
            car_year = int(element.find_element(by=By.CSS_SELECTOR, value='span').text[-4:])
            short_descript = element.find_element(by=By.CSS_SELECTOR,
                                                  value='div[class="css-1fe6w6s e162wx9x0"]').text.strip()
            price = element.find_element(by=By.CSS_SELECTOR, value='span[data-ftid="bull_price"]').text
            price_int = int(price.replace(' ', ''))
            town = element.find_element(by=By.CSS_SELECTOR, value='span[data-ftid="bull_location"]').text
            day_of_announcement = element.find_element(by=By.CSS_SELECTOR, value='div[data-ftid="bull_date"]').text
            site_eval = element.find_element(by=By.CSS_SELECTOR, value='div[class="css-1i8tk3y eyvqki92"]').text
            site_evaluation = (' '.join(site_eval.split()[-2:]))
            if site_evaluation == '000 ₽':
                site_evaluation = 'Без оценки'
            else:
                site_evaluation = site_evaluation
            cars_dict = {'url_cars': url_cars,
                         'car_name': car_name,
                         'car_year': car_year,
                         'short_descript': short_descript,
                         'price_int': price_int,
                         'town': town,
                         'day_of_announcement': day_of_announcement,
                         'site_evaluation': site_evaluation,
                         'type': 'cars'
                         }
            cars_list.append(cars_dict)
        return cars_list

    def _stop_driver(self) -> None:
        self.driver.close()
        self.driver.quit()
