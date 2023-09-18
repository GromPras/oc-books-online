import csv
from book_scrap import scrap_a_book
from category_scrap import get_books_urls, get_category_page_number

category_url = "https://books.toscrape.com/catalogue/category/books/mystery_3"

page_number: int = get_category_page_number(url=category_url)

books = []
if page_number > 1:
    for i in range(page_number):
        page_url = f"{category_url}/page-{i + 1}.html"
        books_urls = get_books_urls(url=page_url)

        for link in books_urls:
            book = scrap_a_book(
                url="https://books.toscrape.com/catalogue/" + link
            )
            books.append(book)
elif page_number == 1:
    books_urls = get_books_urls(url=category_url + "/index.html")

    for link in books_urls:
        book = scrap_a_book(url="https://books.toscrape.com/catalogue/" + link)
        books.append(book)
else:
    print("Invalid url")

with open("books-data/category.csv", "w", newline="") as csvfile:
    fieldnames = list(books[0])
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    for book in books:
        writer.writerow(book)
