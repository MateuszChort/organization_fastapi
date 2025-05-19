from fastapi.testclient import TestClient


def test_organization_create(client: TestClient):
    response = client.post(
        "/organizations",
        json={
            "name": "Test Organization",
            "nip": "test_org_nip",
            "regon": "test_regon",
            "krs": "test_organization_kr",
        },
    )
    assert response.status_code == 201
    data = response.json()
    assert data["name"] == "Test Organization"
    assert "id" in data


def test_organization_read(client: TestClient):
    client.post(
        "/organizations",
        json={
            "name": "Test Organization 1",
            "nip": "test_org_nip_1",
            "regon": "test_regon_1",
            "krs": "test_organization_kr_1",
        },
    )
    client.post(
        "/organizations",
        json={
            "name": "Test Organization 2",
            "nip": "test_org_nip_2",
            "regon": "test_regon_2",
            "krs": "test_organization_kr_2",
        },
    )
    response = client.get("/organizations/")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert any(d["name"] == "Test Organization 1" for d in data)
    assert any(d["name"] == "Test Organization 2" for d in data)


def test_organization_read_by_id(client: TestClient):
    post_response = client.post(
        "/organizations",
        json={
            "name": "Test Organization 3",
            "nip": "test_org_nip_3",
            "regon": "test_regon_3",
            "krs": "test_organization_kr_3",
        },
    )
    organization_id = post_response.json()["id"]

    get_response = client.get(f"/organizations/{organization_id}")
    assert get_response.status_code == 200
    assert get_response.json()["name"] == "Test Organization 3"


def test_organization_update(client: TestClient):
    post_response = client.post(
        "/organizations",
        json={
            "name": "Test Organization 4",
            "nip": "test_org_nip_4",
            "regon": "test_regon_4",
            "krs": "test_organization_kr_4",
        },
    )
    organization_id = post_response.json()["id"]

    put_response = client.put(
        f"/organizations/{organization_id}",
        json={"name": "Updated Organization"},
    )
    assert put_response.status_code == 200
    assert put_response.json()["name"] == "Updated Organization"


def test_organization_delete(client: TestClient):
    post_response = client.post(
        "/organizations",
        json={
            "name": "Test Organization 5",
            "nip": "test_org_nip_5",
            "regon": "test_regon_5",
            "krs": "test_organization_kr_5",
        },
    )
    organization_id = post_response.json()["id"]
    delete_response = client.delete(f"/organizations/{organization_id}")
    assert delete_response.status_code == 204
