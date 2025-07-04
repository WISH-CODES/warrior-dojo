from fastapi.testclient import TestClient
from .conftest import client  # This uses the client fixture

def test_register(client: TestClient):
    res = client.post("/register", json={"email": "test@example.com", "password": "testpass"})
    assert res.status_code == 200
    assert res.json()["email"] == "test@example.com"

def test_login(client: TestClient):
    res = client.post("/login", data={"username": "test@example.com", "password": "testpass"})
    assert res.status_code == 200
    assert "access_token" in res.json()
