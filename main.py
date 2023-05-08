from fastapi import FastAPI
from tool import *
from constant import *

app = FastAPI()


@app.get("/get_book/by_id/get_name")
async def get_book_by_id(id: int):
    data = ''
    soup = get_soup(BOOK_URL.replace('{book_id}', id))
    if soup.select(BOOK_NOT_FOUND_SELECTOR).text == BOOK_NOT_FOUND_KEY_WORD:
        return {'data': 'null', 'error': 'book not found'}
    
    return {"data": data}
