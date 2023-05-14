from LightNovelReaderBackground import *
from fastapi import FastAPI

app = FastAPI()



@app.get("/get_book_information")
async def get_book_information(book_id: int):
    return business.get_book_information(book_id)

@app.get("/get_book_chapter_list")
async def get_book_chapter_list(book_id: int):
    return business.get_book_chapter_list(book_id)

@app.get('/get_book_chapter_content')
async def get_book_chapter_content(book_id: int, chapter_id: int):
    return business.get_book_chapter_content(book_id, chapter_id)