
from models.db import connection
from models.users import register, login, logout, show_users, delete_user, update_user_info
from models.materials import manually_adding
from models.actions import add_action
from display_functions.home import display_home
from display_functions.login import display_login
from display_functions.action_form import display_actions
from display_functions.wh_operations import display_wh_actions, add_material_display
from display_functions.user_actions import show_user_actions
import os



is_running = True

while is_running:
    login_entry = display_home()

    if login_entry == "1":
        os.system("cls")
        login_credentials = display_login()
        is_login = login(connection, login_credentials["username"], login_credentials["password"])
        while is_login:
            os.system("cls")
            action_entry = display_actions()
            if action_entry == "1":
                os.system("cls")
                wh_operations = display_wh_actions()
                if wh_operations == "1":
                    os.system("cls")
                    material_add = add_material_display()
                    if material_add == "2":
                        manual_addition = manually_adding(connection)
                        add_action(connection, manual_addition["action"], manual_addition["action_code"], is_login)

            elif action_entry == "3":
                os.system("cls")
                user_action = show_user_actions()
                if user_action == "1":
                    register(connection)
                elif user_action == "2" or "3":
                    users_list = show_users(connection)
                    column_names = []
                    for idx, user in enumerate(users_list):
                        column_names = [key for key, value in user.items()]
                        list_line = f"\n{idx + 1}. User ID: {user["id"]} User full name: {user["name"].capitalize()} {user["surname"].capitalize()} User role: {user["role"]}"
                        print(list_line)
                        print("-" * len(list_line))
                    if user_action == "2":
                        user_id_entry = int(input("Enter user ID: "))
                        delete_user(connection, user_id_entry)

                    elif user_action == "3":
                        id_entry = int(input("Enter user ID: "))
                        column_list = ""
                        for idx, column in enumerate(column_names[1:]):
                            column_list += f"{idx +1 }. Column name: {column}{' ' * 2}"
                        print(column_list)
                        column_choice = int(input("Enter column name: "))
                        column_name = column_names[column_choice]
                        new_info = input(f"Enter new value for column {column_name}: ")

                        update_user_info(connection, id_entry, column_name, new_info)

            elif action_entry == "4":
                os.system("cls")
                is_login = logout()

    elif login_entry == "2":
        os.system("cls")
        print("Exiting the program...")
        is_running = False




