def test_register_user(client):
    response = client.post("/users", json={
        "email": "test@example.com",
        "username": "testuser",
        "password": "secret123"
    })
    assert response.status_code == 201
    assert response.json()["email"] == "test@example.com"


def test_login(client):
    response = client.post("/token", data={
        "username": "testuser",
        "password": "secret123"
    })
    assert response.status_code == 200
    assert "access_token" in response.json()
