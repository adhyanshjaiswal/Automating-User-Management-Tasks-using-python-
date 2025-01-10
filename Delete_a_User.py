import json

USER_DATA_FILE = 'user_data.json'

def delete_user(username):
    try:
        with open(USER_DATA_FILE, 'r') as f:
            users = json.load(f)
    except FileNotFoundError:
        print("No user data found.")
        return

    # Remove user if found
    users = [user for user in users if user['username'] != username]

    # Save updated data
    with open(USER_DATA_FILE, 'w') as f:
        json.dump(users, f, indent=4)

    print(f"User {username} deleted successfully.")
