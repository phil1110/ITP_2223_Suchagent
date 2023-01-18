from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
from html.parser import HTMLParser

products = []
prices = []
locations = []

link = input("Enter a Link: ")

driver = webdriver.Chrome()
driver.get(link)

content = driver.page_source
soup = BeautifulSoup(content, 'html.parser')

for a in soup.findAll('div', attrs={'class': 'info'}):
    try:
        name = a.findNext('h2', attrs={'class': 'title'}).getText()
        price = a.findNext('span', attrs={'class': 'euro'}).getText()
        location = ""
        #a.findNext('span', attrs={'class': 'mobile-inline'}).getText()

        # Änderung! Nicht im jeden Eintrag ist ein Ort zu finde und gibt somit Error
        try:
            location = a.findNext('span', attrs={'class': 'mobile.inline'}).getText()

        except:
            location = "n/a"

        name = name.strip()
        price = price.strip()
        price = price.replace('.', '')
        price = price.replace(',', '.')
        price = float(price)
        location = location.strip()

        print(name, price, location)

        if not products.__contains__(name):
            products.append(name)
            prices.append(price)
            locations.append(location)

    except:
        print("failed")

driver.close()

df = pd.DataFrame({'Product Name': products, 'Price': prices, 'Location': locations})
df.to_csv('products.csv', index=False, encoding='utf-8')