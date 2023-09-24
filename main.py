#https://en.wikipedia.org/wiki/Doughnut

import requests;
from bs4 import BeautifulSoup

def get_page(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content,  "html.parser")

    tag = soup.find_all("a")

    for t in tag:
        url2 = t.get("href")
        print(url2)


get_page(input("Url to scrape: "))