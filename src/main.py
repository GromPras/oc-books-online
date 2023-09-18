import csv
from book_scrap import scrap_a_book
from category_scrap import get_books_urls

category_url = (
    "https://books.toscrape.com/catalogue/category/books/travel_2/index.html"
)

books_urls = get_books_urls(url=category_url)
books = []

for link in books_urls:
    book = scrap_a_book(url="https://books.toscrape.com/catalogue/" + link)
    books.append(book)

with open("books-data/category.csv", "w", newline="") as csvfile:
    fieldnames = list(books[0])
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    for book in books:
        writer.writerow(book)
