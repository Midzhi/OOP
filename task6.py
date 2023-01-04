# # 6 4-балла
# Спарсить сайт лалафо с недвижимостью (аренда посуточно)
# https://lalafo.kg/kyrgyzstan/nedvizhimost
# Название
# Цену
# Фото
# Адрес
# Дату
# Ссылку на пост

import requests
from bs4 import BeautifulSoup
import json
import re

url = 'https://edc.sale/ru/ru/real-estate/rent/apartments/'
my_html = requests.get(url)
my_html.encoding = "utf8"
soup = BeautifulSoup(my_html.text, 'html.parser')

items = soup.find_all("div", class_="j-item it-list-item")
data = []
for item in items:
    data.append(
        {
            "Название": item.find("div", class_="it-item-title c-shadow-overflow").find("a").get_text(strip=True),
            "Цена": item.find("div", class_="price-item").get_text(strip=True),
            "Город": item.find("div", class_="it-item-address c-shadow-overflow").get_text(strip=True),
            "Ссылка": item.find("div", class_="it-item-title c-shadow-overflow").find("a").get('href')
        }
    )


print(data)


images = soup.findAll('img', src=re.compile('.jpg'))
imgsrc = [img['src'] for img in images]
print(imgsrc)
