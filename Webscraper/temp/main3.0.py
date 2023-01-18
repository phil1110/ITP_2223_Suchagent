# Web Scraper Teilbereich
# Filtert alle Links der Website

from bs4 import BeautifulSoup
import requests

# Links zum Testen
# https://www.bazar.at/l/07-immobilien/c
# https://www.bazar.at/l/05-kindersachen/c

URL = "https://www.bazar.at/l/05-kindersachen/c"
page = requests.get(URL)
soup = BeautifulSoup(page.content, "html.parser")
for a_href in soup.find_all("a", href=True):
    if 'h' != a_href["href"][0]:
        print("https://www.bazar.at"+a_href["href"])
    else:
        print(a_href["href"])


