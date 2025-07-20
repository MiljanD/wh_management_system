from .main_display import display_screen

header = "WH ACTIONS:"

button_padding = 5
buttons = ["ADD MATERIALS", "ISSUE OR RETURN", "CORRECTIONS", "PREVIOUS SCR"]
entry_message = "CHOSE YOUR ACTION: "
material_header = "ADD MATERIAL"
mat_buttons = ["ADD FROM INVOICE","ADD MANUALLY", "PREVIOUS SCR"]



def display_wh_actions():
    wh_actions = display_screen(header, buttons, button_padding, entry_message)
    return wh_actions


def material_display():
    material_action = display_screen(material_header, mat_buttons, button_padding, entry_message)
    return material_action