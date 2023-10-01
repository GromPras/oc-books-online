import csv
from category_scrap import get_categories, scrap_category
from custom_types.book import Book


# Get the categories urls to scrap
categories: list = get_categories("https://books.toscrape.com/index.html")

books = list[Book]

# Loop through the categories url and extract data
for index, category in enumerate(categories):
    percentage = round((int(index) / len(categories)) * 100)
    print(f"Extracting: {category['name']}")

    category_books = scrap_category(category["url"])

    # Write books's data in a csv fil named after the current category
    with open(
        f"books-data/{category['name'].lower().replace(' ', '_')}.csv",
        "w",
        newline="",
    ) as csvfile:
        fieldnames = list(category_books[0])
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for book in category_books:
            writer.writerow(book)
        print(str(len(category_books)) + " books written")
