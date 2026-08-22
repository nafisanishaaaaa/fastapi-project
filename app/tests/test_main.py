from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_home():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {
        "message": "FastAPI started"
    }

def test_read_heroes():
    response = client.get("/heroes/")
    assert response.status_code == 200
    assert isinstance(
        response.json(),
        list
    )


def test_create_hero():
    response = client.post(
        "/heroes/",
        json={
            "name": "Spider Man",
            "age": 20,
            "secret_name": "Peter Parker"
        }
    )
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "Spider Man"
    assert data["age"] == 20
    assert data["secret_name"] == "Peter Parker"