from sqlalchemy.orm import Session

from ..models import movie

def get_movies(db: Session, skip: int = 0, limit: int = 10):
    return db.query(movie.Movie).offset(skip).limit(limit).all()

def get_movie(db: Session, id: int):
    return db.query(movie.Movie).filter(movie.Movie.id == id).first()
