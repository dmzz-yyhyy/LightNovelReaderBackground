import json
import time
from threading import Thread

import bs4
import requests

from constant import REQUESTS_HEADERS


class GetProxiesThread(Thread):
    def __init__(self):
        """
        :param func: 可调用的对象
        :param args: 可调用对象的参数
        """
        Thread.__init__(self)
        self.proxies_list = []

    def kxdaili1(self):
        ip_list = []
        ip_ports = []
        ip_types = []
        for page in range(1, 11):
            res = requests.get("http://www.kxdaili.com/dailiip/2/" + str(page) + ".html")
            soup = bs4.BeautifulSoup(res.text, 'lxml')
            ip_list += soup.select(
                'body > div.banner-box > div.header-container > div.domain-block.price-block > div.auto > div.hot-product > div.hot-product-content > table > tbody > tr > td:nth-child(1)')
            ip_ports += soup.select(
                'body > div.banner-box > div.header-container > div.domain-block.price-block > div.auto > div.hot-product > div.hot-product-content > table > tbody > tr > td:nth-child(2)')
            ip_types += soup.select(
                'body > div.banner-box > div.header-container > div.domain-block.price-block > div.auto > div.hot-product > div.hot-product-content > table > tbody > tr > td:nth-child(4)')

        true_ip_list = []

        for index in range(len(ip_list)):
            ip = ip_list[index].text
            port = ip_ports[index].text
            ip_type = ip_types[index].text
            if ip_type == "HTTP,HTTPS":
                try:
                    proxies = {
                        'http': 'http://' + ip + ':' + port,
                        'https': 'http://' + ip + ':' + port
                    }
                    res = requests.get('https://www.wenku8.net/novel/2/2152/index.htm', headers=REQUESTS_HEADERS,
                                       proxies=proxies, timeout=3)
                    if res is not None:
                        true_ip_list.append({
                            'http': 'http://' + ip + ':' + port,
                            'https': 'http://' + ip + ':' + port
                        })
                except:
                    pass
        print("proxies update:", true_ip_list)
        return true_ip_list

    def kxdaili2(self, list_len):
        if list_len >= 3:
            return []
        ip_list = []
        ip_ports = []
        ip_types = []
        for page in range(1, 11):
            res = requests.get("http://www.kxdaili.com/dailiip/1/" + str(page) + ".html")
            soup = bs4.BeautifulSoup(res.text, 'lxml')
            ip_list += soup.select(
                'body > div.banner-box > div.header-container > div.domain-block.price-block > div.auto > div.hot-product > div.hot-product-content > table > tbody > tr > td:nth-child(1)')
            ip_ports += soup.select(
                'body > div.banner-box > div.header-container > div.domain-block.price-block > div.auto > div.hot-product > div.hot-product-content > table > tbody > tr > td:nth-child(2)')
            ip_types += soup.select(
                'body > div.banner-box > div.header-container > div.domain-block.price-block > div.auto > div.hot-product > div.hot-product-content > table > tbody > tr > td:nth-child(4)')
        true_ip_list = []

        for index in range(len(ip_list)):
            ip = ip_list[index].text
            port = ip_ports[index].text
            ip_type = ip_types[index].text
            if ip_type == "HTTP,HTTPS":
                try:
                    proxies = {
                        'http': 'http://' + ip + ':' + port,
                        'https': 'http://' + ip + ':' + port
                    }
                    res = requests.get('https://www.wenku8.net/novel/2/2152/index.htm', headers=REQUESTS_HEADERS,
                                       proxies=proxies, timeout=3)
                    if res is not None:
                        true_ip_list.append({
                            'http': 'http://' + ip + ':' + port,
                            'https': 'http://' + ip + ':' + port
                        })
                except:
                    pass
        print("proxies update:", true_ip_list)
        return true_ip_list

    def run(self):
        while True:
            self.proxies_list = self.kxdaili1()
            self.proxies_list += self.kxdaili2(len(self.proxies_list))
            if self.proxies_list != []:
                with open("proxies.json", "w") as file:
                    file.write(json.dumps(self.proxies_list, indent=2))
            time.sleep(3)
