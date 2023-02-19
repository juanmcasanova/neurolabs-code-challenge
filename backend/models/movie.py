from sqlalchemy.orm import declarative_base
from sqlalchemy     import Column, Integer, String

Base = declarative_base()

class Movie(Base):
    __tablename__ = "movies"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), index=True)
