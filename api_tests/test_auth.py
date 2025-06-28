# verify login, logout, token validation

import requests

BASE_URL = "http://localhost:8000/api"

def test_login_valid_user():
    response = requests.post(f"{BASE_URL}/auth/login", json={
        "email": "admin@example.com",
        "password": "securepassword"
    })
    assert response.status_code == 200
    assert "token" in response.json()

def test_login_invalid_user():
    response = requests.post(f"{BASE_URL}/auth/login", json={
        "email":"fake@example.com",
        "password": "wrongpassword"
    })
    assert response.status_code == 401

def test_token_validation():
    # no token
    response = requests.get(f"{BASE_URL}/users")
    assert response.status_code == 401