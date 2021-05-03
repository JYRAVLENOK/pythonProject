import requests
from bs4 import BeautifulSoup

class Rates:
    #Ссылка на страницу для последующего парсинга
    DOLLAR_RUB = 'https://www.google.com/search?client=opera-gx&q=rehc+ljkkfhf&sourceid=opera&ie=UTF-8&oe=UTF-8'
    #Для того чтобы гугл не воспринимал нас, как робота
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36 OPR/73.0.3856.438'}

    def GetRate(page, headers):
        full_page = requests.get(page, headers=headers)
        soup = BeautifulSoup(full_page.content, 'html.parser')
        convert = soup.findAll("span", {"class": "Dflfde", "class": "SwHCTb", "data-precision": 2}) #Ищем в html разметке нужные теги
        value = "Один доллар США равен " + convert[0].text + " рублей"
        return (value)

