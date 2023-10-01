from typing import TypedDict


class Book(TypedDict):
    product_page_url: str
    universal_product_code: str
    title: str
    price_including_tax: str
    price_excluding_tax: str
    number_available: str
    product_description: str
    category: str
    review_rating: str
    image_url: str
