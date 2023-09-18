# import csv
from book_scrap import scrap_a_book
from category_scrap import get_books_urls

category_url = (
    "https://books.toscrape.com/catalogue/category/books/travel_2/index.html"
)

books_urls = get_books_urls(url=category_url)
print(books_urls)

# with open("books-data/category.csv", "w", newline="") as csvfile:
#     fieldnames = list(book_data)
#     writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

#     writer.writeheader()
#     writer.writerow(book_data)
