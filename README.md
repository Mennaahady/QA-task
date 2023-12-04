# API Automation with Pytest

This project demonstrates API automation using Pytest and Python for the Reqres API (https://reqres.in/).

## Table of Contents

- [Overview](#overview)
- [Setup](#setup)
- [Usage](#usage)
- [Test Cases](#test-cases)

## Overview

The project includes a Python script (`Task.py`) with functions for interacting with the Reqres API, covering operations such as user creation, listing users, updating users, and deleting users. Pytest test cases are written in `tasktest.py` to verify the functionality of these API operations.

## Setup

1. **Clone the Repository:**
   ```
   git clone <repository_url>
   cd <repository_directory>
   ```
Install Dependencies:
bash
Copy code
pip install -r requirements.txt
Usage
Ensure that you have Python and Pytest installed. To run the tests, execute the following command in your terminal:
```
pytest test_api.py
```
## Test Cases
Create User:

Verifies the successful creation of a user.
List Users:

Verifies the successful listing of users.
Update User:

Verifies the successful update of a user.
Delete User:

Verifies the successful deletion of a user.





