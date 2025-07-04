import pytest

@pytest.fixture
def token(client):
    res = client.post("/login", data={"username": "test@example.com", "password": "testpass"})
    return res.json()["access_token"]

headers = lambda token: {"Authorization": f"Bearer {token}"}

def test_create_warrior(client, token):
    res = client.post("/warriors/", json={"name": "Hanzo", "skill": "stealth"}, headers=headers(token))
    assert res.status_code == 200
    assert res.json()["name"] == "Hanzo"

def test_get_warriors(client, token):
    res = client.get("/warriors/", headers=headers(token))
    assert res.status_code == 200
    assert isinstance(res.json(), list)

def test_update_warrior(client, token):
    res = client.put("/warriors/1", json={"name": "Hanzo Elite", "skill": "shadow"}, headers=headers(token))
    assert res.status_code == 200
    assert res.json()["name"] == "Hanzo Elite"

def test_delete_warrior(client, token):
    res = client.delete("/warriors/1", headers=headers(token))
    assert res.status_code == 200
    assert res.json()["msg"] == "Warrior deleted"
