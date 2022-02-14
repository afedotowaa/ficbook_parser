from bs4 import BeautifulSoup
import requests
import sys
import re


russian = re.compile("[а-яА-Я]+")
sys.stdout = open('ficwriters.txt', 'w')

for user in range(1, 10):
    url = 'https://fanfics.me/user' + str(user) + '/fics'
    print(url)
    # получаем html код страницы
    request = requests.get(url)
    # парсим его с помощью BeautifulSoup
    soup = BeautifulSoup(request.content, 'lxml')
    if 'Работы' not in str(soup.find('li', class_='activ2')):
        continue
    else:
        for fic in soup.find_all('div', class_='ContentTable_Half')[-1]:
            if 'фанфик' in fic:
                print(url, fic.strip())
