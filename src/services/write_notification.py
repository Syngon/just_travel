def write_notification(user_id: int, travel_id: int, action: str, value: float):
    with open(f'log.txt_{user_id}_{travel_id}', mode='a') as log_file:
        content = f'User: {user_id}, Travel: {travel_id}, Action: {action}, value {value}'
        log_file.write(content)
