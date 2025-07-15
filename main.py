from models.db import connection
from models.users import register, login, logout
from display_functions.home import display_home
from display_functions.login import display_login
from display_functions.action_form import display_actions
from display_functions.wh_operations import display_wh_actions, add_material
import os

user_info = ["novi", "dm3004)_", "miljan", "duvnjak", "admin"]

is_running = True

while is_running:
# register(connection, user_info[0], user_info[1], user_info[2], user_info[3], user_info[4])
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
                    add_material()

            elif action_entry == "4":
                os.system("cls")
                is_login = logout()


    elif login_entry == "2":
        os.system("cls")


        print("Exiting the program...")
        is_running = False




