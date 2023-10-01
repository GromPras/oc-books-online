import re
import requests
import shutil
import os
from bs4 import BeautifulSoup
from custom_types.book import Book


def scrap_a_book(url: str) -> Book:
    """A function that takes a book url as parameter and
    returns a dictionary of the book's data
    It also downloads the book's cover image
    and store it in the corresponding category's directory

    Keyword arguments:
    url: str -- the book's page url
    """

    # prepare book's data as a dict
    book_infos: Book = {
        "product_page_url": url,
        "universal_product_code": "",
        "title": "",
        "price_including_tax": "",
        "price_excluding_tax": "",
        "number_available": "",
        "product_description": "",
        "category": "",
        "review_rating": "",
        "image_url": "",
    }
    # converts classes to a [1:5] note
    rating_map = {
        "One": "1",
        "Two": "2",
        "Three": "3",
        "Four": "4",
        "Five": "5",
    }

    r = requests.get(url)
    if r.ok:
        # Extract data from the response html
        r.encoding = "utf-8"
        soup = BeautifulSoup(r.text, features="html.parser")
        table = soup.find_all("td")

        # Gets a list of the breadcrumbs, filtering out empty lines
        breadcrumbs = list(
            filter(
                lambda i: i != "\n",
                soup.find("ul", class_="breadcrumb").contents,
            )
        )
        category = breadcrumbs[2].text.strip() if not None else "NC"
        rating = soup.find("p", class_="star-rating") if not None else "NC"
        image = soup.find("img") if not None else "NC"
        image_source = image["src"][6:] if image != "NC" else "NC"

        book_infos["upc"] = table[0].text if not None else "NC"
        book_infos["title"] = soup.find("h1").text if not None else "NC"
        book_infos["price_including_tax"] = table[3].text if not None else "NC"
        book_infos["price_excluding_tax"] = table[2].text if not None else "NC"
        book_infos["number_available"] = (
            re.findall(r"\d+", table[5].text)[0] if not None else "NC"
        )

        # Get the book's description if it exists
        if soup.find("div", id="product_description"):
            book_infos["product_description"] = (
                soup.find("div", id="product_description").find_next("p").text
                if not None
                else "NC"
            )
        book_infos["category"] = category

        # Convert class rating
        book_infos["review_rating"] = (
            rating_map[rating["class"][1]] if rating != "NC" else "NC"
        )
        book_infos["image_url"] = (
            f"https://books.toscrape.com/{image_source}"
            if image_source != "NC"
            else "NC"
        )

        if image and category and book_infos["title"] != "NC":
            get_image(
                book_infos["image_url"],
                book_infos["category"],
                book_infos["title"],
            )
    else:
        print("[ERROR]: {r.status_code}")
    return book_infos


def get_image(image_url: str, book_category: str, book_title: str) -> None:
    """Save the book's cover in folders sorted by categories

    Keyword arguments:
    image_url: str -- the image url
    book_category: str -- the book's category
    book_title: str -- the book's title
    """
    res = requests.get(image_url, stream=True)
    if res.ok:
        image_dir = (
            f"./books-data/images/{book_category.lower().replace(' ', '_')}"
        )

        # Make sure the folder exists before saving the file
        if not os.path.exists(image_dir):
            os.makedirs(image_dir)

        # Format the title
        img_title = (
            book_title.lower()
            .replace(" ", "-")
            .replace("'", "")
            .replace(":", "")
            .replace(".", "")
            .replace(",", "")
            .replace("/", "-")
        )
        image_path = f"{image_dir}/{img_title}.jpg"

        # download the file if it does not exists
        if not os.path.exists(image_path):
            with open(image_path, "wb") as f:
                shutil.copyfileobj(res.raw, f)
    else:
        print("[ERROR]: Could not find image for " + book_title)
