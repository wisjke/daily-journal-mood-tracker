import pytest
from app.main import app
from fastapi.testclient import TestClient


def test_root():
    client = TestClient(app)
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to Journal & Mood Tracker API"}