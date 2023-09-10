import pytest

from http import HTTPStatus
from api.api import app
from fastapi.testclient import TestClient


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

def test_create_post(client):
    post_data = {
        "title": "post title",
        "content": "post content"
    }

    response = client.post("/posts", json=post_data)

    assert response.status_code == HTTPStatus.CREATED
