
WELCOME_MESSAGE = "WELCOME TO WAREHOUSE MANAGEMENT SYSTEM"
BAR_COUNT = 50
SCREEN_LENGTH = BAR_COUNT + len(WELCOME_MESSAGE)
UNDERSCORE_SEPARATION = SCREEN_LENGTH * "_"


def display_screen(header, buttons, buttons_padding, entry_message, is_login=False):
    """
    Function is used to display interface for the client.

    :param header: Title of the active screen
    :param buttons: Buttons related to certain screen
    :param buttons_padding: value that will indicate how much buttons will be separated between each other
    :param entry_message: message to client to choose desired action
    :param is_login: by default is False and functions displays screen if it is changed to true than login form will be shown
    :return: user action choice
    """

    # header of the program
    header_start = (int(SCREEN_LENGTH/2) - int(len(header)/2))
    print(UNDERSCORE_SEPARATION)
    print(f"{' ' * int(BAR_COUNT / 2)} {WELCOME_MESSAGE} {' ' * int(BAR_COUNT / 2)}")
    print(UNDERSCORE_SEPARATION)

    # login form
    if is_login:
        username_entry = input(f"Enter username: ")
        password_entry = input(f"Enter password: ")
        user_entry = {"username": username_entry, "password": password_entry}

    # screen display
    else:
        buttons_line = ""
        for idx, button in enumerate(buttons):
              if button == buttons[-1]:
                  buttons_line += f"[{idx + 1}.{button}]"
              else:
                  buttons_line += f"[{idx+1}.{button}]{' ' * buttons_padding}"

        buttons_starts = int((SCREEN_LENGTH - len(buttons_line)) / 2)


        print(f"{' ' * header_start}{header.upper()}")
        print(f"\n{' ' * buttons_starts}{buttons_line}")

        print(UNDERSCORE_SEPARATION)
        user_entry = input(f"{entry_message}")
        print(UNDERSCORE_SEPARATION)

    return user_entry
