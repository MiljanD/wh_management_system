from helper_functions.cryptograph import cipher



def register(con, username, password, name, surname, role):
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
        elif username == user["username"] and ciphered_password != user["password"]:
            message = "Wrong password"
        elif username == user["username"] and ciphered_password == user["password"]:
            is_validated = True
            message = f"User {user["name"]} {user["surname"]} is logged in"
        else:
            message = "Wrong username and password!"

    print(message)
    return is_validated


def logout():
    return False




