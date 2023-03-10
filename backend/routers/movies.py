from fastapi import APIRouter, Depends, HTTPException, Response
from sqlalchemy.orm import Session

from ..models.movie import Movie as MovieModel
from ..schemas import movie as movie_schemas
from ..database import get_db_session
from ..repositories import movies as movies_repository

router = APIRouter(prefix="/movies")


@router.get("", response_model=list[movie_schemas.Movie])
def list_movies(response: Response,
                skip: int = 0,
                limit: int = 10,
                db: Session = Depends(get_db_session)) -> list[MovieModel]:
    """Returns a list of movies."""
    response.headers['X-Total-Count'] = str(movies_repository.get_total_count(db))

    return movies_repository.get_movies(db, skip=skip, limit=limit)


@router.get("/{id}", response_model=movie_schemas.Movie)
def get_movie(id: int, db: Session = Depends(get_db_session)) -> MovieModel:
    """Returns a detailed view of a movie."""
    movie = movies_repository.get_movie(db, id)
    if movie is None:
        raise HTTPException(404, "Not found")

    return movie


@router.delete("/{id}")
def delete_movie(id: int, db: Session = Depends(get_db_session)) -> Response:
    """Deletes an existing movie."""
    movie = movies_repository.get_movie(db, id)
    if movie is None:
        raise HTTPException(404, "Not found")

    movies_repository.delete_movie(db, movie)

    return Response(status_code=204)


@router.post("", response_model=movie_schemas.Movie, status_code=201)
def create_movie(
    movie: movie_schemas.MovieCreate, db: Session = Depends(get_db_session)
) -> MovieModel:
    """Creates a new movie."""
    return movies_repository.create_movie(db, movie)


@router.patch("/{id}", response_model=movie_schemas.Movie)
def patch_movie(
    id: int,
    movie_update: movie_schemas.MovieUpdatePatch,
    db: Session = Depends(get_db_session)
) -> MovieModel:
    """Updates a movie data.

    If a field is missing it won't be changed in the database.
    """
    movie = movies_repository.get_movie(db, id)
    if movie is None:
        raise HTTPException(404, "Not found")

    return movies_repository.update_movie(db,
                                          movie_update,
                                          movie,
                                          exclude_unset=True)


@router.put("/{id}", response_model=movie_schemas.Movie)
def put_movie(
    id: int,
    movie_update: movie_schemas.MovieCreate,
    db: Session = Depends(get_db_session)
) -> MovieModel:
    """Updates a movie data.

    If a field is missing it will be set to null in the database.
    """
    movie = movies_repository.get_movie(db, id)
    if movie is None:
        raise HTTPException(404, "Not found")

    return movies_repository.update_movie(db,
                                          movie_update,
                                          movie,
                                          exclude_unset=False)
