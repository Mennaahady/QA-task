import pytest
# Import functions from the Task.py script for testing
from Task import create_user, list_users, update_user, delete_user

# Define a fixture named user_data to provide test data for user
@pytest.fixture
def user_data():
    return {"name": "John Doe", "job": "Engineer"}

# Test function to verify the creation of a user
def test_create_user(user_data):
    response = create_user(user_data["name"], user_data["job"])
    assert response.status_code == 201
    assert "id" in response.json()

# Test function to verify listing users
def test_list_users():
    response = list_users()
    assert response.status_code == 200
    assert "data" in response.json()

# Test function to verify updating a user
def test_update_user(user_data):
    response = update_user(user_data["name"], user_data["job"])
    assert response.status_code == 200
    assert response.json()["name"] == user_data["name"]
    assert response.json()["job"] == user_data["job"]

# Test function to verify deleting a user
def test_delete_user():
    response = delete_user()
    assert response.status_code == 204
    assert response.content == b'' 