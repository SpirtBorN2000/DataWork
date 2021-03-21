import requests
from lxml import html
from pprint import pprint
import datetime
from pymongo import MongoClient

# Лента

main_link = "https://lenta.ru"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/89.0.4389.90 Safari/537.36"}
response = requests.get(main_link, headers=headers)
dom = html.fromstring(response.text)
news_list_lenta0 = dom.xpath(
    '//section[contains(@class,"row b-top7-for-main js-top-seven")]/div/div[contains(@class,"item")]')
news_list_lenta1 = dom.xpath('//section[contains(@class,"row b-top7-for-main js-top-seven")]/div[1]/div[1]')
list_of_all_news = []
bad_chars = ['\xa0']
for news in news_list_lenta0:
    news_data = {}
    name_news = ''.join(news.xpath('./a/text()'))
    link_news = ''.join(news.xpath('./a/@href '))
    date_news = ''.join(news.xpath('./a/time/@datetime'))

    news_data['Name_of_news'] = name_news.replace(u'\xa0', ' ')
    news_data['link_of_news'] = main_link + link_news
    news_data['date_of_news'] = date_news
    news_data['website'] = main_link
    list_of_all_news.append(news_data)
del list_of_all_news[0]
news_data = {}  # Отдельное добавление труднодоступной записи
name_news = ''.join(
    dom.xpath('//section[contains(@class,"row b-top7-for-main js-top-seven")]/div[1]/div[1]/h2/a/text()'))
link_news = ''.join(
    dom.xpath('//section[contains(@class,"row b-top7-for-main js-top-seven")]/div[1]/div[1]/h2/a/@href'))
date_news = ''.join(
    dom.xpath('//section[contains(@class,"row b-top7-for-main js-top-seven")]/div[1]/div[1]/h2/a/time/@datetime'))
news_data['Name_of_news'] = name_news.replace(u'\xa0', ' ')
news_data['link_of_news'] = main_link + link_news
news_data['date_of_news'] = date_news
news_data['website'] = main_link
list_of_all_news.insert(0, news_data)

# Яндекс новости

main_link = "https://yandex.ru/news/"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/89.0.4389.90 Safari/537.36"}
response = requests.get(main_link, headers=headers)
dom = html.fromstring(response.text)
news_list_yandex = dom.xpath(
    '//div[contains(@class,"mg-grid__row mg-grid__row_gap_8 news-top-flexible-stories news-app__top")]/div[contains('
    '@class,"mg-grid__col")]')
for news in news_list_yandex:
    news_data = {}
    name_news = ''.join(news.xpath('.//h2/text()'))
    link_news = ''.join(news.xpath('.//a[contains(@class,"mg-card__link")]/@href'))
    date_news = ''.join(news.xpath('.//span[contains(@class,"mg-card-source__time")]/text()'))
    website = ''.join(news.xpath('.//a[contains(@class,"mg-card__source-link")]/text()'))
    news_data['Name_of_news'] = name_news.replace(u'\xa0', ' ')
    news_data['link_of_news'] = link_news
    now = datetime.datetime.today().strftime('%d/%m/%Y')
    news_data['date_of_news'] = date_news + ' ' + now
    news_data['website'] = website
    list_of_all_news.append(news_data)

# Мейл новости
mail_list = []
main_link = 'https://news.mail.ru'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/89.0.4389.90 Safari/537.36'}
response = requests.get(main_link, headers=headers)
dom = html.fromstring(response.text)
news_list_mail = dom.xpath('//div[@class="js-module"]//a/@href')
links_list = []
for link in news_list_mail:
    # news_dict = link
    # links_list.append(news_dict)
    links_list.append(link)
for news_link in links_list:
    response_news = requests.get(news_link, headers=headers)
    dom2 = html.fromstring(response_news.text)
    container = dom2.xpath('//div[contains(@class,"article ")]')
    for news in container:
        news_data = {}
        name_news = ''.join(news.xpath('.//span[@class="hdr__text"]/h1[@class="hdr__inner"]/text()'))
        date_news = ''.join(news.xpath('.//div[contains(@class,"breadcrumbs")]//span[@class="note"]//@datetime'))
        website = ''.join(news.xpath('//div[contains(@class,"breadcrumbs")]//span[@class="link__text"]/text()'))
        news_data['link_of_news'] = news_link
        news_data['Name_of_news'] = name_news.replace(u'\xa0', ' ')
        news_data['date_of_news'] = date_news
        news_data['website'] = website
        list_of_all_news.append(news_data)
        break
pprint(list_of_all_news)

# client = MongoClient('localhost', 27017)
# db = client['NewsData']
# news = db.news
# news.insert_many(list_of_all_news)
