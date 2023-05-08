import cfscrape
import lxml
from bs4 import BeautifulSoup


def get_soup(url: str):
    scraper = cfscrape.create_scraper()
    res = scraper.get("https://www.wenku8.net/book/2312753.htm")
    res.encoding = 'gbk'
    data = res.text
    soup = BeautifulSoup(data, lxml)
    return soup

def class_to_dict(arg*):

