
from .main_display import display_screen


buttons = ["ISSUE TO PRODUCTION", "RETURN ON STOCK", "PREVIOUS SCR"]
header = "ISSUE OR RETURN"
button_padding = 5
entry_message = "CHOSE YOUR ACTION: "

def issue_or_return():
    actions = display_screen(header, buttons, button_padding, entry_message)
    return actions