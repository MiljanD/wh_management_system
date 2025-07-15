
WELCOME_MESSAGE = "Welcome to Warehouse Management System".upper()
SCREEN_LENGTH = bar_length = 50 + len(WELCOME_MESSAGE)
HEADER = "LOGIN FORM:"



def display_login():
    print(SCREEN_LENGTH * "_")
    print(f"{' ' * 25} {WELCOME_MESSAGE} {' ' * 25}")
    print(SCREEN_LENGTH * "_")
    print(f"{' ' * (int(SCREEN_LENGTH/2) - int(len(HEADER)/2))}{HEADER}")
    username_entry = input(f"Enter username: ")
    password_entry = input(f"Enter password: ")

    print(f"\n{SCREEN_LENGTH * '_'}")

    return {"username": username_entry, "password": password_entry}
