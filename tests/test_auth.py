from config import client

username = "ddddddjdddddaddddddddddddddddwhudih"
password = "dawdawdawd"

data = {"username": username, "password": password}
invalid_login = {"username": f"{username}123", "password": password}
invalid_password = {"username": username, "password": f"{password}12321321"}

signup_url = "/auth/signup"
login_url = "/auth/token"


# SIGNUP TESTS
def test_sign_up_with_correct_data():
    response = client.post(signup_url, json=data)
    assert response.status_code == 201

    res = response.json()
    assert isinstance(response.json()["user_id"], int)
    assert isinstance(response.json()["username"], str)
    assert isinstance(response.json()["password"], str)
    assert isinstance(response.json()["is_active"], bool)
    assert isinstance(response.json()["created_at"], str)


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
            "user_id": response.json()["user"]["user_id"],
            "username": response.json()["user"]["username"],
        },
        "access_token": response.json()["access_token"]
    }
