from config import client

data = {"user_id": 1, "travel_id": 2, "action": "add", "value": 12}
incorrect_data_var_names = {
    "user_id": 1,
    "travel_id": 2,
    "act2ion": "add",
    "val2ue": 12,
}

log_url = "/log"


def test_log_with_correct_data():
    response = client.post(log_url, json=data)
    assert response.status_code == 200
    assert response.json() == {"OK": "Mensagem enviada"}


def test_log_with_incorrect_data_var_names():
    response = client.post(log_url, json=incorrect_data_var_names)
    assert response.status_code == 422
    assert response.json() == {
        "detail": [
            {
                "loc": ["body", "action"],
                "msg": "field required",
                "type": "value_error.missing",
            },
            {
                "loc": ["body", "value"],
                "msg": "field required",
                "type": "value_error.missing",
            },
        ]
    }

