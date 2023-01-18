from lib import webscraper as w
import pandas as pd

#
#link = input("Enter a link: ")
#scraper = w.Webscraper(link)
#
#scraper.run()

class Scraper:
    def __init__(self, link):
        self.scraper = w.Webscraper(link)

    def scrape(self):
        return self.scraper.run()

        
        