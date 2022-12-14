from src.logging.logger import *
from src.utilities.soupify import *

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
                        AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 \
                        Safari/537.36'}

BASE_URL = 'https://konachan.com/'
PAGE_CODE = "k"



def get_post_ids(page):
    posts_list = page.find('ul', {'id': 'post-list-posts'})
    posts = posts_list.findAll('li')
    ids = []
    for post in posts:
        # alt = post.find('img', alt=True)['alt']
        id = post['id'][1:]
        if id+PAGE_CODE not in NUM_SET:
            ids.append(id)
    next_page = BASE_URL + page.find('a', {'class': 'next_page'})['href']
    return ids, next_page


def scrape_konachan(url):
    page = read_url(url, headers)
    # print("Page read!")
    ids, next_page = get_post_ids(page)
    print(ids)


