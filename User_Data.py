import json
import os

USER_DATA_FILE = 'user_data.json'

def add_user(username, password, home_dir, shell):
    # Check if the file exists, if not, create an empty JSON file
    if not os.path.exists(USER_DATA_FILE):
        with open(USER_DATA_FILE, 'w') as f:
            json.dump([], f)
    
    # Load existing data
    try:
        with open(USER_DATA_FILE, 'r') as f:
            users = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        users = []

    # Check if user already exists
    for user in users:
        if user['username'] == username:
            print(f"User {username} already exists!")
            return

    # Add the new user
    new_user = {
        'username': username,
        'password': password,
        'home_directory': home_dir,
        'shell': shell
    }
    users.append(new_user)

    # Save data back to the file
    with open(USER_DATA_FILE, 'w') as f:
        json.dump(users, f, indent=4)

    print(f"User {username} added successfully.")
