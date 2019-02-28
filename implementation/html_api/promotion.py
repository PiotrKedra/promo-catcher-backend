import re

from bs4 import BeautifulSoup

import requests

promo_patterns = (
    '%',
    'TANIEJ',
    'RABATU',
    'Promocje',
    'promocje',
    'Promocja'
    'promocja',
    'Promo',
    'promo',
    'promotion',
    'promotions'
)


def find_promotion_messages(url: str):
    r = requests.get(url)
    html = r.text
    b_soup = BeautifulSoup(html, 'html.parser')

    result = []
    # TODO base on content class (ist not good)
    get_all_inner_text(b_soup.find('div', class_='content'), result)
    return result


def promotion_links(url: str) -> set:
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


def get_all_inner_text(tag: BeautifulSoup, result: list):
    try:
        tag.children
    except AttributeError:
        return tag

    for child in tag.children:
        text = get_all_inner_text(child, result)
        if text is not None:
            result.append(text)


r = requests.get('https://pizzababilon.pl/promocje/')
html = r.text
b_soup = BeautifulSoup(html, 'html.parser')

r = []

get_all_inner_text(b_soup.find('div', class_='content'), r)

print(r)
for ele in r:
    for pattern in promo_patterns:
        if re.search(pattern, ele):
            print(ele)