from fastapi.testclient import TestClient

from ..main import app

client = TestClient(app)


def test_root_page() -> None:
    response = client.get("/", follow_redirects=False)

    assert response.status_code == 307
    assert response.headers['Location'] == "/docs"
