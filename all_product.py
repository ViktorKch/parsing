from bs4 import BeautifulSoup as bs
from urllib.request import *
import csv
import pandas as pd

url = 'http://www.tlock.ru/catalog/bronenakladki_i_plastiny/filter/producer-is-armadillo-or-fuaro-or-punto/apply/'
union = []
d= {}
report = []



def get_html(url):
    req = Request(url)
    html = urlopen(req).read()
    return html

def bronenakladki_parser(x=0):
    opener = build_opener()
    opener.addheaders = [('User-Agent', 'Mozilla/5.0')]
    install_opener(opener)
    html = get_html(url)
    soup = bs(html, 'html.parser')
    list = soup.find_all('a', class_='prod__link block-link clearfix')
    for a in list:
        x += 1
        product_link = get_html('http://www.tlock.ru' + a['href'])
        product_soup = bs(product_link, 'html.parser')
        product_title = ''.join((product_soup.find('h1')).contents)
        product_description = product_soup.find('div', attrs={'id': 'description'}).contents[0]
        product_characteristics = product_soup.find_all('table', class_='char table_1 table')
        d['id'] = x
        d['Название'] = product_title
        d['Описание'] = product_description
        for product_property in product_characteristics:
            union.extend(product_property.contents[1::2])
            for i in range(len(union)):
                d[''.join(union[i].contents[1].contents)] = ''.join(union[i].contents[3].contents)
        report.append(d.copy())


    return report


goods = bronenakladki_parser()

pd.DataFrame(goods).to_csv('out.csv', index=False, encoding='utf-8')
#cp1251
