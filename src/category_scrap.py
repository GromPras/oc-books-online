import re
import requests
from bs4 import BeautifulSoup
from book_scrap import scrap_a_book


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


def get_categories(url: str) -> list[dict[str, str]] | list:
    r = requests.get(url)
    if r.ok:
        soup = BeautifulSoup(r.text, features="html.parser")
        nav = soup.find("div", class_="side_categories")
        categories = []
        for i in nav.findAll("li"):
            category = {
                "name": i.a.text.strip(),
                "url": "https://books.toscrape.com/" + i.a["href"],
            }
            categories.append(category)
        categories.pop(0)
        return categories
    return []


def scrap_category(url: str) -> list[dict[str, str]]:
    category_url = url[:-10]

    page_number: int = get_category_page_number(url=url)

    books = []
    if page_number > 1:
        for i in range(page_number):
            page_url = f"{category_url}page-{i + 1}.html"
            books_urls = get_books_urls(url=page_url)

            for link in books_urls:
                book = scrap_a_book(
                    url="https://books.toscrape.com/catalogue/" + link
                )
                books.append(book)
    elif page_number == 1:
        books_urls = get_books_urls(url=category_url + "index.html")

        for link in books_urls:
            book = scrap_a_book(
                url="https://books.toscrape.com/catalogue/" + link
            )
            books.append(book)
    else:
        print("Invalid url")

    return books
