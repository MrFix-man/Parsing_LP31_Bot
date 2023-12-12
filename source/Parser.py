import json
from selenium import webdriver
from selenium.webdriver.common.by import By



def get_parsing_avito():


    global offer, driver
    try:
        url = "https://www.avito.ru/balashiha/kvartiry/sdam/na_dlitelnyy_srok-ASgBAgICAkSSA8gQ8AeQUg"
        option = webdriver.ChromeOptions()
        option.add_argument("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                            "Chrome/120.0.0.0 Safari/537.36")
        driver = webdriver.Chrome()
        driver.get(url=url)
        page_number = 1

        for items in range(page_number):
            offer = {}
            # all_info = []
            elems = driver.find_elements(by=By.CSS_SELECTOR, value='div[data-marker="item"]')

            for elem in elems:
                try:
                    avito_id = int(elem.get_attribute("id")[1:])
                    url_offer = elem.find_element(by=By.CSS_SELECTOR, value='a[itemprop="url"]').get_attribute("href")
                    item_address = elem.find_element(by=By.CSS_SELECTOR,
                                                     value='div[data-marker="item-address"]').text.split("\n")
                    adress = " ".join(item_address)
                    advert = elem.text.split("\n")
                    price = round(int(advert[1][:-10].replace(" ", "")))
                    rooms = advert[0].split(", ")[0].split()[0]
                    floor = int(advert[0].split(', ')[2].split('/')[0])
                    floor_level = f"Этаж: {floor}"

                    # all_info = (
                    #     price,
                    #     rooms,
                    #     item_address,
                    #     floor_level,
                    #     url_offer
                    # )
                    offer[avito_id] = {
                        "price": price,
                        "rooms": rooms,
                        "adress": adress,
                        "floor_level": floor_level,
                        "url_offer": url_offer
                    }



                except Exception as ex:
                    print(ex)

        with open("first_offers.json", "w") as file:
            json.dump(offer, file, indent=4, ensure_ascii=False)

        return offer




    finally:
        driver.close()
        driver.quit()


# def check_new_offers():
#     global driver
#     with open("first_offers.json") as f:
#         offers = json.load(f)
#
#     new_offers ={}
#     try:
#         url = "https://www.avito.ru/balashiha/kvartiry/sdam/na_dlitelnyy_srok-ASgBAgICAkSSA8gQ8AeQUg?cd=1&s=104"
#         option = webdriver.ChromeOptions()
#         option.add_argument("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
#                             "Chrome/120.0.0.0 Safari/537.36")
#         driver = webdriver.Chrome()
#         driver.get(url=url)
#         page_number = 1
#
#         for items in range(page_number):
#
#             elems = driver.find_elements(by=By.CSS_SELECTOR, value='div[data-marker="item"]')
#
#             for elem in elems:
#                 try:
#                     avito_id = int(elem.get_attribute("id")[1:])
#
#                     if avito_id in offers:
#                         print("Нечего добавлять")
#                         continue
#                     else:
#                         print("Сейчас добавим")
#                         avito_id = int(elem.get_attribute("id")[1:])
#                         url_offer = elem.find_element(by=By.CSS_SELECTOR, value='a[itemprop="url"]').get_attribute(
#                             "href")
#                         item_address = elem.find_element(by=By.CSS_SELECTOR,
#                                                          value='div[data-marker="item-address"]').text.split("\n")
#                         adress = " ".join(item_address)
#                         advert = elem.text.split("\n")
#                         price = round(int(advert[1][:-10].replace(" ", "")))
#                         rooms = advert[0].split(", ")[0].split()[0]
#                         floor = int(advert[0].split(', ')[2].split('/')[0])
#                         floor_level = f"Этаж: {floor}"
#
#                         offers[avito_id] = {
#                             "price": price,
#                             "rooms": rooms,
#                             "adress": adress,
#                             "floor_level": floor_level,
#                             "url_offer": url_offer
#                         }
#
#                         new_offers[avito_id] = {
#                             "price": price,
#                             "rooms": rooms,
#                             "adress": adress,
#                             "floor_level": floor_level,
#                             "url_offer": url_offer
#                         }
#
#                 except Exception as ex:
#                     print(ex)
#         with open("first_offers.json", "w") as file:
#             json.dump(new_offers, file, indent=4, ensure_ascii=False)
#
#
#         return new_offers
#
#
#     finally:
#         driver.close()
#         driver.quit()
#
#

def main():
    get_parsing_avito()
    #print(check_new_offers())


if __name__ == "__main__":
    main()
