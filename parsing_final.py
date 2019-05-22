from bs4 import BeautifulSoup
from urllib.request import *
import csv

url = "http://www.tlock.ru/catalog/zamki_vreznye/dlya_legkikh_dverey/"
union = []
d = {}
report = []

def get_html(url):
    req = Request(url)
    html = urlopen(req).read()
    return html

def good_parser():
    opener = build_opener()
    opener.addheaders = [('User-Agent', 'Mozilla/5.0')]
    install_opener(opener)
    html = get_html(url)
    soup = BeautifulSoup(html, 'html.parser')
    list = soup.find_all(class_='prod__link block-link clearfix')
    for a in list:
        product_link = 'http://www.tlock.ru' + a['href']
        print(product_link)
        table_html = get_html(product_link)
        table_soup = BeautifulSoup(table_html, 'html.parser')
        divs = table_soup.find_all('table', class_='char table_1 table')
        title = table_soup.find('h1')
        title_1 = ''.join(title.contents)
        descriptions = table_soup.find_all('div', attrs={'id': 'description'})
        for description in descriptions:
            decr = description.contents
        for div in divs:
            sum = div.contents
            union.extend(sum[1::2])
        for i in range(len(union)):
            d[''.join(union[i].contents[1].contents)] = ''.join(union[i].contents[3].contents)

        d['Название'] = title_1
        d['Описание'] = decr[0]


        report.append(d.copy())


    return report





def goods_writer(d):
    with open('goods.csv', 'a') as file:
        a_pen = csv.writer(file)
        a_pen.writerow(('Название', 'Описание', 'Производитель', 'Страна', 'Вес', 'Гарантия', 'Бэксет (удаление ключевого отверстия)', 'Вылет ригеля', 'Диаметр ригеля', 'Длина ключа', 'Класс безопасности', 'Количество ключей', 'Количество комбинаций', 'Количество ригелей', 'Комплектация ручкой', 'Комплектация цилиндром', 'Материал ключа', 'Материал ручки', 'Материал цилиндра', 'Межосевое расстояние', 'Наличие лицевой планки', 'Отверстие под броню', 'Отверстия под стяжки', 'Тип замка', 'Тип механизма секретности', 'Тип упаковки', 'Цвет'))
        for d1 in d:
            try:
                a_pen.writerow((d1['Название'],d1['Описание'],d1['Производитель'],d1['Страна'],d1['Вес'],d1['Гарантия'],d1['Бэксет (удаление ключевого отверстия)'],d1['Вылет ригеля'],d1['Диаметр ригеля'],d1['Длина ключа'],d1['Класс безопасности'],d1['Количество ключей'],d1['Количество комбинаций'],d1['Количество ригелей'],d1['Комплектация ручкой'],d1['Комплектация цилиндром'],d1['Материал ключа'],d1['Материал ручки'],d1['Материал цилиндра'],d1['Межосевое расстояние'],d1['Наличие лицевой планки'],d1['Отверстие под броню'],d1['Отверстия под стяжки'],d1['Тип замка'],d1['Тип механизма секретности'],d1['Тип упаковки'],d1['Цвет']))
            except:
                pass


goods = good_parser()
goods_writer(goods)


