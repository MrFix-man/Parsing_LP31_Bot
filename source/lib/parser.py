import json
from selenium import webdriver
from selenium.webdriver.common.by import By


class Parser:

    def __init__(self, option=webdriver.ChromeOptions(), driver=webdriver.Chrome()):
        self.option = option
        self.driver = driver

    def get_parsing_avito(self):

        url = "https://www.avito.ru/balashiha/kvartiry/sdam/na_dlitelnyy_srok-ASgBAgICAkSSA8gQ8AeQUg"
        self.option.add_argument("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                                 "Chrome/120.0.0.0 Safari/537.36")
        self.driver.get(url)
        page_number = 1

        for items in range(page_number):
            offer = {}

            elems = self.driver.find_elements(by=By.CSS_SELECTOR, value='div[data-marker="item"]')

            for elem in elems:
                avito_id = int(elem.get_attribute("id")[1:])
                url_offer = elem.find_element(by=By.CSS_SELECTOR, value='a[itemprop="url"]').get_attribute(
                    "href")
                item_address = elem.find_element(by=By.CSS_SELECTOR,
                                                 value='div[data-marker="item-address"]').text.split("\n")
                adress = " ".join(item_address)
                advert = elem.text.split("\n")
                price = round(int(advert[1][:-10].replace(" ", "")))
                rooms = advert[0].split(", ")[0].split()[0]
                floor = int(advert[0].split(', ')[2].split('/')[0])
                floor_level = f"Этаж: {floor}"

                offer[avito_id] = {
                    "price": price,
                    "adress": adress,
                    "rooms": rooms,
                    "floor_level": floor_level,
                    "url_offer": url_offer
                }

        with open("first_offers.json", "w") as file:
            json.dump(dict(sorted(offer.items(), key=lambda x: x[1]['price'])), file, indent=4, ensure_ascii=False)

        return dict(sorted(offer.items(), key=lambda x: x[1]['price']))

    def _stop(self):
        self.driver.close()
        self.driver.quit()


ekz_pars = Parser()
print(ekz_pars.get_parsing_avito())
