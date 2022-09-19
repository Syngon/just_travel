# from config import client


# # list_user_travels
# # get_user_by_id
# #
# #

# username = "dawdadawdawddawdaw"
# user_id = 2


# user_get_user_by_id = f"/user/{user_id}/"
# user_get_user_by_id_incorrect_data = f"/user/{user_id+999999}/"

# user_list_travels_url = f"/user/{user_id}/travels"
# user_list_travels_url_incorrect_data = f"/user/{user_id+999999}/travels"


# def test_list_user_travels():
#     response = client.post(user_list_travels_url)
#     assert response.status_code == 200

#     res = response.json()
#     assert res["user_id"] == user_id


# def test_list_user_travels_with_incorrect_data():
#     response = client.post(user_list_travels_url_incorrect_data)
#     assert response.status_code == 400

#     res = response.json()
#     assert res == {"detail": "There is no travels for this user"}


# def test_get_user_by_id():
#     response = client.post(user_get_user_by_id)
#     assert response.status_code == 200

#     res = response.json()
#     assert res == {"user_id": user_id, "username": username}


# def test_get_user_by_id_with_incorrect_data():
#     response = client.post(user_get_user_by_id_incorrect_data)
#     assert response.status_code == 400

#     res = response.json()
#     assert res == {"detail": "There is no user with id = " + (user_id + 999999)}
