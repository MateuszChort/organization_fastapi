import pytest
from fastapi.testclient import TestClient
from app.main import app


client = TestClient(app)


def test_get_nip(nip_search_mock):
    response = client.get("/api/nip/5")
    assert response.status_code == 200
    assert response.json() == [{"NIP": "123456"}]


def test_get_nip_not_int():
    response = client.get("/api/nip/aa")
    assert response.status_code == 422


def test_get_nip_404(nip_search_mock_404):
    response = client.get("/api/nip/555")
    assert response.status_code == 404
    assert response.json()["detail"] == [{"ErrorCode": "4"}]
