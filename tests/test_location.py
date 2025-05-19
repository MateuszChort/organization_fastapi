from fastapi.testclient import TestClient


def test_create_location(client: TestClient):
    response = client.post(
        "/locations",
        json={
            "name": "Test Location",
            "code": "test_location_code",
            "location_kind": "CR",
        },
    )
    response_with_parent = client.post(
        "/locations",
        json={
            "name": "Test Location with Parent",
            "code": "test_location_code_parent",
            "location_kind": "RG",
            "parent_location_id": 1,
        },
    )
    assert response.status_code == 201
    assert response_with_parent.status_code == 201
    data = response.json()
    assert data["name"] == "Test Location"
    assert "id" in data


def test_read_locations(client: TestClient):
    client.post(
        "/locations",
        json={
            "name": "Test Location 1",
            "code": "test_location_code_1",
            "location_kind": "CR",
        },
    )
    client.post(
        "/locations",
        json={
            "name": "Test Location 2",
            "code": "test_location_code_2",
            "location_kind": "RG",
        },
    )
    response = client.get("/locations/")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert any(d["name"] == "Test Location 1" for d in data)
    assert any(d["name"] == "Test Location 2" for d in data)


def test_read_location_by_id(client: TestClient):
    post_response = client.post(
        "/locations",
        json={
            "name": "Test Location 3",
            "code": "test_location_code_3",
            "location_kind": "CR",
        },
    )
    location_id = post_response.json()["id"]

    get_response = client.get(f"/locations/{location_id}")
    assert get_response.status_code == 200
    assert get_response.json()["name"] == "Test Location 3"


def test_update_location(client: TestClient):
    post_response = client.post(
        "/locations",
        json={
            "name": "Test Location 4",
            "code": "test_location_code_4",
            "location_kind": "CR",
        },
    )
    location_id = post_response.json()["id"]

    put_response = client.put(
        f"/locations/{location_id}", json={"name": "new", "location_kind": "RG"}
    )
    assert put_response.status_code == 200
    assert put_response.json()["name"] == "new"


def test_delete_location(client: TestClient):
    post_response = client.post(
        "/locations",
        json={
            "name": "Test Location 5",
            "code": "test_location_code_5",
            "location_kind": "CR",
        },
    )
    location_id = post_response.json()["id"]

    delete_response = client.delete(f"/locations/{location_id}")
    assert delete_response.status_code == 200
    assert delete_response.json() == {"deleted": location_id}

    get_response = client.get(f"/locations/{location_id}")
    assert get_response.status_code == 404
