from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
from html.parser import HTMLParser
from datetime import datetime
from datetime import date
from lib.cleaner import cleaner


class Webscraper:
    products = []
    prices = []
    locations = []

    def __init__(self, link):
        self.url = link

    def run(self):
        soup = BeautifulSoup(self.__getContent(), 'html.parser')

        self.__fillLists(soup)

        self.__writeResults()



    def __getContent(self):
        driver = webdriver.Chrome()
        driver.get(self.url)
        content = driver.page_source
        driver.close()
        return content

    def __fillLists(self, soup):
        for a in soup.findAll('div', attrs={'class': 'info'}):
            try:
                name = a.findNext('h2', attrs={'class': 'title'}).getText()
                price = a.findNext('span', attrs={'class': 'euro'}).getText()
                location = a.findNext('span', attrs={'class': 'mobile-inline'}).getText()

                name = name.strip()
                price = price.strip()
                price = price.replace('.', '')
                price = price.replace(',', '.')
                price = float(price)
                location = location.strip()

                print(name, price, location)

                self.__appendItems(name, price, location)

            except:
                print("failed")

    def __writeResults(self):
        filename = f'Webscraper/results/{date.today().strftime("%Y_%m_%d")}_at_{datetime.now().strftime("%H_%M_%S")}.json'
        df = pd.DataFrame({'Product Name': self.products, 'Price': self.prices, 'Location': self.locations})
        df.to_json(filename)
        print(df)

        cl = cleaner
        cl.run(cl)

    def __appendItems(self, name, price, location):
        if not self.products.__contains__(name):
            self.products.append(name)
            self.prices.append(price)
            self.locations.append(location)