from app import app


def test_home(monkeypatch):
    monkeypatch.setenv("APP_ENV", "development")
    response = app.test_client().get("/")
    assert response.status_code == 200
    assert response.get_json()["environment"] == "development"


def test_health(monkeypatch):
    monkeypatch.setenv("APP_ENV", "staging")
    response = app.test_client().get("/health")
    assert response.status_code == 200
    assert response.get_json() == {
        "status": "ok",
        "environment": "staging",
    }


def test_version(monkeypatch):
    monkeypatch.setenv("BUILD_SHA", "test-commit")
    response = app.test_client().get("/version")
    assert response.status_code == 200
    assert response.get_json()["commit"] == "test-commit"
