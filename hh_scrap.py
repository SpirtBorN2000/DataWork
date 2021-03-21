from bs4 import BeautifulSoup as bs
import requests
from pprint import pprint
import pandas as pd
bad_chars = ['\xa0']
sub = 'д'
sub2 = 'т'


def spliternormal(a):
    pay = a.split(' ')
    pay_amount = pay[0].split('-')
    currency = pay[1]
    min_pay = pay_amount[0]
    max_pay = pay_amount[1]
    return currency, min_pay, max_pay, pay_amount


def spliternot(a):
    pay = a.split(' ')
    prefix = pay[0]
    pay_amount = pay[1]
    currency = pay[2]
    return prefix, pay_amount, currency

main_link = 'https://hh.ru/'
goal = input("Введите должность:")
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36'}
vacancys = []
i = True
pagenumber = 0
while i == True:
    params = {'clusters': 'true', 'area': '1', 'L_is_autosearch': 'false', 'enable_snippets': 'true', 'text': goal,'page':pagenumber}
    response = requests.get(main_link + '/search/vacancy',params=params,headers=headers)
    if response.ok:
        soup = bs(response.text,'html.parser')
        vacancy_list = soup.findAll('div',{'class':'vacancy-serp-item'})
        try:
            target = soup.find('a',{'class':'bloko-button HH-Pager-Controls-Next HH-Pager-Control'}).getText()
        except Exception as e:
            target = "последняя страница"
        if target == "дальше":
            for vacancy in vacancy_list:
                vacancy_data = {}
                vacancy_name = vacancy.find('a').getText()
                try:
                    vacancy_pay = vacancy.find('span', {'data-qa': 'vacancy-serp__vacancy-compensation'}).getText()
                    vacancy_pay = "".join(r for r in vacancy_pay if r not in bad_chars)
                    if sub in vacancy_pay:
                        vacancy_data['max payment'] = spliternot(vacancy_pay)[1]
                        vacancy_data['currency'] = spliternot(vacancy_pay)[2]
                    if sub2 in vacancy_pay:
                        vacancy_data['min payment'] = spliternot(vacancy_pay)[1]
                        vacancy_data['currency'] = spliternot(vacancy_pay)[2]
                    else:
                        vacancy_data['min payment'] = spliternormal(vacancy_pay)[1]
                        vacancy_data['max payment'] = spliternormal(vacancy_pay)[2]
                        vacancy_data['currency'] = spliternormal(vacancy_pay)[0]
                except Exception as e:
                    vacancy_pay = None
                    vacancy_data['Payment discription'] = vacancy_pay
                vacancy_link = vacancy.find('a')['href']
                vacancy_site = response.url
                vacancy_data['link'] = vacancy_link
                vacancy_data['name'] = vacancy_name
                vacancy_data['url'] = main_link
                vacancys.append(vacancy_data)
            pagenumber = pagenumber + 1
        else:
            for vacancy in vacancy_list:
                vacancy_data = {}
                vacancy_name = vacancy.find('a').getText()
                try:
                    vacancy_pay = vacancy.find('span', {'data-qa': 'vacancy-serp__vacancy-compensation'}).getText()
                    vacancy_pay = "".join(r for r in vacancy_pay if r not in bad_chars)
                    if sub in vacancy_pay:
                        vacancy_data['max payment'] = spliternot(vacancy_pay)[1]
                        vacancy_data['currency'] = spliternot(vacancy_pay)[2]
                    if sub2 in vacancy_pay:
                        vacancy_data['min payment'] = spliternot(vacancy_pay)[1]
                        vacancy_data['currency'] = spliternot(vacancy_pay)[2]
                    else:
                        vacancy_data['min payment'] = spliternormal(vacancy_pay)[1]
                        vacancy_data['max payment'] = spliternormal(vacancy_pay)[2]
                        vacancy_data['currency'] = spliternormal(vacancy_pay)[0]
                except Exception as e:
                    vacancy_pay = None
                    vacancy_data['Payment discription'] = vacancy_pay
                vacancy_link = vacancy.find('a')['href']
                vacancy_site = response.url
                vacancy_data['link'] = vacancy_link
                vacancy_data['name'] = vacancy_name
                vacancy_data['url'] = main_link
                vacancys.append(vacancy_data)
            i = False

compression_opts = dict(method='zip',
                        archive_name='out.csv')
HH_DF = pd.DataFrame.from_dict(vacancys)
del HH_DF['Payment discription']
HH_DF.to_csv('out.zip', index=False,
          compression=compression_opts)