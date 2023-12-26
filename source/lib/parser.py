from selenium import webdriver
from selenium.webdriver.common.by import By


class Parser:

    def __init__(self, option=webdriver.ChromeOptions(), driver=webdriver.Chrome()) -> None:
        self.option = option
        self.driver = driver

    def get_parsing_avito(self) -> list[dict]:
        url = ("https://www.avito.ru/balashiha/kvartiry/sdam/na_dlitelnyy_srok-ASgBAgICAkSSA8gQ8AeQUg?context"
               "=H4sIAAAAAAAA_0q0MrSqLraysFJKK8rPDUhMT1WyLrYyNLNSKk5NLErOcMsvyg3PTElPLVGyrgUEAAD__xf8iH4tAAAA")
        self.option.add_argument("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                                 "Chrome/120.0.0.0 Safari/537.36")
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

    def get_parsing_drom(self):
        url = "https://moscow.drom.ru/auto/used/all/?unsold=1"
        self.option.add_argument("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                                 "Chrome/120.0.0.0 Safari/537.36")
        self.driver.get(url)
        self._get_element_drom()
        return self._get_info_from_drom()

    def _get_element_drom(self):
        return self.driver.find_elements(by=By.CSS_SELECTOR, value='a[class="css-1oas0dk e1huvdhj1"]')

    def _get_info_from_drom(self):
        cars_list = []

        for element in self._get_element_drom():
            url_cars = element.get_attribute("href")
            car_name = element.find_element(by=By.CSS_SELECTOR, value='span').text[:-6]
            car_year = int(element.find_element(by=By.CSS_SELECTOR, value='span').text[-4:])
            short_descript = element.find_element(by=By.CSS_SELECTOR,
                                                  value='div[class="css-1fe6w6s e162wx9x0"').text.strip()
            price = element.find_element(by=By.CSS_SELECTOR, value='span[data-ftid="bull_price"]').text
            price_int = int(price.replace(' ', ''))
            town = element.find_element(by=By.CSS_SELECTOR, value='span[data-ftid="bull_location"]').text
            day_of_announcement = element.find_element(by=By.CSS_SELECTOR, value='div[data-ftid="bull_date"]').text

            cars_dict = {'url_cars': url_cars,
                         'car_name': car_name,
                         'car_year': car_year,
                         'short_descript': short_descript,
                         'price_int': price_int,
                         'town': town,
                         'day_of_announcement': day_of_announcement
                         }
            cars_list.append(cars_dict)
        return cars_list

    def _stop_driver(self):
        self.driver.close()
        self.driver.quit()


avito = Parser()
drom = Parser()
print(drom.get_parsing_drom())
