from fastapi        import APIRouter, Depends, HTTPException, Response
from sqlalchemy.orm import Session

from ..schemas      import movie as movie_schemas
from ..database     import get_db_session
from ..repositories import movies as movies_repository

router = APIRouter(prefix="/movies")

@router.get("", response_model=list[movie_schemas.Movie])
def list_movies(skip: int = 0, limit: int = 10, db: Session = Depends(get_db_session)):
    return movies_repository.get_movies(db, skip=skip, limit=limit)

@router.get("/{id}", response_model=movie_schemas.Movie)
def get_movie(id: int, db: Session = Depends(get_db_session)):
    movie = movies_repository.get_movie(db, id)
    if movie is None:
        raise HTTPException(404, "Not found")

    return movie

@router.delete("/{id}")
def delete_movie(id: int, db: Session = Depends(get_db_session)):
    movie = movies_repository.get_movie(db, id)
    if movie is None:
        raise HTTPException(404, "Not found")

    movies_repository.delete_movie(db, movie)

    return Response(status_code=204)
