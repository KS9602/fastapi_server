import pytest
from fastapi.testclient import TestClient
from main import app
from database import Base, SQLALCHEMY_DATABASE_URL, get_db
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine("postgresql://postgres:admin@localhost/party_test")

TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

@pytest.fixture()
def session():

    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)

    db = TestingSessionLocal()

    try:
        yield db
    finally:
        db.close()
@pytest.fixture()
def client(session):

    # Dependency override

    def override_get_db():
        try:
            yield session
        finally:
            session.close()

    app.dependency_overrides[get_db] = override_get_db

    yield TestClient(app)



def test_read_get_user(client):
    response = client.get('/all_users')
    assert response.status_code == 200

def test_create_user(client):

    payload = {
        'username':'testowy',
        'password':'testowe'
    }
    response = client.post('/add_user',json=payload)
    assert response.status_code == 201
    assert response.json() == {'db_user':'created'}

def test_read_get_by_parameter(client):
    payload = {
        'username':'testowy',
        'password':'testowe'
    }
    response = client.post('/add_user',json=payload)
    response = client.get('/get_user/1')
    assert response.status_code == 200
    assert response.json()['username'] == 'testowy'


