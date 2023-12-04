import pytest
from Task import create_user, list_users, update_user, delete_user

@pytest.fixture
def user_data():
    return {"name": "John Doe", "job": "Engineer"}

def test_create_user(user_data):
    response = create_user(user_data["name"], user_data["job"])
    assert response.status_code == 201
    assert "id" in response.json()

def test_list_users():
    response = list_users()
    assert response.status_code == 200
    assert "data" in response.json()

def test_update_user(user_data):
    response = update_user(user_data["name"], user_data["job"])
    assert response.status_code == 200
    assert response.json()["name"] == user_data["name"]
    assert response.json()["job"] == user_data["job"]

def test_delete_user():
    response = delete_user()
    assert response.status_code == 204
    assert response.content == b'' 