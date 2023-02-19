from fastapi.testclient import TestClient

from ...main     import app
from ...database import get_db_session
from ...models   import movie as movie_models

client = TestClient(app)

def test_list_movies():
    db = next(get_db_session())
    db.add(movie_models.Movie(title="Foo"))
    db.commit()

    response = client.get("/movies")

    assert response.status_code == 200

    responseData = response.json()

    assert isinstance(responseData, list)
    assert len(responseData) > 0
    assert 'id' in responseData[0]
    assert 'title' in responseData[0]


def test_list_movies_limit():
    db = next(get_db_session())
    db.add(movie_models.Movie(title="Foo"))
    db.add(movie_models.Movie(title="Bar"))
    db.commit()

    response = client.get("/movies", params={"limit": 1})

    assert response.status_code == 200
    assert len(response.json()) == 1


def test_list_movies_skip():
    db = next(get_db_session())
    db.add(movie_models.Movie(title="Foo"))
    db.add(movie_models.Movie(title="Bar"))
    db.commit()

    firstResponse = client.get("/movies", params={"limit": 1})
    secondResponse = client.get("/movies", params={"limit": 1, "skip": 1})

    assert firstResponse.status_code == 200
    assert secondResponse.status_code == 200
    assert firstResponse.json()[0]["id"] != secondResponse.json()[0]["id"]
