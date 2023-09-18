import csv
from category_scrap import get_categories, scrap_category


categories: list = get_categories("https://books.toscrape.com/index.html")
books = []

for category in categories:
    print(category["name"])
    category_books = scrap_category(category["url"])
    with open(
        f"books-data/{category['name'].lower()}.csv", "w", newline=""
    ) as csvfile:
        fieldnames = list(category_books[0])
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for book in category_books:
            writer.writerow(book)
        print(str(len(category_books)) + " books written")
