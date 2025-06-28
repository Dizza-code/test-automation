import requests

from utils.test_helpers import BASE_URL, get_auth_headers

# Assuming tokens of two tenants
TENANT_A_TOKEN = "token_for_tenant_A"
TENANT_B_TOKEN = "token_for_tenant_B"

def test_tenant_cannot_see_other_users():
    # Create a user in Tenant A
    user_a = requests.post(
        f"{BASE_URL}/users",
        json={"name": "Tenant A User", "email":"a@example.com", "role":"user"},
        headers=get_auth_headers(TENANT_A_TOKEN)
).json()
# Tenant B tries to fetch user A's data
response = requests.get(
    f"{BASE_URL}/users/{user_a['id']}",
    headers=get_auth_headers(TENANT_B_TOKEN)
)
assert response.status_code == 404 # should not be found for Tenant B