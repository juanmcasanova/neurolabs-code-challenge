from sqlalchemy.orm import Session

from ..models import movie

def get_movies(db: Session, skip: int = 0, limit: int = 10):
    return db.query(movie.Movie).offset(skip).limit(limit).all()
