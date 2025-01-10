import json
import os

USER_DATA_FILE = 'user_data.json'
BACKUP_FILE = 'user_data_backup.json'

def restore_from_backup():
    # Check if the backup file exists
    if not os.path.exists(BACKUP_FILE):
        print("No backup file found.")
        return

    try:
        # Load data from the backup file
        with open(BACKUP_FILE, 'r') as f:
            backup_data = json.load(f)

        # Check if the backup data is valid
        if not isinstance(backup_data, list):
            print("Invalid backup data format.")
            return

        # Load the current user data
        if os.path.exists(USER_DATA_FILE):
            with open(USER_DATA_FILE, 'r') as f:
                current_data = json.load(f)
        else:
            current_data = []

        # Add users from backup that are not already in the current data
        current_usernames = {user['username'] for user in current_data}
        for user in backup_data:
            if user['username'] not in current_usernames:
                current_data.append(user)

        # Save updated data back to the original user data file
        with open(USER_DATA_FILE, 'w') as f:
            json.dump(current_data, f, indent=4)

        print("User data has been successfully restored from the backup.")

    except Exception as e:
        print(f"Error restoring backup: {e}")
