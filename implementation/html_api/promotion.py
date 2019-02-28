import re

from bs4 import BeautifulSoup

import requests


def promotion_links(url: str):
    promo_patterns = (
        'promocje',
        'promocja',
        'promo',
        'promotion',
        'promotions'
    )

    r = requests.get(url)
    html = r.text
    b_soup = BeautifulSoup(html, 'html.parser')

    links = set()
    for link in b_soup.find_all('a'):
        for pattern in promo_patterns:
            href = link.get('href')
            if re.search(pattern, href):
                links.add(href)

    return links

