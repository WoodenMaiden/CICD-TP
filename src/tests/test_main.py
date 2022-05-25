"""
Test main module
"""

import json


def test_post_city(client):
    """Test to create a new city"""
    city = {
        "id": 1,
        "department_code": 34,
        "insee_code": "34000",
        "zip_code": "34000",
        "name": "Montpellier",
        "lat": 1.0,
        "lon": 1.0,
    }

    response = client.post(
        "/city", data=json.dumps(city), content_type="application/json"
    )
    assert response.status_code == 201


def test_get_city(client):
    """Test to get all cities"""
    response = client.get("/city")
    assert response.status_code == 200


def test_health(client):
    """Test to get health check"""
    response = client.get("/_health")
    assert response.status_code == 204
