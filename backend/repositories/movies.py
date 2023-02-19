from sqlalchemy.orm import Session

from ..models  import movie as movie_models
from ..schemas import movie as movie_schemas

def get_movies(db: Session, skip: int = 0, limit: int = 10):
    return db.query(movie_models.Movie).offset(skip).limit(limit).all()

def get_movie(db: Session, id: int):
    return db.query(movie_models.Movie).filter(movie_models.Movie.id == id).first()

def delete_movie(db: Session, movie: movie_models.Movie):
    db.delete(movie)
    db.commit()

def create_movie(db: Session, movie: movie_schemas.MovieCreate):
    db_movie = movie_models.Movie(title=movie.title)
    db.add(db_movie)
    db.commit()
    db.refresh(db_movie)

    return db_movie

def update_movie(db: Session, movie_update: movie_schemas.MovieCreate, movie: movie_models.Movie, exclude_unset: bool = True):
    update_data = movie_update.dict(exclude_unset=exclude_unset)

    if 'title' in update_data:
        movie.title = update_data['title']

    db.add(movie)
    db.commit()

    return movie
