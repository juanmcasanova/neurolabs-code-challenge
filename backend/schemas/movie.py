from pydantic import BaseModel, Field
from typing import Union


class MovieBase(BaseModel):
    title: str = Field(min_length=1)


class Movie(MovieBase):
    id: int

    class Config:
        orm_mode = True


class MovieCreate(MovieBase):
    pass


class MovieUpdatePatch(MovieBase):
    title: Union[str, None] = Field(min_length=1)
