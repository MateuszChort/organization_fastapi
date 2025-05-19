from fastapi.testclient import TestClient


def test_create_bank_account(client: TestClient):
    currency = client.post("/currencies", json={"code": "USD", "name": "US Dollar"})
    organization = client.post(
        "/organizations",
        json={
            "name": "Test Organization",
            "nip": "test_org_nip",
            "regon": "test_regon",
        },
    )
    response = client.post(
        "/bank_accounts",
        json={
            "number": "1234567890",
            "is_active": True,
            "main_account": True,
            "currency_code": currency.json()["code"],
            "organization_id": organization.json()["id"],
        },
    )
    assert response.status_code == 201
    data = response.json()
    assert data["number"] == "1234567890"
    assert "id" in data


def test_read_bank_accounts(client: TestClient):
    currency = client.post("/currencies", json={"code": "PLN", "name": "Polish Zloty"})
    client.post(
        "/bank_accounts",
        json={
            "number": "12 2000 1234 5678 9012 3456 7890",
            "is_active": True,
            "main_account": True,
            "currency_code": currency.json()["code"],
        },
    )
    response = client.get("/bank_accounts/")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert any(d["number"] == "1234567890" for d in data)


def test_read_bank_account_by_id(client: TestClient):
    currency = client.post("/currencies", json={"code": "CHF", "name": "Swiss Franc"})
    post_response = client.post(
        "/bank_accounts",
        json={
            "number": "12 2000 1234 5678 9012 3456 9999",
            "is_active": True,
            "main_account": True,
            "currency_code": currency.json()["code"],
        },
    )
    bank_account_id = post_response.json()["id"]

    get_response = client.get(f"/bank_accounts/{bank_account_id}")
    assert get_response.status_code == 200
    assert get_response.json()["number"] == "12 2000 1234 5678 9012 3456 9999"


def test_update_bank_account(client: TestClient):
    currency = client.post("/currencies", json={"code": "GBP", "name": "British Pound"})
    post_response = client.post(
        "/bank_accounts",
        json={
            "number": "12 2000 1234 5678 9012 3456 8888",
            "is_active": True,
            "main_account": True,
            "currency_code": currency.json()["code"],
        },
    )
    bank_account_id = post_response.json()["id"]

    put_response = client.put(
        f"/bank_accounts/{bank_account_id}",
        json={"number": "new_number", "is_active": False},
    )
    assert put_response.status_code == 200
    assert put_response.json()["number"] == "new_number"


def test_delete_bank_account(client: TestClient):
    currency = client.post("/currencies", json={"code": "JPY", "name": "Japanese Yen"})
    post_response = client.post(
        "/bank_accounts",
        json={
            "number": "12 2000 1234 5678 9012 3456 7777",
            "is_active": True,
            "main_account": True,
            "currency_code": currency.json()["code"],
        },
    )
    bank_account_id = post_response.json()["id"]

    delete_response = client.delete(f"/bank_accounts/{bank_account_id}")
    assert delete_response.status_code == 200
    assert delete_response.json() == {"deleted": bank_account_id}

    get_response = client.get(f"/bank_accounts/{bank_account_id}")
    assert get_response.status_code == 404
