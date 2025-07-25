from pathlib import Path
from display_functions.material_action import issue_or_return
from helper_functions.material_display import show_materials, collect_data_edit, materials_by_exp
from helper_functions.user_display import display_user_list
from models.db import connection
from models.users import register, login, logout, show_users, delete_user, update_user_info
from models.materials import manually_adding, show_material_by, edit_material_record, show_mat_by_exp_date, issue_material, return_on_stock
from models.actions import add_action, generate_report
from display_functions.home import display_home
from display_functions.login import display_login
from display_functions.action_form import display_actions
from display_functions.wh_operations import display_wh_actions, material_display
from display_functions.user_actions import show_user_actions
from display_functions.report_display import generate_report_display
import os


# variable that is responsible for starting and closing of program
is_running = True

while is_running:
    # home screen display and login form choice
    login_entry = display_home()

    if login_entry == "1":
        os.system("cls")
        login_credentials = display_login()
        # credentials validation
        is_login = login(connection, login_credentials["username"], login_credentials["password"])

        while is_login:
            os.system("cls")
            # action choice WH/Reports/User
            action_entry = display_actions()
            if action_entry == "1":
                os.system("cls")
                wh_operations = display_wh_actions()
                # WH action section
                if wh_operations == "1":
                    os.system("cls")
                    material_action = material_display()

                    # manual addition of material on stock
                    if material_action == "1":
                        manual_addition = manually_adding(connection)
                        add_action(connection, manual_addition["action"], manual_addition["action_code"], is_login)

                # issuing or returning materials
                elif wh_operations == "2":
                    os.system("cls")
                    action = issue_or_return()

                    #issuing materials to production
                    if action == "1":
                        material_name = input("Enter material name:\n")
                        materials = show_mat_by_exp_date(connection, material_name)

                        materials_by_exp(materials)

                        mat_id = int(input("Enter material ID: "))
                        old_qty = 0
                        for mat in materials:
                            if mat["id"] == mat_id:
                                old_qty = mat["quantity"]

                        quantity = float(input("Enter quantity: "))
                        material_issued = issue_material(connection, mat_id, quantity, old_qty)
                        add_action(connection, material_issued["action"], material_issued["action_code"], is_login)

                    # returning materials on stock to wh
                    elif action == "2":
                        column_entry = input("Enter mat_name or batch: ")
                        criterion = input("Enter criterion: ")
                        material = show_material_by(connection, column_entry, criterion)

                        # handles if material that needs to be return has available qty on stock
                        if material:
                            show_materials(material, return_on_stock=True)
                            qty_to_return = float(input("Enter quantity: "))
                            mat_id = None
                            qty_on_stock = 0
                            if len(material) > 1:
                                id_entry = int(input("Enter material ID: "))
                                for mat in material:
                                    if mat["id"] == id_entry:
                                        mat_id = mat["id"]
                                        qty_on_stock = mat["quantity"]
                            else:
                                mat_id = material[0]["id"]
                                qty_on_stock = material[0]["quantity"]

                            new_qty = qty_to_return + qty_on_stock
                            ret_on_stock = return_on_stock(connection, mat_id, new_qty)
                            add_action(connection, ret_on_stock["action"], ret_on_stock["action_code"], is_login)

                        # if there is no available qty of material
                        else:
                            manually_adding(connection)
                            add_action(connection, "return on stock", 301, is_login)

                # edit of material data
                elif wh_operations == "3":
                    column_entry = input("Enter mat_name, batch or position: ")
                    criterion = input("Enter criterion: ")
                    material = show_material_by(connection, column_entry, criterion)

                    show_materials(material)

                    edit_data = collect_data_edit()

                    edit_material_record(connection, edit_data["mat_id"], edit_data["col_name"], edit_data["new_value"])

            # Report section - generating report
            elif action_entry == "2":
                os.system("cls")
                report = generate_report_display()
                project_path = Path(__file__).parent
                generate_report(connection, project_path)

            # User section - user administration add/delete/update
            elif action_entry == "3":
                os.system("cls")
                user_action = show_user_actions()

                # registration of new users
                if user_action == "1":
                    register(connection)
                # if action is delete or update show list of users
                elif user_action == "2" or "3":
                    users_list = show_users(connection)
                    column_names = display_user_list(users_list)

                    # delete user
                    if user_action == "2":
                        user_id_entry = int(input("Enter user ID: "))
                        delete_user(connection, user_id_entry)

                    # edit user data
                    elif user_action == "3":
                        id_entry = int(input("Enter user ID: "))
                        print(column_names["list"])
                        column_choice = int(input("Enter column name: "))
                        column_name = column_names["col_names"][column_choice]
                        new_info = input(f"Enter new value for column {column_name}: ")

                        update_user_info(connection, id_entry, column_name, new_info)

            # log out of user from program
            elif action_entry == "4":
                os.system("cls")
                is_login = logout()

    # exiting the program
    elif login_entry == "2":
        os.system("cls")
        print("Exiting the program...")
        is_running = False
