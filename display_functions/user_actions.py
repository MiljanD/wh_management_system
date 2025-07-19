from .main_display import display_screen


buttons = ["ADD NEW USER", "DELETE USER", "UPDATE USER DATA", "PREVIOUS SCR"]
header = "USER ACTIONS"
button_padding = 5
entry_message = "CHOSE YOUR ACTION: "

def show_user_actions():
    actions = display_screen(header, buttons, button_padding, entry_message)
    return actions