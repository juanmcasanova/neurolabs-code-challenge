import os

from sqlalchemy                 import create_engine, Engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm             import sessionmaker, Session

engine       = create_engine(os.environ['DATABASE_URL'])
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base         = declarative_base()

def get_db_session() -> Session:
    """Returns a database session.

    The connection will be automatically closed.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
