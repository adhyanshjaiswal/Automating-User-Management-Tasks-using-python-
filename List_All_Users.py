import json

USER_DATA_FILE = 'user_data.json'

def list_users():
    try:
        with open(USER_DATA_FILE, 'r') as f:
            users = json.load(f)
    except FileNotFoundError:
        print("No user data found.")
        return

    if not users:
        print("No users found.")
        return

    print("Current Users:")
    for user in users:
        print(f"Username: {user['username']}, Home: {user['home_directory']}, Shell: {user['shell']}")
