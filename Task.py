import requests

BASE_URL = "https://reqres.in/api"
USER_ID = None  # To store the user ID created during the test

def create_user(name, job):
    global USER_ID
    endpoint = f"{BASE_URL}/users"
    data = {"name": name, "job": job}
    response = requests.post(endpoint, json=data)
    user_data = response.json()
    USER_ID = user_data.get("id")
    return response

def list_users():
    endpoint = f"{BASE_URL}/users"
    response = requests.get(endpoint)
    return response

def update_user(name, job):
    global USER_ID
    if USER_ID is None:
        raise ValueError("User ID is not available for update. Please create a user first.")
    endpoint = f"{BASE_URL}/users/{USER_ID}"
    data = {"name": name, "job": job}
    response = requests.put(endpoint, json=data)
    return response

def delete_user():
    global USER_ID
    if USER_ID is None:
        raise ValueError("User ID is not available for deletion. Please create a user first.")
    endpoint = f"{BASE_URL}/users/{USER_ID}"
    response = requests.delete(endpoint)
    USER_ID = None  # Reset USER_ID after deletion
    return response