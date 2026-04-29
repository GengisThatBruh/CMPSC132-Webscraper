import requests
from bs4 import BeautifulSoup

url = "https://webscraper.io/test-sites/e-commerce/static/computers/laptops"

def get_html(url): # gets url and parses html
    page = requests.get(url)
    return BeautifulSoup(page.text, "html.parser")





