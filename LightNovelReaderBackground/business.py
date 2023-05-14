from typing import Dict, Optional, Union, List, Any

from LightNovelReaderBackground import *
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
            'BookCoverURL': book_cover_url,
            'BookIntroduction': book_introduction
        }
    }
    return data


def get_book_chapter_list(book_id: int) -> Union[
    Dict[str, Optional[str]], Dict[str, List[Dict[str, Union[List[Any], str]]]], Dict[str, Optional[str]], Dict[
        str, Dict[str, str]]]:
    book_url = utilities.format(BOOK_CHAPTERS_LIST_URL, {'book_id': book_id})
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
