from .main_display import display_screen

header = "WH ACTIONS:"

button_padding = 5
buttons = ["ADD MATERIALS", "ISSUE OR RETURN", "CORRECTIONS", "PREVIOUS SCR"]
entry_message = "CHOSE YOUR ACTION: "
material_header = "ADD MATERIAL"
mat_buttons = ["ADD MATERIAL", "PREVIOUS SCR"]



def display_wh_actions():
    """
    handles the screen for warehouse action
    :return: user choice of action
    """
    wh_actions = display_screen(header, buttons, button_padding, entry_message)
    return wh_actions


def material_display():
    """
    handles the screen for action of adding materials on stock
    :return: user choice of action
    """
    material_action = display_screen(material_header, mat_buttons, button_padding, entry_message)
    return material_action