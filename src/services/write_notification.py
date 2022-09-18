def write_notification(user_id: int, travel_id: int, action: str, value: float):
    with open('log.txt', mode='a') as log_file:
        content = f'User: {user}, Travel: {travel_id}, Action: {action}, value {value}'
        log_file.write(content)
