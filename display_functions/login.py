from .main_display import display_screen

header = "LOGIN FORM:"
buttons = None
button_padding = None
entry_message = None
is_login = True



def display_login():
    login_entry = display_screen(header, buttons, button_padding, entry_message, is_login)
    return login_entry
