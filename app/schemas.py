from pydantic import BaseModel, constr
from typing import Annotated, Optional

class AuthorBase(BaseModel):
    name: str
    image: Annotated[str, constr(min_length=1)]

class AuthorCreate(AuthorBase):
    pass

class AuthorUpdate(AuthorBase):
    name: Optional[str] = None
    image: Optional[str] = None

class AuthorResponse(AuthorBase):
    id: int
    
    model_config = {
        "from_attributes": True
    }


class BookBase(BaseModel):
    title: str
    summary: str
    image: Annotated[str, constr(min_length=1)]

class BookCreate(BookBase):
    pass

class BookCreateWithAuthor(BookBase):
    author_id: int

class BookUpdate(BaseModel):
    title: Optional[str] = None
    summary: Optional[str] = None
    image: Optional[str] = None
    author_id: Optional[int] = None

class BookResponse(BookBase):
    id: int
    author_id: int
    
    model_config = {
        "from_attributes": True
    }