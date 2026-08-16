import pytest
from flask import Flask
from unittest.mock import patch
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

# 1. Test GET /inventory
def test_get_all_inventory(client):
    response = client.get('/inventory')
    assert response.status_code == 200
    assert isinstance(response.get_json(), list)

# 2. Test POST /inventory
def test_add_inventory_item(client):
    payload = {
        "status": 99,
        "product": {"product_name": "Test Snack", "brands": "Test Brand"}
    }
    response = client.post('/inventory', json=payload)
    assert response.status_code == 201
    assert response.get_json()["message"] == "Item added successfully"

# 3. Test PATCH /inventory/<id>
def test_update_inventory_item(client):
    payload = {"product": {"product_name": "Updated Test Snack"}}
    response = client.patch('/inventory/99', json=payload)
    assert response.status_code == 200

# 4. Test DELETE /inventory/<id>
def test_delete_inventory_item(client):
    response = client.delete('/inventory/99')
    assert response.status_code == 200

