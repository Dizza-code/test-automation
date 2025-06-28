import requests

import faker

faker = faker.Faker()

BASE_URL = "http://localhost:8000/api"

def get_auth_headers(token):
    return {"Authorization": f"Bearer {token}"}

def create_dummy_user(token):
    data = {
        "name": faker.user_name(),
        "email": faker.email(),
        "role": "user"
    }
    response = requests.post(f"{BASE_URL}/users", json=data, headers=get_auth_headers(token))
    return response

def malicious_input(): 
    return {
        "sql_injection": "' OR '1'='1",
        "xss": "<script>alert('XSS')</script>",
        "html_injection": "<h1>hacked<h1>",
        "long_string": "A" * 1000,
    }

def get_headers_for_role(role):
    #simulated token assignment
    tokens ={
        "admin": "admin_token_here",
        "user": "user_token_here",
        "attacker": "invalid_or_other_tenant_token"
    }
    return {"Authorization": f"Bearer {tokens[role]}"}
