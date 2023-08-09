import re
import time
from typing import Dict, Optional, Union, List, Any
from urllib.parse import quote

import utilities
from constant import *


def get_book_information(book_id: int) -> Dict[str, str]:
    book_url = utilities.format(BOOK_URL, {'book_id': book_id})
    soup = utilities.get_soup(book_url)
    if soup.select_one(BOOK_NOT_FOUND_SELECTOR) is not None:
        if soup.select_one(BOOK_NOT_FOUND_SELECTOR).text.find(BOOK_NOT_FOUND_KEY_WORD) != -1:
            return {'data': None, 'error': 'book not found'}
    book_name = soup.select_one(BOOK_NAME_SELECTOR).text
    book_cover_url = soup.select_one(BOOK_COVER_SELECTOR).get('src')
    book_introduction = soup.select_one(BOOK_INTRODUCTION).text.replace('<br>', '\n')
    data = {
        'data': {
            'bookID': book_id,
            'bookName': book_name,
            'bookCoverURL': book_cover_url,
            'bookIntroduction': book_introduction
        }
    }
    return data


def get_book_chapter_list(book_id: int) -> Union[
    Dict[str, Optional[str]], Dict[str, List[Dict[str, Union[List[Any], str]]]], Dict[str, Optional[str]], Dict[
        str, Dict[str, str]]]:
    book_url = utilities.format(BOOK_URL, {'book_id': book_id})
    soup = utilities.get_soup(book_url)
    if soup.select_one(BOOK_NOT_FOUND_SELECTOR) is not None:
        if soup.select_one(BOOK_NOT_FOUND_SELECTOR).text.find(BOOK_NOT_FOUND_KEY_WORD) != -1:
            return {'data': None, 'error': 'book not found'}
    book_url = soup.select_one(BOOK_CHAPTERS_MENU).get('href')
    soup = utilities.get_soup(book_url)
    if soup.select_one(BOOK_CHAPTERS_LIST_NOT_FOUND_SELECTOR) is not None:
        if soup.select_one(BOOK_CHAPTERS_LIST_NOT_FOUND_SELECTOR).text.find(
                BOOK_CHAPTERS_LIST_NOT_FOUND_KEY_WORD) != -1:
            return {'data': None, 'error': 'book not found'}
    res_chapter_list = soup.select(BOOK_CHAPTERS_LIST_SELECTOR)
    chapter_list = []
    volume_number = 0
    for chapter in res_chapter_list:
        if chapter.get('class')[0] == BOOK_CHAPTERS_LIST_VOLUME_CLASS_NAME_KEY_WORD:
            volume_name = chapter.text
            chapter_list.append({'volumeName': volume_name, 'chapters': []})
            volume_number += 1
        else:
            if chapter.select_one('a') is not None:
                chapter_list[volume_number - 1]['chapters'].append(
                    {'title': chapter.text, 'id': chapter.select_one('a').get('href').replace('.htm', '')})
    data = {'data': chapter_list}
    return data


def get_book_chapter_content(book_id: int, chapter_id) -> Dict[str, Optional[str]]:
    book_url = utilities.format(BOOK_CHAPTERS_CONTENT_URL, {'book_id': book_id, 'chapter_id': chapter_id})
    soup = utilities.get_soup(book_url)
    if soup.select_one(BOOK_CHAPTERS_CONTENT_NOT_FOUND_SELECTOR) is not None:
        if soup.select_one(BOOK_CHAPTERS_CONTENT_NOT_FOUND_SELECTOR).text.find(
                BOOK_CHAPTERS_CONTENT_NOT_FOUND_KEY_WORD) != -1:
            return {'data': None, 'error': 'book not found'}
    res_content = soup.select_one(BOOK_CHAPTERS_CONTENT_SELECTOR)
    content = ''
    for key_word in BOOK_CHAPTERS_CONTENT_REPLACE_KEY_WORD_LIST:
        content = res_content.text.replace(key_word, '')
    title = soup.select_one(BOOK_CHAPTERS_CONTENT_TITLE_SELECTOR).text
    data = {
        'data': {
            'title': title,
            'content': content
        }
    }
    return data


def search_book(search_type: str, book_name: str):
    search_url = utilities.format(SEARCH_BOOK_URL,
                                  {'search_type': search_type, 'book_name': quote(book_name, encoding='gbk'),
                                   'page': 1})
    soup = utilities.get_soup(search_url)
    book_list_page_number = soup.select_one(SEARCH_BOOK_PAGE_NUMBER_SELECTOR).text
    data = {
        'data': {
            'searchBookList': []
        }
    }
    if book_list_page_number is None:
        return data
    book_list = []
    for i in range(int(book_list_page_number)):
        search_url = utilities.format(SEARCH_BOOK_URL,
                                      {'search_type': search_type, 'book_name': quote(book_name, encoding='gbk'),
                                       'page': book_list_page_number})
        is_get_succeed = False
        while not is_get_succeed:
            soup = utilities.get_soup(search_url, is_use_proxies=True)
            if soup.select_one(SEARCH_BOOK_TOO_FAST_SELECTOR).text.find(SEARCH_BOOK_TOO_FAST_KEY_WORD) == -1:
                is_get_succeed = True
            time.sleep(3)
        book_list_temp = soup.select(SEARCH_BOOK_SELECTOR)

        for book in book_list_temp:
            book_id = re.search(SEARCH_BOOK_ID_REGEX, book.select_one(SEARCH_BOOK_ID_SELECTOR).get('href')).group()
            title = book.select_one(SEARCH_BOOK_TITLE_SELECTOR).text
            cover_url = book.select_one(SEARCH_BOOK_COVER_URL_SELECTOR).get('src')
            writer_and_type = book.select_one(SEARCH_BOOK_WRITER_AND_TYPE_SELECTOR).text
            writer_and_type = writer_and_type.split("/")
            writer = writer_and_type[0].split(":")[1]
            book_type = writer_and_type[1].split(":")[1]
            tags = book.select_one(SEARCH_BOOK_TAGS_SELECTOR).text.split(":", 1)[0].split(" ")
            introduction = book.select_one(SEARCH_BOOK_INTRODUCTION_SELECTOR).text.split(":", 1)[1]
            book_list.append({
                'bookId': book_id,
                'title': title,
                'coverUrl': cover_url,
                'writer': writer,
                'type': book_type,
                'tags': tags,
                'introduction': introduction
            })
    data['data']['searchBookList'] = book_list
    return data
