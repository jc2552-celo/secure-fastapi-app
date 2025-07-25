from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_create_user():
    response = client.post("/users/", json={
        "username": "testuser",
        "email": "test@example.com",
        "password": "testpassword"
    })
    assert response.status_code == 200
    data = response.json()
    assert data["username"] == "testuser"
    assert data["email"] == "test@example.com"
    assert "password" not in data

def test_create_user_missing_field():
    response = client.post("/users/", json={
        "username": "incomplete"
        # Missing email and password
    })
    assert response.status_code == 422

def test_duplicate_user():
    user_data = {
        "username": "dupeuser",
        "email": "dupe@example.com",
        "password": "dupepass"
    }
    client.post("/users/", json=user_data)  # First creation
    response = client.post("/users/", json=user_data)  # Duplicate
    assert response.status_code == 400
