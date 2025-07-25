from .main_display import display_screen



header = "ACTIONS"
button_padding = 5
buttons = ["LOGIN", "EXIT"]
entry_message = "CHOSE YOUR ACTION: "



def display_home():
    """
    Home screen login or exiting from program
    :return: desired choice of user action
    """
    home_entry = display_screen(header, buttons, button_padding, entry_message)
    return home_entry
