import requests
import sys
import re

from bs4 import BeautifulSoup


russian = re.compile("[а-яА-Я]+")
sys.stdout = open('ficwriters.txt', 'w')


for user in range(1, 200):
    url = 'https://fanfics.me/user' + str(user) + '/fics'
    # получаем html код страницы
    request = requests.get(url)
    # парсим его с помощью BeautifulSoup
    soup = BeautifulSoup(request.content, 'lxml')
    if 'Работы' not in str(soup.find('li', class_='activ2')):
        continue
    else:
        for fic in soup.find_all('div', class_='ContentTable_Half')[-1]:
            if 'фанфик' in fic:
                print(url)
                # print(fic.strip())

