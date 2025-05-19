import os

import pytest
from fastapi.testclient import TestClient
from sqlmodel import Session, SQLModel, create_engine

from app.db.session import get_session
from app.main import app

DATABASE_URL = "sqlite:///./test.db"

# Create the engine ONCE for the whole test session
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})


@pytest.fixture(scope="session", autouse=True)
def create_test_db():
    # Remove old test DB if exists
    if os.path.exists("test.db"):
        os.remove("test.db")
    SQLModel.metadata.create_all(engine)


@pytest.fixture(name="session")
def session_fixture():
    with Session(engine) as session:
        yield session


@pytest.fixture(name="client")
def client_fixture(session):
    def get_session_override():
        yield session

    app.dependency_overrides[get_session] = get_session_override
    with TestClient(app) as c:
        yield c
