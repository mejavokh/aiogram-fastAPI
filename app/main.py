from fastapi import FastAPI, HTTPException, Depends, Body
from typing import Annotated, List
from sqlalchemy.orm import Session

from app import schemas, database, models, crud

models.Base.metadata.create_all(bind=database.engine)
app = FastAPI()

def get_db():
    db = database.session_local()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def main_menu():
    return f"This is main menu"

@app.get("/books", response_model=List[schemas.BookResponse])
def get_all_books(db: Session=Depends(get_db)):
    return crud.get_books(db=db)

@app.get("/books/{book_id}", response_model=schemas.BookResponse)
def get_book_by_id(book_id: int, db: Session=Depends(get_db)):
    book = crud.get_book_by_id(db=db, book_id=book_id)
    
    if book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    
    return book

@app.post("/books", response_model=schemas.BookResponse)
def create_new_book(
    book: Annotated[schemas.BookCreateWithAuthor, Body(
            example={
                "title": "The Clean Coder",
                "summary": "A book about being a professional programmer",
                "image": "images/clean_coder.jpg",
                "author_id": 1
            }
        )],
    db: Session=Depends(get_db)
):
    return crud.create_book(db=db, book=book, author_id=book.author_id)

@app.put("/books/{book_id}")
def update_book_by_id(
    book_id: int,
    book_update: Annotated[schemas.BookUpdate, Body(
        example={
            "title": "Update book title",
            "summary": "Updated description of the book",
            "image": "new path to image",
            "author_id": 3
        }
    )],
    db: Session=Depends(get_db)
):
    db_book = crud.update_book(db=db, book_update=book_update, book_id=book_id)
    
    if db_book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    
    return db_book

@app.delete("/books/{book_id}", response_model=schemas.BookResponse)
def delete_book_by_id(book_id: int, db: Session=Depends(get_db)):
    db_book = crud.delete_book(book_id=book_id, db=db)
    
    if db_book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    
    return db_book

@app.get("/authors", response_model=List[schemas.AuthorResponse])
def get_all_authors(db: Session=Depends(get_db)):
    return crud.get_authors(db=db)

@app.get("/authors/{author_id}", response_model=schemas.AuthorResponse)
def get_author_by_id(author_id: int, db: Session=Depends(get_db)):
    author = crud.get_author_by_id(db=db, author_id=author_id)
    
    if author is None:
        raise HTTPException(status_code=404, detail="Author not found")
    
    return author

@app.post("/authors", response_model=schemas.AuthorResponse)
def create_author(
    author: Annotated[schemas.AuthorCreate, Body(
        example={
            "name": "Joanna Ketlin Rowling",
            "image": "images/rowling.png"
        }
    )],
    db: Session=Depends(get_db)
):
    return crud.create_author(db=db, author=author)

@app.put("/authors?{author_id}", response_model=schemas.AuthorResponse)
def update_author(
    author_id: int,
    author_update: Annotated[schemas.AuthorUpdate, Body(
        example={
            "name": "John Doe",
            "image": "images/name_image.png"
        }
    )],
    db: Session=Depends(get_db)
):
    db_author = crud.update_author(db=db, author_id=author_id, author_update=author_update)
    
    if db_author is None:
        raise HTTPException(status_code=404, detail="Author not found")
    
    return db_author

@app.delete("/author/{author_id}", response_model=schemas.AuthorResponse)
def delete_author(author_id: int, db: Session=Depends(get_db)):
    db_author = crud.delete_author(author_id=author_id, db=db)
    
    if db_author is None:
        raise HTTPException(status_code=404, detail="Author not found")
    
    return db_author

@app.get("/authors/{author_id}/books", response_model=List[schemas.BookResponse])
def get_books_by_author_id(author_id: int, db: Session=Depends(get_db)):
    books = crud.get_books_by_author_id(db=db, author_id=author_id)
    
    return books
