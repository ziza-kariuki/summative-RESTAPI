import pytest
from flask import Flask
from unittest.mock import patch
from app import app

# Test External API call using Mock (Simulates OpenFoodFacts response)
@patch('app.requests.get')
def test_mock_external_api(mock_get, client):
    # Setup the fake network response
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {
        "status": 1,
        "product": {
            "product_name": "Mocked Cereal",
            "brands": "Mock Brand",
            "ingredients_text": "Mock Wheat"
        }
    }

    # Execute request
    response = client.get('/external/123456')
    
    # Assertions
    assert response.status_code == 200
    data = response.get_json()
    assert data["product"]["product_name"] == "Mocked Cereal"