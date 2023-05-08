class BookContent:
    def __init__(self, book_url:str):
        self.book_url = book_url


class Book:
    def __init__(self, book_url: str, name: str, cover_url: str, content: BookContent):
        self.name = name
        self.cover_url = cover_url
        self.content = BookContent(book_url)

    def get_all_data(self):
        dict = {'name': ''}


