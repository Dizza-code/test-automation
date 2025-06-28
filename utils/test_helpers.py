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