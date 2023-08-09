from fastapi import FastAPI

import business
import cache
from proxies import GetProxiesThread
from cache import Cache

app = FastAPI()
get_proxies = [GetProxiesThread(), GetProxiesThread(), GetProxiesThread()]
cache_objet = Cache()


@app.on_event("startup")
def on_setup():
    print(get_proxies)
    get_proxies[0].start()
    get_proxies[1].start()
    get_proxies[2].start()
    cache_objet.start()


@app.get("/get_book_information")
def get_book_information(book_id: int):
    uid = str(book_id) + "BI"
    data = cache.get(uid)
    if data is None:
        cache.save(uid, business.get_book_information(book_id))
        data = cache.get(uid)
    return data


@app.get("/get_book_chapter_list")
async def get_book_chapter_list(book_id: int):
    uid = str(book_id) + "BCL"
    data = cache.get(uid)
    if data is None:
        cache.save(uid, business.get_book_chapter_list(book_id))
        data = cache.get(uid)
    return data


@app.get('/get_book_chapter_content')
async def get_book_chapter_content(book_id: int, chapter_id: int):
    uid = str(book_id) + "_" + str(chapter_id) + "BCC"
    data = cache.get(uid)
    if data is None:
        cache.save(uid, business.get_book_chapter_content(book_id, chapter_id))
        data = cache.get(uid)
    return data


@app.get('/search_book')
async def search_book(search_type: str, book_name: str):
    uid = str(search_type) + "_" + str(book_name) + "SB"
    data = cache.get(uid)
    if data is None:
        cache.save(uid, business.search_book(search_type, book_name))
        data = cache.get(uid)
    return data


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
