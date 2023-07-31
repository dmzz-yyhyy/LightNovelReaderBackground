import json
import random
import time
from typing import Dict

import cfscrape
from bs4 import BeautifulSoup

from constant import *


def get_soup(url: str) -> BeautifulSoup:
    soup = None
    for i in range(RECONNECT_TIMES):
        try:
            scraper = cfscrape.create_scraper()
            if REQUESTS_PROXIES:
                with open("proxies.json", "r") as file:
                    proxies = json.loads(file.read())
                    proxies = proxies[random.randint(0, len(proxies))]
                res = scraper.get(url, headers=REQUESTS_HEADERS, proxies=proxies)
            else:
                res = scraper.get(url, headers=REQUESTS_HEADERS)

            res.encoding = 'gbk'
            data = res.text
            soup = BeautifulSoup(data, 'lxml')
            break
        except IndexError:
            print("had no proxies to use")
        except Exception as e:
            print(e)
            print("reconnect " + str(i + 1))

    return soup


def format(text: str, dict: Dict) -> str:
    return_text = text
    for keyname in dict:
        return_text = return_text.replace('{' + keyname + '}', str(dict[keyname]))
    return return_text


def is_time_over(last, wait):
    return (time.time() - last) > wait
