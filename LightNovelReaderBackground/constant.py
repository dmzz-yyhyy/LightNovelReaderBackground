# url
DATA_SOURCE_HOME = 'https://www.wenku8.net/'
BOOK_URL = DATA_SOURCE_HOME + 'book/{book_id}.htm'
BOOK_CHAPTERS_CONTENT_URL = DATA_SOURCE_HOME + 'novel/2/{book_id}/{chapter_id}.htm'
# selector
BOOK_NOT_FOUND_SELECTOR = 'body > div > div > div > div.blocktitle'
BOOK_NAME_SELECTOR = '#content > div > table > tr >  td > table > tr > td > span > b'
BOOK_COVER_SELECTOR = '#content > div > table > tr > td > img'
BOOK_INTRODUCTION = '#content > div > table > tr > td:nth-child(2) > span:nth-child(13)'
BOOK_CHAPTERS_MENU = '#content > div:nth-child(1) > div:nth-child(6) > div > span:nth-child(1) > fieldset > div > a'
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
BOOK_CHAPTERS_CONTENT_REPLACE_KEY_WORD_LIST = ['本文来自 轻小说文库(http://www.wenku8.com)',
                                               '最新最全的日本动漫轻小说 轻小说文库(http://www.wenku8.com) 为你一网打尽！']
# other
REQUESTS_HEADERS = {
    'cookie': 'Hm_lvt_acfbfe93830e0272a88e1cc73d4d6d0f=1689699383; Hm_lvt_d72896ddbf8d27c750e3b365ea2fc902=1689599799,1689699383; Hm_lpvt_acfbfe93830e0272a88e1cc73d4d6d0f=1689700321; cf_clearance=JGfSQ1POKy_Y_AQEyF_TIniYg.u.dAY7uGOYdHDBrL4-1689700322-0-0.2.1689700322; jieqiVisitId=article_articleviews%3D2152; PHPSESSID=9f0c1944571bd0325f49e333db9776a0; jieqiUserInfo=jieqiUserId%3D1125456%2CjieqiUserName%3Dyyhyy%2CjieqiUserGroup%3D3%2CjieqiUserVip%3D0%2CjieqiUserPassword%3Deb62861281462fd923fb99218735fef0%2CjieqiUserName_un%3Dyyhyy%2CjieqiUserHonor_un%3D%26%23x666E%3B%26%23x901A%3B%26%23x4F1A%3B%26%23x5458%3B%2CjieqiUserGroupName_un%3D%26%23x666E%3B%26%23x901A%3B%26%23x4F1A%3B%26%23x5458%3B%2CjieqiUserLogin%3D1689700457; jieqiVisitInfo=jieqiUserLogin%3D1689700457%2CjieqiUserId%3D1125456; Hm_lpvt_d72896ddbf8d27c750e3b365ea2fc902=1689700460',
    'sec-ch-ua': 'Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114',
    'Sec-Ch-Ua-Platform': 'Windows',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'}
REQUESTS_PROXIES = True
RECONNECT_TIMES = 5
MAX_CACHE = 50
