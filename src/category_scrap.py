import requests
from bs4 import BeautifulSoup


def get_books_urls(url: str) -> list[str]:
    r = requests.get(url)
    products = []

    if r.ok:
        soup = BeautifulSoup(r.text, features="html.parser")
        product_pods = soup.findAll("article", class_="product_pod")
        products = [p.h3.a["href"][9:] for p in product_pods]

    return products
