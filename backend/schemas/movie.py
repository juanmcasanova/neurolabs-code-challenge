from pydantic import BaseModel
from typing import Union


class MovieBase(BaseModel):
    title: str


class Movie(MovieBase):
    id: int

    class Config:
        orm_mode = True


class MovieCreate(MovieBase):
    pass


class MovieUpdatePatch(MovieBase):
    title: Union[str, None]
