import requests

from utils.test_helpers  import BASE_URL, get_headers_for_role, malicious_inputs

def test_sql_injection_login():
    payload = {
        "email": malicious_inputs()["sql_injection"],
        "password": "anyting"
    }
    response = requests.post(f"{BASE_URL}/auth/login", json=payload)
    assert response.status_code in [400, 401]

def test_xss_user_name():
    headers = get_headers_for_role("admin")
    payload = {
        "name": malicious_inputs()["xss_scripts"],
        "email": "xss@example.com",
        "role": "user"
    }
    response = requests.post(f"{BASE_URL}/users", json=payload, headers=headers)
    assert response.status_code in [400, 422]

def test_large_payload_rejection():
    headers = get_headers_for_role("admin")
    payload = {
        "name": malicious_inputs()["long_string"],
        "email": "bigpayload@example.com",
        "role": "user"
    }
    response = requests.post(f"{BASE_URL}/users", json=payload, headers=headers)
    assert response.status_code in [400, 413] # Large payloads should be rejected

    