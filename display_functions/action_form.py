
WELCOME_MESSAGE = "Welcome to Warehouse Management System".upper()
SCREEN_LENGTH = bar_length = 50 + len(WELCOME_MESSAGE)
HEADER = "Actions:".upper()
BUTTON_PADDING = 5
BUTTON1 = "[ WH ACTIONS ]"
BUTTON2 = "[ REPORTS ACTIONS ]"
BUTTON3 = "[ USER ACTIONS ]"
BUTTON4 = "[ LOGOUT ]"
BUTTONS_STARTS = (int(SCREEN_LENGTH/2) - int((len(BUTTON1)/2)+(len(BUTTON2)/2)+(len(BUTTON3)/2)+(len(BUTTON3)/2)+ BUTTON_PADDING/2))


def display_actions():
    print(SCREEN_LENGTH * "_")
    print(f"{' ' * 25} {WELCOME_MESSAGE} {' ' * 25}")
    print(SCREEN_LENGTH * "_")
    print(f"{' ' * (int(SCREEN_LENGTH/2) - int(len(HEADER)/2))}{HEADER}")
    print(f"\n{' ' * BUTTONS_STARTS}{BUTTON1}{' ' * BUTTON_PADDING}{BUTTON2}{' ' * BUTTON_PADDING}{BUTTON3}{' ' * BUTTON_PADDING}{BUTTON4}")

    print(SCREEN_LENGTH * "_")
    user_entry = input("Chose action: ")
    print(SCREEN_LENGTH * "-")
    return user_entry

