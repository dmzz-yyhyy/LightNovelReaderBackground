from typing import Dict

import cfscrape
from bs4 import BeautifulSoup

from constant import *


def get_soup(url: str) -> BeautifulSoup:
    scraper = cfscrape.create_scraper()
    if REQUESTS_PROXIES is None:
        res = scraper.get(url, headers=REQUESTS_HEADERS)
    else:
        res = scraper.get(url, headers=REQUESTS_HEADERS, proxies=REQUESTS_PROXIES)
    res.encoding = 'gbk'
    data = res.text
    soup = BeautifulSoup(data, 'lxml')
    return soup


def format(text: str, dict: Dict) -> str:
    return_text = text
    for keyname in dict:
        return_text = return_text.replace('{' + keyname + '}', str(dict[keyname]))
    return return_text
