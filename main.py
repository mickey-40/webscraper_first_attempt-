import csv
import requests
from bs4 import BeautifulSoup

# Fetch the webpage
page_to_scrap = requests.get("http://quotes.toscrape.com")
soup = BeautifulSoup(page_to_scrap.text, "html.parser")

# Find the quotes and authors
quotes = soup.findAll("span", attrs={"class": "text"})
authors = soup.findAll("small", attrs={"class": "author"})

# Open the file in write mode and create a CSV writer instance
with open("scraped_quotes.csv", "w", newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(["Quotes", "Authors"])  # Write the header

    # Loop through the quotes and authors and write them to the CSV file
    for quote, author in zip(quotes, authors):
        print(quote.text + " - " + author.text)
        writer.writerow([quote.text, author.text])
