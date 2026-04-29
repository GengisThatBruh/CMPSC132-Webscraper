import requests
from bs4 import BeautifulSoup

url = "https://webscraper.io/test-sites/e-commerce/static/computers/laptops"

def get_html(url): # checks if url is valid or can be scraped, also parses html 
    try:
        page = requests.get(url, timeout=10)
        page.raise_for_status()
        return BeautifulSoup(page.text, "html.parser")
    except requests.exceptions.MissingSchema:
        print("Invalid URL. Make sure it starts with http:// or https://")
        exit()
    except requests.exceptions.ConnectionError:
        print("Could not connect. Check your internet or the URL.")
        exit()
    except requests.exceptions.HTTPError:
        print(f"HTTP error: {page.status_code}")
        exit()
    except requests.exceptions.Timeout:
        print("Request timed out.")
        exit()

def get_name(card): # parses through html to print out laptop name
    try:
        return " ".join(card.find("a", class_="title").text.split())
    except AttributeError:
        return "N/A"

def get_price(card): # parses through html to print out price
    try:
        return card.find("span", itemprop="price").text.strip()
    except AttributeError:
        return "N/A"
    
def display(name, price, rating): # print formatted strings from previous returns
    print(f"Laptop: {name}")
    print(f"Price: {price}")
    print(f"Rating: {rating}")
    print("-" * 30) 

def scrape_laptops(url): # appends all laptops into a list, calls get functions
    htmlparsed = get_html(url)
    cards = htmlparsed.find_all("div", class_="card-body")
    laptops = []
    for card in cards:
        name = get_name(card)
        price = get_price(card)
        laptops.append({"name": name, "price": price})
    return laptops


url = input("Enter URL: ")
laptops = scrape_laptops(url) # calls display for each laptop in list
for laptop in laptops:
    display(laptop["name"], laptop["price"], laptop["rating"])




