from bs4 import BeautifulSoup as bs
from urllib.request import *
import csv
import pandas as pd

url = 'http://www.tlock.ru/catalog/bronenakladki_i_plastiny/filter/producer-is-armadillo-or-fuaro-or-punto/apply/'




def get_html(url):
    req = Request(url)
    html = urlopen(req).read()
    return html

def bronenakladki_parser():
    opener = build_opener()
    opener.addheaders = [('User-Agent', 'Mozilla/5.0')]
    install_opener(opener)
    html = get_html(url)
    soup = bs(html, 'html.parser')
    list = soup.find_all('a', class_='prod__link block-link clearfix')
    for a in list:
        product_link = get_html('http://www.tlock.ru' + a['href'])
        product_soup = bs(product_link, 'html.parser')
        images = product_soup.find_all('div', class_='prod-thumbs__thumb')
        for image in images:
            img_url = image.contents[1]["src"].split('/')[-1]
            number_of_photos = int(image.contents[1]["src"].split('/')[-1][-5])
            image_name = image.contents[1]['alt']
            if number_of_photos == 1:
                urlretrieve('http://www.tlock.ru/photo_bank/' + img_url, image_name.replace('/', '').strip() + '.jpeg')
            else:
                urlretrieve('http://www.tlock.ru/photo_bank/' + img_url, image_name.replace('/', '').strip() + str(number_of_photos) + '.jpeg')
            print(image_name + ': скачан')


bronenakladki_parser()
#http://www.tlock.ru/photo_bank/
