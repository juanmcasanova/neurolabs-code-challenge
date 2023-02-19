from pydantic import BaseModel

class MovieBase(BaseModel):
    id: int
    title: str

class Movie(MovieBase):
    class Config:
        orm_mode = True
