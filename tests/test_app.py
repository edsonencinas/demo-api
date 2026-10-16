from app import app

def test_health():
    client = app.test_client()
    res = client.get("/health")
    assert res.status_code == 200
    assert res.get_json()["status"] == "ok"

def test_items():
    client = app.test_client()
    res = client.get("/api/items")
    assert res.status_code == 200
    assert len(res.get_json()) == 2
