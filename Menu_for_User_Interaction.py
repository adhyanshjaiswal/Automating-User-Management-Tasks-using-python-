from Add_a_User import add_user
from Delete_a_User import delete_user
from List_All_Users import list_users
from Forgot_Password import forgot_password
from Check_Password_Expiry import check_password_expiry
from Backup import create_backup
from Delete_All_Users import delete_all_users
from Restore_Backup import restore_from_backup

def main_menu():
    while True:
        print("------------------------")
        print("User Management System")
        print("1. Add a User")
        print("2. Delete a User")
        print("3. List All Users")
        print("4. Forgot Password")
        print("5. Check Password Expiry")
        print("6. Create Backup")
        print("7. Delete All Users")
        print("8. Restore from Backup")
        print("9. Exit")
        print("------------------------")

        choice = input("Enter your choice: ")
        

        print("------------------------")

        if choice == '1':
            username = input("Enter username: ")
            password = input("Enter password: ")
            home_dir = input("Enter home directory: ")
            shell = input("Enter shell: ")
            add_user(username, password, home_dir, shell)
        elif choice == '2':
            username = input("Enter username to delete: ")
            delete_user(username)
        elif choice == '3':
            list_users()
        elif choice == '4':
            username = input("Enter username for password reset: ")
            forgot_password(username)
        elif choice == '5':
            username = input("Enter username to check password expiry: ")
            check_password_expiry(username)
        elif choice == '6':
            create_backup()
        elif choice == '7':
            delete_all_users()
        elif choice == '8':
            restore_from_backup()
        elif choice == '9':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main_menu()
