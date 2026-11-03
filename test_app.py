import pytest

from app import add, app


@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


def test_add_function():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0


def test_index(client):
    response = client.get("/")
    assert response.status_code == 200
    data = response.get_json()
    assert data["message"] == "Hello from the Harness lab app!"
    assert "version" in data


def test_health(client):
    response = client.get("/health")
    assert response.status_code == 200
    assert response.get_json() == {"status": "ok"}


def test_version(client):
    response = client.get("/version")
    assert response.status_code == 200
    assert "version" in response.get_json()


def test_add_route(client):
    response = client.get("/add?a=2&b=3")
    assert response.status_code == 200
    assert response.get_json()["result"] == 5


def test_add_route_missing_params(client):
    response = client.get("/add?a=2")
    assert response.status_code == 400


def test_add_route_invalid_params(client):
    response = client.get("/add?a=two&b=3")
    assert response.status_code == 400
