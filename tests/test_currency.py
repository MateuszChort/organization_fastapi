from fastapi.testclient import TestClient


def test_create_currency(client: TestClient):
    response = client.post(
        "/currencies", json={"code": "code1", "name": "Test Currency"}
    )
    assert response.status_code == 201
    data = response.json()
    assert data["name"] == "Test Currency"
    assert "code" in data


def test_read_currencies(client: TestClient):
    client.post("/currencies/", json={"code": "code2", "name": "Test Currency"})
    client.post("/currencies/", json={"code": "code3", "name": "Test Currency2"})
    response = client.get("/currencies/")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert any(d["name"] == "Test Currency" for d in data)
    assert any(d["name"] == "Test Currency2" for d in data)


def test_read_currency_by_code(client: TestClient):
    post_response = client.post(
        "/currencies/", json={"code": "code4", "name": "Test Currency"}
    )
    currency_code = post_response.json()["code"]

    get_response = client.get(f"/currencies/{currency_code}")
    assert get_response.status_code == 200
    assert get_response.json()["name"] == "Test Currency"


def test_update_currency(client: TestClient):
    post_response = client.post(
        "/currencies/", json={"code": "code5", "name": "Test Currency"}
    )
    currency_code = post_response.json()["code"]

    put_response = client.put(f"/currencies/{currency_code}", json={"name": "new"})
    assert put_response.status_code == 200
    assert put_response.json()["name"] == "new"


def test_delete_currency(client: TestClient):
    post_response = client.post(
        "/currencies/", json={"code": "code6", "name": "Test Currency"}
    )
    currency_code = post_response.json()["code"]

    delete_response = client.delete(f"/currencies/{currency_code}")
    assert delete_response.status_code == 200
    assert delete_response.json() == {"deleted": currency_code}

    get_response = client.get(f"/currencies/{currency_code}")
    assert get_response.status_code == 404
