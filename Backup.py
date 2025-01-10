import json
import shutil
import os

USER_DATA_FILE = 'user_data.json'
BACKUP_FILE = 'user_data_backup.json'

def create_backup():
    try:
        if os.path.exists(USER_DATA_FILE):
            shutil.copy(USER_DATA_FILE, BACKUP_FILE)
            print(f"Backup of user data created successfully: {BACKUP_FILE}")
        else:
            print("User data file does not exist, cannot create a backup.")
    except Exception as e:
        print(f"Error creating backup: {e}")
