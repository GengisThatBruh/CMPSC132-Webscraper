import requests
from bs4 import BeautifulSoup

url = "https://webscraper.io/test-sites/e-commerce/static/computers/laptops"

def get_html(url): # gets url and parses html
    page = requests.get(url)
    return BeautifulSoup(page.text, "html.parser")

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




