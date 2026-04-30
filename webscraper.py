import requests
from bs4 import BeautifulSoup

# Step 1: Send request and parse HTML
def get_html(url):
    page = requests.get(url)
    return BeautifulSoup(page.text, "html.parser")

# Step 2: Extract laptop name
def get_name(card):
    try:
        return " ".join(card.find("a", class_="title").text.split())
    except AttributeError:
        return "N/A"

# Step 3: Extract laptop price
def get_price(card):
    try:
        return card.find("span", itemprop="price").text.strip()
    except AttributeError:
        return "N/A"

# Step 4: Extract laptop rating
def get_rating(card):
    try:
        return card.find("span", class_="ratings").get("data-rating")
    except AttributeError:
        return "N/A"

# Step 5: Display laptop info
def display(name, price, rating):
    print(f"Laptop: {name}")
    print(f"Price: {price}")
    print(f"Rating: {rating}")
    print("-" * 30)

# Step 6: Scrape all laptops and store in a list
def scrape_laptops(url):
    htmlparsed = get_html(url)
    cards = htmlparsed.find_all("div", class_="card-body")
    laptops = []
    for card in cards:
        name = get_name(card)
        price = get_price(card)
        rating = get_rating(card)
        laptops.append({"name": name, "price": price, "rating": rating})
    return laptops

# Main
url = input("Enter URL: ")
laptops = scrape_laptops(url)
for laptop in laptops:
    display(laptop["name"], laptop["price"], laptop["rating"])