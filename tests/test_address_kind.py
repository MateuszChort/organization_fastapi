from fastapi.testclient import TestClient


def test_create_address_kind(client: TestClient):
    response = client.post(
        "/address_kinds", json={"id": "address_kind_1", "kind": "test_kind"}
    )
    assert response.status_code == 201
    data = response.json()
    assert data["kind"] == "test_kind"
    assert "id" in data


def test_read_address_kinds(client: TestClient):
    client.post("/address_kinds/", json={"id": "address_kind_2", "kind": "test_kind"})
    client.post("/address_kinds/", json={"id": "address_kind_3", "kind": "test_kind2"})
    response = client.get("/address_kinds/")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert any(d["kind"] == "test_kind" for d in data)
    assert any(d["kind"] == "test_kind2" for d in data)


def test_read_address_kind_by_id(client: TestClient):
    post_response = client.post(
        "/address_kinds/", json={"id": "address_kind_4", "kind": "test_kind"}
    )
    kind_id = post_response.json()["id"]

    get_response = client.get(f"/address_kinds/{kind_id}")
    assert get_response.status_code == 200
    assert get_response.json()["kind"] == "test_kind"


def test_update_address_kind(client: TestClient):
    post_response = client.post(
        "/address_kinds/", json={"id": "address_kind_5", "kind": "test_kind"}
    )
    kind_id = post_response.json()["id"]

    put_response = client.put(f"/address_kinds/{kind_id}", json={"kind": "new"})
    assert put_response.status_code == 200
    assert put_response.json()["kind"] == "new"


def test_delete_address_kind(client: TestClient):
    post_response = client.post(
        "/address_kinds/", json={"id": "address_kind_6", "kind": "test_kind"}
    )
    kind_id = post_response.json()["id"]

    delete_response = client.delete(f"/address_kinds/{kind_id}")
    assert delete_response.status_code == 200
    assert delete_response.json() == {"deleted": kind_id}

    get_response = client.get(f"/address_kinds/{kind_id}")
    assert get_response.status_code == 404
