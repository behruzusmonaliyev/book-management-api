from pydantic import BaseModel, Field
from typing import Optional

class BookBase(BaseModel):
    title: str
    author: str
    genre: str
    year: int = Field(..., ge=0)
    rating: float = Field(..., ge=0.0, le=5.0)

class BookCreate(BookBase):
    pass

class BookUpdate(BookBase):
    pass

class BookResponse(BookBase):
    id: int

    class Config:
        orm_mode = True
