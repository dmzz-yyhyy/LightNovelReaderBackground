# url
DATA_SOURCE_HOME = 'https://www.wenku8.net/'
BOOK_URL = DATA_SOURCE_HOME + 'book/{book_id}.htm'
BOOK_CHAPTERS_LIST_URL = DATA_SOURCE_HOME + 'novel/2/{book_id}/index.htm'
BOOK_CHAPTERS_CONTENT_URL = DATA_SOURCE_HOME + 'novel/2/{book_id}/{chapter_id}.htm'
# selector
BOOK_NOT_FOUND_SELECTOR = 'body > div > div > div > div.blocktitle'
BOOK_NAME_SELECTOR = '#content > div > table > tr >  td > table > tr > td > span > b'
BOOK_COVER_SELECTOR = '#content > div > table > tr > td > img'
BOOK_INTRODUCTION = '#content > div > table > tr > td:nth-child(2) > span:nth-child(13)'
BOOK_CHAPTERS_LIST_NOT_FOUND_SELECTOR = '#content > table > caption'
BOOK_CHAPTERS_LIST_SELECTOR = 'body > table > tr > td'
BOOK_CHAPTERS_CONTENT_NOT_FOUND_SELECTOR = '#content > table > caption'
BOOK_CHAPTERS_CONTENT_TITLE_SELECTOR = '#title'
BOOK_CHAPTERS_CONTENT_SELECTOR = '#content'
# key word
BOOK_NOT_FOUND_KEY_WORD = '出现错误'
BOOK_CHAPTERS_LIST_NOT_FOUND_KEY_WORD = '出错啦，你所访问的网址不存在，可能是该小说已经更换版本，请你在本站重新查找'
BOOK_CHAPTERS_CONTENT_NOT_FOUND_KEY_WORD = '出错啦，你所访问的网址不存在，可能是该小说已经更换版本，请你在本站重新查找'
BOOK_CHAPTERS_LIST_VOLUME_CLASS_NAME_KEY_WORD = 'vcss'
BOOK_CHAPTERS_CONTENT_REPLACE_KEY_WORD_LIST = ['本文来自 轻小说文库(http://www.wenku8.com)', '最新最全的日本动漫轻小说 轻小说文库(http://www.wenku8.com) 为你一网打尽！']
# other
REQUESTS_HEADERS = {
    'cookie': 'Hm_lvt_acfbfe93830e0272a88e1cc73d4d6d0f=1683048552,1683394569; Hm_lvt_d72896ddbf8d27c750e3b365ea2fc902=1683396890,1683652391,1683828453,1683984695; jieqiUserInfo=jieqiUserId%3D1125456%2CjieqiUserName%3Dyyhyy%2CjieqiUserGroup%3D3%2CjieqiUserVip%3D0%2CjieqiUserPassword%3Deb62861281462fd923fb99218735fef0%2CjieqiUserName_un%3Dyyhyy%2CjieqiUserHonor_un%3D%26%23x65B0%3B%26%23x624B%3B%26%23x4E0A%3B%26%23x8DEF%3B%2CjieqiUserGroupName_un%3D%26%23x666E%3B%26%23x901A%3B%26%23x4F1A%3B%26%23x5458%3B%2CjieqiUserLogin%3D1683984748; jieqiVisitInfo=jieqiUserLogin%3D1683984748%2CjieqiUserId%3D1125456; PHPSESSID=e7c7b2ed413c0e806083403875be1728; Hm_lpvt_d72896ddbf8d27c750e3b365ea2fc902=1683985358',
    'sec-ch-ua': '"Microsoft Edge";v="113", "Chromium";v="113", "Not-A.Brand";v="24"',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36 Edg/113.0.1774.35'
}
