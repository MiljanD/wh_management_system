
WELCOME_MESSAGE = "Welcome to Warehouse Management System".upper()
SCREEN_LENGTH = bar_length = 50 + len(WELCOME_MESSAGE)
HEADER = "WH ACTIONS:"
MATERIAL_HEADER = "ADD MATERIAL"
BUTTON_PADDING = 5
BUTTON1 = "[ ADD MATERIALS ]"
BUTTON2 = "[ ISSUE OR RETURN ]"
BUTTON3 = "[ CORRECTIONS ]"
BUTTON4 = "[ PREVIOUS SCR ]"
BUTTONS_STARTS = (int(SCREEN_LENGTH/2) - int((len(BUTTON1)/2)+(len(BUTTON2)/2)+(len(BUTTON3)/2)+(len(BUTTON3)/2)+ BUTTON_PADDING/2))
MAT_BUTTON1 = "[ ADD FROM INVOICE ]"
MAT_BUTTON2 = "[ ADD MANUALLY ]"


def display_wh_actions():
    print(SCREEN_LENGTH * "_")
    print(f"{' ' * 25} {WELCOME_MESSAGE} {' ' * 25}")
    print(SCREEN_LENGTH * "_")
    print(f"{' ' * (int(SCREEN_LENGTH/2) - int(len(MATERIAL_HEADER)/2))}{MATERIAL_HEADER}")
    print(f"\n{' ' * (int(SCREEN_LENGTH/2) - int((len(MAT_BUTTON1)/2)+(len(MAT_BUTTON2)/2) +(len(BUTTON4)/2) + BUTTON_PADDING/2))}{MAT_BUTTON1}{' ' * BUTTON_PADDING}{MAT_BUTTON2}{' ' * BUTTON_PADDING}{BUTTON4}")

    print(SCREEN_LENGTH * "_")
    user_entry = input("Chose action: ")
    print(SCREEN_LENGTH * "-")
    return user_entry


def add_material():
    print(SCREEN_LENGTH * "_")
    print(f"{' ' * 25} {WELCOME_MESSAGE} {' ' * 25}")
    print(SCREEN_LENGTH * "_")
    print(f"{' ' * (int(SCREEN_LENGTH / 2) - int(len(MATERIAL_HEADER) / 2))}{MATERIAL_HEADER}")
    print(
        f"\n{' ' * (int(SCREEN_LENGTH / 2) - int((len(BUTTON1) / 2) + (len(BUTTON2) / 2) + BUTTON_PADDING / 2))}{BUTTON1}{' ' * BUTTON_PADDING}{BUTTON2}")

    print(SCREEN_LENGTH * "_")
    user_entry = input("Chose action: ")
    print(SCREEN_LENGTH * "-")
    return user_entry