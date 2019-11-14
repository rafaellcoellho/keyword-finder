from starlette.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_alive():
    res = client.get("/alive")
    assert res.status_code == 200
    assert res.json() == {"text": "RUNNING"}
