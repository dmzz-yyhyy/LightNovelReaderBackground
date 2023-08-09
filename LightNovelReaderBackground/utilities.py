import json
import random
import time
from typing import Dict

import cfscrape
from bs4 import BeautifulSoup

from constant import *


def get_soup(url: str, is_use_proxies: bool = REQUESTS_PROXIES) -> BeautifulSoup:
    soup = None
    for i in range(RECONNECT_TIMES):
        try:
            scraper = cfscrape.create_scraper()
            if is_use_proxies:
                with open("proxies.json", "r") as file:
                    local_proxies = json.loads(file.read())
                proxies = local_proxies['proxies'][local_proxies['index'] % len(local_proxies['proxies'])]
                with open("proxies.json", "w") as file:
                    local_proxies['index'] = (1 + local_proxies['index']) % len(local_proxies['proxies'])
                    file.write(json.dumps(local_proxies, indent=2))
                res = scraper.get(url, headers=REQUESTS_HEADERS, proxies=proxies, timeout=3)
            else:
                res = scraper.get(url, headers=REQUESTS_HEADERS)

            res.encoding = 'gbk'
            data = res.text
            soup = BeautifulSoup(data, 'lxml')
            return soup
        except IndexError as e:
            print(e)
            print("had no proxies to use")
        except Exception as e:
            print(e)
            print("reconnect " + str(i - 1))
    return soup


def format(text: str, dict: Dict) -> str:
    return_text = text
    for keyname in dict:
        return_text = return_text.replace('{' + keyname + '}', str(dict[keyname]))
    return return_text


def is_time_over(last, wait):
    return (time.time() - last) > wait
