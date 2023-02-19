from fastapi        import APIRouter, Depends
from sqlalchemy.orm import Session

from ..schemas      import movie as movie_schemas
from ..database     import get_db_session
from ..repositories import movies as movies_repository

router = APIRouter(prefix="/movies")

@router.get("", response_model=list[movie_schemas.Movie])
def read_movies(skip: int = 0, limit: int = 10, db: Session = Depends(get_db_session)):
    return movies_repository.get_users(db, skip=skip, limit=limit)
