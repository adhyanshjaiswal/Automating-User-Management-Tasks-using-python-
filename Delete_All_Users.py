import json
import os

USER_DATA_FILE = 'user_data.json'

def delete_all_users():
    # Check if the file exists before proceeding
    if not os.path.exists(USER_DATA_FILE):
        print("No user data file found.")
        return

    # Empty the file
    with open(USER_DATA_FILE, 'w') as f:
        json.dump([], f, indent=4)

    print("All users have been deleted successfully.")
