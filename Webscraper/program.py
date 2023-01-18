from lib import webscraper as w

link = input("Enter a link: ")
scraper = w.Webscraper(link)

scraper.run()
