import requests 
from utils.test_helpers import BASE_URL, get_headers_for_role

def test_unauthorized_access():
    response = requests.get(f"{BASE_URL}/users")
    assert response == 401

def test_user_accessing_admin_route():
    headers = get_headers_for_role('user')
    response = requests.get(f"{BASE_URL}/users", json={
        "name": "not allowed",
        "email": "bad@example.com",
        "role": "admin"
    }, headers=headers)
    assert response.status_code == 403

def test_cross_tenant_user_visibility():
    attacker_headers = get_headers_for_role("attacker")
    # Assume a known user ID created by another tenant
    victim_user_id = "some_known_id"
    response = requests.get(f"{BASE_URL}/users/{victim_user_id}", headers=attacker_headers)
    assert response.status_code == 404
