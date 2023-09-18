import csv
from book_scrap import scrap_a_book

url = "https://books.toscrape.com/catalogue/tipping-the-velvet_999/index.html"

book_data = scrap_a_book(url=url)

with open("books-data/category.csv", "w", newline="") as csvfile:
    fieldnames = list(book_data)
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerow(book_data)
