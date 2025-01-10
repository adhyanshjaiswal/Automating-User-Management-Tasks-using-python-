import json
from datetime import datetime

USER_DATA_FILE = 'user_data.json'

def check_password_expiry(username):
    try:
        with open(USER_DATA_FILE, 'r') as f:
            users = json.load(f)
    except FileNotFoundError:
        print("No user data found.")
        return

    # Find the user by username
    user_found = False
    for user in users:
        if user['username'] == username:
            user_found = True
            if 'expiry_date' not in user:
                print(f"No expiry date set for user {username}.")
                return  # Exit or prompt for expiry date setting
            # Continue with the expiry date check if it exists
            expiry_date = datetime.strptime(user['expiry_date'], '%Y-%m-%d')
            current_date = datetime.now()
            if current_date > expiry_date:
                print(f"Password for {username} has expired! Please reset your password.")
            else:
                print(f"Password for {username} is valid. Expiry date: {user['expiry_date']}.")
            break

    if not user_found:
        print(f"User {username} not found!")
