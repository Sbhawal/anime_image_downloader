import requests
from bs4 import BeautifulSoup

from src.site_support import *
from src.utilities.constants import sites


def read_url(url):
    """Reads a url and returns the html"""
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    return soup


def parse_url(url):
    if sites[0] in url:
        scrape_konachan(url)
    elif sites[1] in url:
        scrape_yandere(url)
    elif sites[2] in url:
        scrape_danbooru(url)
    