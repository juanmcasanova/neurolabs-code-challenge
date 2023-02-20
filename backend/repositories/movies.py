from sqlalchemy.orm import Session
from typing import Union

from ..models.movie import Movie as MovieModel
from ..schemas import movie as movie_schemas


def get_movies(db: Session,
               skip: int = 0,
               limit: int = 10) -> list[MovieModel]:
    return db.query(MovieModel).order_by(MovieModel.id.asc()).offset(skip).limit(limit).all()


def get_movie(db: Session, id: int) -> Union[MovieModel, None]:
    return db.query(MovieModel).filter(MovieModel.id == id).first()


def delete_movie(db: Session, movie: MovieModel) -> None:
    db.delete(movie)
    db.commit()


def create_movie(db: Session, movie: movie_schemas.MovieCreate) -> MovieModel:
    db_movie = MovieModel(title=movie.title)
    db.add(db_movie)
    db.commit()
    db.refresh(db_movie)

    return db_movie


def update_movie(db: Session,
                 movie_update: movie_schemas.MovieCreate,
                 movie: MovieModel,
                 exclude_unset: bool = True) -> MovieModel:
    update_data = movie_update.dict(exclude_unset=exclude_unset)

    if 'title' in update_data:
        movie.title = update_data['title']

    db.add(movie)
    db.commit()

    return movie

def get_total_count(db: Session) -> int:
    return db.query(MovieModel).count()
