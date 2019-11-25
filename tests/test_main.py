from starlette.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_alive():
    res = client.get("/alive")
    assert res.status_code == 200
    assert res.json() == {"text": "RUNNING"}


def test_search_word():
    example_search = {
        "word": "python",
        "urls": ["https://www.python.org/"]
    }
    res = client.post("/", json=example_search)
    assert res.json() == {
        "search": [
            {"word": "python", "count": 1, "url": "https://www.python.org/"}
        ]
    }
