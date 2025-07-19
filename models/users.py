import time
# from db import connection
from helper_functions.cryptograph import cipher
import os



def register(con):
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    name = input("Enter your first name: ").capitalize()
    surname = input("Enter your last name: ").capitalize()
    role = input("Enter your role: ").capitalize()
    cursor = con.cursor()
    query = ("INSERT  INTO users (username, password, name, surname, role)"
             "VALUES (%s, %s, %s, %s, %s)")

    ciphered_password = cipher(password)
    cursor.execute(query, (username, ciphered_password, name, surname, role))
    con.commit()
    cursor.close()


def login(con, username, password):
    cursor = con.cursor()
    cursor.execute("SELECT * FROM users")
    con.commit()

    result = cursor.fetchall()

    ciphered_password = cipher(password)
    is_validated = False
    message = ""

    for user in result:
        if username != user["username"] and ciphered_password == user["password"]:
            message = "Wrong username!"
            break
        elif username == user["username"] and ciphered_password != user["password"]:
            message = "Wrong password"
            break
        elif username == user["username"] and ciphered_password == user["password"]:
            is_validated = user["id"]
            message = f"User {user["name"]} {user["surname"]} is logged in"
            break
        else:
            message = "Wrong username and password!"

    print(message)
    time.sleep(1.5)
    os.system("cls")
    cursor.close()
    return is_validated


def logout():
    return False


def show_users(con):
    cursor = con.cursor()
    cursor.execute("SELECT * FROM users")
    con.commit()

    results = cursor.fetchall()

    return results


def delete_user(con, user_id):
    cursor = con.cursor()
    cursor.execute("DELETE FROM users WHERE id = %s", user_id)
    con.commit()
    cursor.close()


def update_user_info(con, user_id, column_name, new_info):
    cursor = con.cursor()

    if column_name == "password":
        new_info = cipher(new_info)

    cursor.execute(f"UPDATE users SET {column_name} = %s WHERE id = %s", (new_info, user_id))
    con.commit()
    cursor.close()





# show_users(connection)




