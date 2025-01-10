import json

USER_DATA_FILE = 'user_data.json'

def forgot_password(username):
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
            # Ask for the new password
            new_password = input(f"Enter new password for {username}: ")
            user['password'] = new_password  # Update the password
            break

    if not user_found:
        print(f"User {username} not found!")
        return

    # Save updated data
    with open(USER_DATA_FILE, 'w') as f:
        json.dump(users, f, indent=4)

    print(f"Password for {username} has been successfully updated.")
