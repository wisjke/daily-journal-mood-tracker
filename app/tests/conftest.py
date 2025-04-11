import pytest
from fastapi.testclient import TestClient
from app.main import app
from app.db.database import get_db
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.models import models


TEST_DATABASE_URL = "postgresql://postgres:postgres@db:5432/test_db"

engine = create_engine(TEST_DATABASE_URL)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def override_get_db():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()

app.dependency_overrides[get_db] = override_get_db


@pytest.fixture(scope="session", autouse=True)
def setup_database():
    models.Base.metadata.drop_all(bind=engine)
    models.Base.metadata.create_all(bind=engine)


@pytest.fixture
def client():
    return TestClient(app)


@pytest.fixture
def auth_headers(client):
    client.post("/users", json={
        "email": "test@example.com",
        "username": "testuser",
        "password": "secret123"
    })

    response = client.post("/token", data={
        "username": "testuser",
        "password": "secret123"
    })

    token = response.json()["access_token"]
    return {"Authorization": f"Bearer {token}"}
