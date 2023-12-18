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

        self._get_element()
        return self._get_info()

    def _get_element(self) -> any:
        return self.driver.find_elements(by=By.CSS_SELECTOR, value='div[data-marker="item"]')

    def _get_info(self) -> list[dict]:
        elems = self._get_element()
        offer = {}
        for elem in elems:
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
            offer[avito_id] = {
                "price": price,
                "adress": adress,
                "district": district,
                "rooms": rooms,
                "area": area,
                "floor_level": floor_level,
                "url_offer": url_offer,
            }

        return [offer]

    def _stop(self) -> None:
        self.driver.close()
        self.driver.quit()


ekz_pars = Parser()
print(ekz_pars.get_parsing_avito())
