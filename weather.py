import requests
from bs4 import BeautifulSoup

class Weather:
    # Ссылка на страницу для последующего парсинга
    page_sinop= 'https://sinoptik.com.ru'
    # Для того чтобы гугл не воспринимал нас, как робота
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36 OPR/73.0.3856.438'}

    def GetWeather(page, headers):
        full_page = requests.get(page, headers=headers)
        soup = BeautifulSoup(full_page.content, 'html.parser')
        convert = soup.findAll("div", {"class": "weather__article_description-text"})  # Ищем в html разметке нужные теги

        min = soup.findAll("div", {"class": "weather__article_description-text"})# нужно доделать парсинг с температурой
        max = soup.findAll("div", {"class": "weather__article_description-text"})

        value = "Погода на сегодня:/n Мин: " +  " Макс: " + "/n" + convert[0].text
        return value
