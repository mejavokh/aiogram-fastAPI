from sqlalchemy.orm import Session

from app import schemas, models

def get_books(db: Session):
    return db.query(models.Book).all()

def get_book_by_id(db: Session, book_id: int):
    return db.query(models.Book).filter(
        models.Book.id == book_id
    ).first()

def create_book(db: Session, book: schemas.BookCreate, author_id: int):
    data = book.model_dump()
    data.pop("author_id", None)
    db_book = models.Book(**data, author_id=author_id)
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book

def update_book(db: Session, book_update: schemas.BookUpdate, book_id: int):
    db_book = db.query(models.Book).filter(models.Book.id==book_id).first()
    
    if not db_book:
        return None
    
    update_data = book_update.model_dump(exclude_unset=True)
    
    for key, value in update_data.items():
        setattr(db_book, key, value)
    
    db.commit()
    db.refresh(db_book)
    
    return db_book

def delete_book(db: Session, book_id: int):
    book = get_book_by_id(db=db, book_id=book_id)
    
    if not book:
        return None
    
    db.delete(book)
    db.commit()
    
    return book

def get_authors(db: Session):
    return db.query(models.Author).all()

def get_author_by_id(db: Session, author_id: int):
    return db.query(models.Author).filter(
        models.Author.id == author_id
    ).first()

def create_author(db: Session, author: schemas.AuthorCreate):
    db_author = models.Author(**author.model_dump())
    
    db.add(db_author)
    db.commit()
    db.refresh(db_author)
    
    return db_author

def update_author(db: Session, author_update: schemas.AuthorUpdate, author_id: int):
    db_author = db.query(models.Author).filter(
        models.Author.id == author_id
    ).first()
    
    if not db_author:
        return None
    
    update_data = author_update.model_dump(exclude_unset=True)
    
    for key, value in update_data.items():
        setattr(author_update, key, value)
        
    db.commit()
    db.refresh(db_author)
    
    return db_author

def delete_author(db: Session, author_id: int):
    author = get_author_by_id(db=db, author_id=author_id)
    
    if not author:
        return None
    
    db.delete(author)
    db.commit()
    
    return author

def get_books_by_author_id(db: Session, author_id: int):
    return db.query(models.Book).filter(
        models.Book.author_id == author_id
    ).all()