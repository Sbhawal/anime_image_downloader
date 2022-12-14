import requests
from bs4 import BeautifulSoup


def read_url(url, headers=''):
    """Reads a url and returns the html"""
    if headers != '':
        response = requests.get(url, headers=headers)
    else:
        response = requests.get(url)  
    soup = BeautifulSoup(response.text, 'html.parser')
    return soup

