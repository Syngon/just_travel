import pytest
import json

from tests.config import client

username = "Pedr2231321312321312322o"
password = "Pedr231232122o"

data = {"username": username, "password": password}
invalid_login = {"username": f"{username}123", "password": password}
invalid_password = {"username": username, "password": f"{password}12321321"}

signup_url = "/auth/signup/"
login_url = "/auth/token/"


# SIGNUP TESTS
def test_sign_up_with_correct_data():
    response = client.post(signup_url, json=data)
    assert response.status_code == 201

    res = response.json()
    assert res["user_id"] == pytest.isinstance(response.json()["user_id"], int)
    assert res["username"] == pytest.isinstance(response.json()["username"], str)
    assert res["password"] == pytest.isinstance(response.json()["password"], str)
    assert res["is_active"] == pytest.isinstance(response.json()["is_active"], bool)
    assert res["created_at"] == pytest.isinstance(response.json()["created_at"], str)


def test_existing_username_sign_up():
    response = client.post(signup_url, json=data)
    assert response.status_code == 400
    assert response.json() == {"detail": "User already exists"}


incorrect_data = {
    "username": username,
    "password": password,
    "confirm_password": password,
}


def test_data_with_incorrect_info_sign_up():
    response = client.post(signup_url, json=incorrect_data)
    assert response.status_code == 400
    assert response.json() == {"detail": "User already exists"}


#
#
#
#
#
#
#
#
#
#
#
#
#
#

# LOGIN TESTS
def test_login_by_invalid_username():
    response = client.post(login_url, json=invalid_login)
    assert response.status_code == 400
    assert response.json() == {"detail": "Wrong data, please use the correct data!"}


def test_login_by_invalid_password():
    response = client.post(login_url, json=invalid_password)
    assert response.status_code == 400
    assert response.json() == {"detail": "Password is not valid!"}


def test_valid_login():
    response = client.post(login_url, json=data)
    assert response.status_code == 200
    assert response.json() == {
        "user": {
            "user_id": response.json()["access"]["user_id"],
            "username": response.json()["access"]["username"],
        },
        "access_token": response.json()["access_token"],
    }
