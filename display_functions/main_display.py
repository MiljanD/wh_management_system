
WELCOME_MESSAGE = "WELCOME TO WAREHOUSE MANAGEMENT SYSTEM"
BAR_COUNT = 50
SCREEN_LENGTH = BAR_COUNT + len(WELCOME_MESSAGE)
UNDERSCORE_SEPARATION = SCREEN_LENGTH * "_"


def display_screen(header, buttons, buttons_padding, entry_message, is_login=False):
    header_start = (int(SCREEN_LENGTH/2) - int(len(header)/2))
    print(UNDERSCORE_SEPARATION)
    print(f"{' ' * int(BAR_COUNT / 2)} {WELCOME_MESSAGE} {' ' * int(BAR_COUNT / 2)}")
    print(UNDERSCORE_SEPARATION)


    if is_login:
        username_entry = input(f"Enter username: ")
        password_entry = input(f"Enter password: ")
        user_entry = {"username": username_entry, "password": password_entry}

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