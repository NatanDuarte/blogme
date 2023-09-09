from api.api import app

from fastapi.testclient import TestClient
from http import HTTPStatus


@pytest.fixture
def client():
    return TestClient(app)

def test_when_verify_integrity_should_return_200(client):
    response = client.get("/healthcheck")
    assert response.status_code == HTTPStatus.OK

def test_when_verify_integrity_format_should_be_json(client):
    response = client.get("/healthcheck")
    assert response.headers["Content-Type"] == "application/json"

def test_respose_should_have_content(client):
    response = client.get("/healthcheck")
    assert response.json() == {"status": "ok"}
