import re
import requests
from bs4 import BeautifulSoup
from book_scrap import scrap_a_book
from types.book import Book


def get_books_urls(category_url: str) -> list[str]:
    """
    Retrieves a list of book's urls from the category page

    Keyword arguments:
    category_url: str -- the category's url
    """
    r = requests.get(category_url)
    books: list[str] = []

    if r.ok:
        soup = BeautifulSoup(r.text, features="html.parser")
        product_pods = soup.findAll("article", class_="product_pod")
        books = [p.h3.a["href"][9:] for p in product_pods]

    return books


def get_category_page_number(category_url: str) -> int:
    """
    Get the last possible page number for a given category

    Keyword arguments:
    category_url: str -- the category's url
    """
    r = requests.get(category_url)
    if r.ok:
        soup = BeautifulSoup(r.text, features="html.parser")
        pager = soup.find("li", class_="current")
        if pager:
            max_page = re.findall(r"\d+", pager.text.strip())[1]
            return int(max_page)
        return 1
    return 0


def get_categories(home_url: str) -> list[dict[str, str]] | list:
    """
    Retrieves the list of categories from the website's home page

    Keyword arguments:
    home_url: str -- the website's url
    """
    r = requests.get(home_url)
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


def scrap_category(category_url: str) -> list[Book]:
    """
    Retrieves the book's url from a given category by going through each of
    its pages and then extract the books's data from their url

    Keyword arguments:
    category_url: str -- the category's url
    """

    # format the url to prepare for multiple pages
    formated_url = category_url[:-10]

    # get the last page number for this category
    page_number: int = get_category_page_number(category_url=category_url)

    books: list[Book] = []

    # going through multiple pages
    if page_number > 1:
        for i in range(page_number):
            # adding 1 to i because of how range() works
            page_url = f"{formated_url}page-{i + 1}.html"
            books_urls = get_books_urls(category_url=page_url)

            for link in books_urls:
                book = scrap_a_book(
                    url="https://books.toscrape.com/catalogue/" + link
                )
                books.append(book)
    # scrapping only one page
    elif page_number == 1:
        books_urls = get_books_urls(category_url=formated_url + "index.html")

        for link in books_urls:
            book = scrap_a_book(
                url="https://books.toscrape.com/catalogue/" + link
            )
            books.append(book)
    else:
        print("Invalid url")

    return books
