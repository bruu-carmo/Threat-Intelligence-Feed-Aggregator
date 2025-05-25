from fastapi.testclient import TestClient
from threat_intelligence_aggregator.api import app

client = TestClient(app)


def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json()["status"] == "running"


def test_status():
    response = client.get("/status")
    assert response.status_code == 200
    assert response.json() == {"status": "OK"}


def test_list_feeds():
    response = client.get("/feeds")
    assert response.status_code == 200
    assert "feeds" in response.json()


def test_lookup_ioc():
    response = client.get("/lookup/testioc")
    assert response.status_code == 200
    assert response.json()["ioc"] == "testioc"
