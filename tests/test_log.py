import pytest

from tests.config import client

data = {"user_id": 1, "travel_id": 2, "action": "add", "value": 12}
incorrect_data_var_names = {
    "user_id": 1,
    "travel_id": 2,
    "act2ion": "add",
    "val2ue": 12,
}
incorrect_data_values_types = {
    "user_id": 1,
    "travel_id": 2.4,
    "action": "add",
    "value": 12,
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
                "loc": ["body", "travel_id"],
                "msg": "field required",
                "type": "value_error.missing",
            }
        ]
    }


def test_log_with_incorrect_data_values_types():
    response = client.post(log_url, json=incorrect_data_values_types)
    assert response.status_code == 200
    assert response.json() == {
        "detail": [
            {
                "loc": ["body", 34],
                "msg": "Expecting property name enclosed in double quotes: line 3 column 18 (char 34)",
                "type": "value_error.jsondecode",
                "ctx": {
                    "msg": "Expecting property name enclosed in double quotes",
                    "doc": '{\n\t"user_id": 1,\n  "travel_id": 2,4,\n  "action": "add",\n  "value": 12\n}',
                    "pos": 34,
                    "lineno": 3,
                    "colno": 18,
                },
            }
        ]
    }
