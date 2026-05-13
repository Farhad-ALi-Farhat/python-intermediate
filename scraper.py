import requests
from bs4 import BeautifulSoup

URL = "https://quotes.toscrape.com/"

def scrape_quotes():
    response = requests.get(URL)
    soup = BeautifulSoup(response.text, "html.parser")

    quotes = soup.find_all("span", class_="text")

    for i, quote in enumerate(quotes, 1):
        print(f"{i}. {quote.text}")

if __name__ == "__main__":
    scrape_quotes()
