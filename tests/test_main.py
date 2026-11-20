from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World"}


def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_create_and_read_item():
    response = client.post("/items/1", json={"name": "Pen", "price": 10.5})
    assert response.status_code == 200
    assert response.json() == {"item_id": 1, "name": "Pen", "price": 10.5}

    response = client.get("/items/1")
    assert response.status_code == 200
    assert response.json() == {"item_id": 1, "name": "Pen", "price": 10.5}
