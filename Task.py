# Import the requests library for making HTTP requests
import requests

# Define the base URL of the Reqres API
BASE_URL = "https://reqres.in/api"
# Global variable to store the user ID created during the test
USER_ID = None  

# Function to create a user by making a POST request
def create_user(name, job):
    global USER_ID
    endpoint = f"{BASE_URL}/users"
    data = {"name": name, "job": job}
    response = requests.post(endpoint, json=data)
    user_data = response.json()
    USER_ID = user_data.get("id")
    return response

# Function to list users by making a GET request
def list_users():
    endpoint = f"{BASE_URL}/users"
    response = requests.get(endpoint)
    return response

# Function to update a user by making a PUT request
def update_user(name, job):
    global USER_ID
    if USER_ID is None:
        raise ValueError("User ID is not available for update. Please create a user first.")
    endpoint = f"{BASE_URL}/users/{USER_ID}"
    data = {"name": name, "job": job}
    response = requests.put(endpoint, json=data)
    return response

# Function to delete a user by making a DELETE request
def delete_user():
    global USER_ID
    if USER_ID is None:
        raise ValueError("User ID is not available for deletion. Please create a user first.")
    endpoint = f"{BASE_URL}/users/{USER_ID}"
    response = requests.delete(endpoint)
    USER_ID = None  
    return response