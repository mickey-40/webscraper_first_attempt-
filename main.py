from bs4 import BeautifulSoup
import requests
import csv

page_to_scrap = requests.get("http://quotes.toscrape.com")
soup = BeautifulSoup(page_to_scrap.text, "html.parser")
quotes = soup.findAll("span", attrs={"class":"text"})
authors = soup.findAll("small", attrs={"class":"author"})

file = open("scraped_quotes.csv", "w")
writer.writerow(["Quotes", "Authors"])

for quote, author in zip(quotes, authors):
  print(quote.text + " - " + author.text)
  writer.writerow([quote.text, author.text])

file.close()

