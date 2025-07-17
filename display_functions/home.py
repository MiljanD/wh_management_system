from .main_display import display_screen



header = "ACTIONS"
button_padding = 5
buttons = ["LOGIN", "EXIT"]
entry_message = "CHOSE YOUR ACTION: "



def display_home():
    home_entry = display_screen(header, buttons, button_padding, entry_message)
    return home_entry
