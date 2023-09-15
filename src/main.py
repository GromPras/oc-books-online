import re
import requests
from bs4 import BeautifulSoup

url = "https://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html"
book_infos = {
    "product_page_url": url,
    "upc": "",
    "title": "",
    "price_including_tax": "",
    "price_excluding_tax": "",
    "number_available": "",
    "product_description": "",
    "category": "",
    "review_rating": "",
    "image_url": "",
}

rating_map = {"One": "1", "Two": "2", "Three": "3", "Four": "4", "Five": "5"}

r = requests.get(url)
if r.ok:
    soup = BeautifulSoup(r.text, features="html.parser")
    table = soup.find_all("td")
    breadcrumbs = list(
        filter(lambda i: i != "\n", soup.find("ul", class_="breadcrumb").contents)
    )
    category = breadcrumbs[2].text.strip()
    rating = soup.find("p", class_="star-rating")
    image_source = list(
        filter(lambda i: i != "\n", soup.find("div", class_="item active").contents)
    )

    book_infos["upc"] = table[0].text
    book_infos["title"] = soup.find("h1").text
    book_infos["price_including_tax"] = table[3].text
    book_infos["price_excluding_tax"] = table[2].text
    book_infos["number_available"] = re.findall(r"\d+", table[5].text)[0]
    book_infos["product_description"] = (
        soup.find("div", id="product_description").find_next("p").text
    )
    book_infos["category"] = category
    book_infos["review_rating"] = rating_map[rating["class"][1]]
    book_infos["image_url"] = "https://books.toscrape.com/" + image_source[0]["src"][6:]

    print(book_infos)
