from urllib.parse import urljoin

import requests
from bs4 import BeautifulSoup
from urllib import *

visited_urls = set()

def spider_urls(url, keyword):
    try:
        response = requests.get(url)

    except:
        print(f"Request failed {url}")
        return

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, "html.parser")

        a_tag = soup.find_all("a")
        urls = []
        for tag in a_tag:
            href = tag.get("href")
            if href is not None and href != "":
                urls.append(href)
        #print(urls)

        for single_url in urls:
            if single_url not in visited_urls:
                visited_urls.add(single_url)
                url_join = urljoin(url, single_url)
                if keyword in url_join:
                    print(url_join)
                    spider_urls(url_join,keyword)
            else:
                pass

url = input("URL to scrape: ")
keyword = input("Keyword to search for: ")
spider_urls(url, keyword)

#https://www.yahoo.com

