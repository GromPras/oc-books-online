import re
import requests
from bs4 import BeautifulSoup


def get_books_urls(url: str) -> list[str]:
    r = requests.get(url)
    products: list[str] = []

    if r.ok:
        soup = BeautifulSoup(r.text, features="html.parser")
        product_pods = soup.findAll("article", class_="product_pod")
        products = [p.h3.a["href"][9:] for p in product_pods]

    return products


def get_category_page_number(url: str) -> int:
    r = requests.get(url)
    if r.ok:
        soup = BeautifulSoup(r.text, features="html.parser")
        pager = soup.find("li", class_="current")
        if pager:
            max_page = re.findall(r"\d+", pager.text.strip())[1]
            return int(max_page)
        return 1
    return 0
