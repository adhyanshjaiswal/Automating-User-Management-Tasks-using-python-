import json
import os
from datetime import datetime, timedelta

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

    # Prompt the user for an expiry date
    expiry_date = input("Enter the expiry date for the user (YYYY-MM-DD): ")

    # Validate the expiry date format
    try:
        expiry_date = datetime.strptime(expiry_date, '%Y-%m-%d').strftime('%Y-%m-%d')
    except ValueError:
        print("Invalid expiry date format! Please use YYYY-MM-DD.")
        return

    # Add the new user
    new_user = {
        'username': username,
        'password': password,
        'home_directory': home_dir,
        'shell': shell,
        'expiry_date': expiry_date  # Set the expiry date provided by the user
    }
    users.append(new_user)

    # Save data back to the file
    with open(USER_DATA_FILE, 'w') as f:
        json.dump(users, f, indent=4)

    print(f"User {username} added successfully with expiry date {expiry_date}.")
