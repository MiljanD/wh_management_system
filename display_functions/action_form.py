from .main_display import display_screen


buttons = ["WH ACTIONS", "REPORTS ACTIONS", "USER ACTIONS", "LOGOUT"]
header = "ACTIONS"
button_padding = 5
entry_message = "CHOSE YOUR ACTION: "


def display_actions():
    """
    Screen that is allowing user to choose desired action
    :return: desired choice of user action
    """
    action_entry = display_screen(header, buttons, button_padding, entry_message)
    return action_entry
