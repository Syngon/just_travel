import os


def write_notification(user_id: int, travel_id: int, action: str, value: float):

    filename = f"logs/{user_id}/{travel_id}/log.txt_{user_id}_{travel_id}"
    os.makedirs(os.path.dirname(filename), exist_ok=True)

    with open(filename, mode="a") as log_file:
        content = (
            f"User: {user_id}, Travel: {travel_id}, Action: {action}, Value: {value}\n"
        )
        log_file.write(content)
