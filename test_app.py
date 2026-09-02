from app import app


def test_home():
    client = app.test_client()

    response = client.get("/")

    assert response.status_code == 200


def test_health():
    client = app.test_client()

    response = client.get("/api/health")

    assert response.status_code == 200
    assert response.json["status"] == "UP"


def test_add():
    client = app.test_client()

    response = client.get("/api/add?a=10&b=20")

    assert response.status_code == 200
    assert response.json["result"] == 30


def test_add_missing_parameters():
    client = app.test_client()

    response = client.get("/api/add")

    assert response.status_code == 400
