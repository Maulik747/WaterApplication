from fastapi.testclient import TestClient
from app.main import app
from datetime import datetime

client = TestClient(app)


def test_health_check():
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {
        "status": "healthy"
    }


def test_hello_endpoint():
    response = client.get("/hello?name=Alice")

    assert response.status_code == 200
    assert response.json() == {
        "message": "Hello, Alice!"
    }


def test_calculate_age():
    current_year = datetime.now().year

    response = client.get(
        "/calculate-age?year_of_birth=2000"
    )

    expected_age = current_year - 2000

    assert response.status_code == 200
    assert response.json() == {
        "year_of_birth": 2000,
        "age": expected_age
    }