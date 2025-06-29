import requests

from utils.test_helpers import BASE_URL, create_dummy_user, get_auth_headers

TOKEN = "your_test_admin_token_here"  

# create a user
def test_create_user():
    response = create_dummy_user(TOKEN)
    assert response.status_code == 201
    assert "id" in response.json()

# Test to fetch user
def test_get_user():
    created = create_dummy_user(TOKEN)
    user_id = created["id"]

    response = requests.get(f"{BASE_URL}/users/{user_id}", headers=get_auth_headers(TOKEN))
    assert response.status_code == 200
    assert response.json()["id"] == user_id

# Test to update user
def test_update_user():
    created = create_dummy_user(TOKEN)
    user_id = created["id"]
    update_data = {"name": "updated name"}
    response = requests.put(f"{BASE_URL}/user/{user_id}", json=update_data, headers=get_auth_headers(TOKEN))
    assert response.status_code == 200
    assert response.json()["name"] == "updated name"

# Test to delete user
def test_delete_user():
    created = create_dummy_user(TOKEN)
    user_id = created["id"]
    response = requests.delete(f"{BASE_URL}/users/{user_id}", headers=get_auth_headers(TOKEN))
    assert response.status_code == 204
    #verify that the user is deleted
    check = requests.get(f"{BASE_URL}/users/{user_id}", headers=get_auth_headers(TOKEN))
    assert check.status_code == 404
