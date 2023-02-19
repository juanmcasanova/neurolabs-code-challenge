from pydantic import BaseModel

class MovieBase(BaseModel):
    title: str

class Movie(MovieBase):
    id: int

    class Config:
        orm_mode = True

class MovieCreate(MovieBase):
    pass
