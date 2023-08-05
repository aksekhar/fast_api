from fastapi import FastAPI, Body

app = FastAPI()

BOOKS = [
    {'title': 'Title One', 'author': 'Author One', 'category': 'science'},
    {'title': 'Title Two', 'author': 'Author Two', 'category': 'science'},
    {'title': 'Title Three', 'author': 'Author Three', 'category': 'history'},
    {'title': 'Title Four', 'author': 'Author Four', 'category': 'math'},
    {'title': 'Title Five', 'author': 'Author Five', 'category': 'math'},
    {'title': 'Title Six', 'author': 'Author Two', 'category': 'math'}
]


@app.get("/all_books")
async def fast_api():
    return BOOKS


@app.get("/all_books{title}")
async def fast_api(title: str):
    for b in BOOKS:
        if b.get('title').casefold() == title.casefold():
            return b


@app.get("/all_books/{book_auth}/")
async def fetch_data_by_params(book_auth: str, category: str):
    book_by_cate = []
    for b in BOOKS:
        if b.get('author').casefold() == book_auth.casefold() and \
                b.get('category').casefold() == category.casefold():
            book_by_cate.append(b)
    return book_by_cate


@app.get("/all_books/")
async def fetch_data_by_query(category: str):
    book_by_cate = []
    for b in BOOKS:
        if b.get('category').casefold() == category.casefold():
            book_by_cate.append(b)
    return book_by_cate


@app.post("/books/create_book")
async def create_book(new_book=Body()):
    BOOKS.append(new_book)


@app.put("/books/update_book")
async def update_book(updated_book=Body()):
    for i in range(len(BOOKS)):
        if BOOKS[i].get('title').casefold() == updated_book.get('title').casefold():
            BOOKS[i] = updated_book


@app.delete("/books/delete_book/{title}")
async def delete_book(title: str):
    for i in range(len(BOOKS)):
        if BOOKS[i].get('title').casefold() == title.casefold():
            BOOKS.pop(i)
            break
