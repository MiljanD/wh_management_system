from .main_display import display_screen


buttons = ["GENERATE REPORT", "PREVIOUS SCR"]
header = "REPORTS"
button_padding = 5
entry_message = "DO YOU WANT TO GENERATE REPORT: "

def generate_report_display():
    """
    handles the screen for generating daily reports
    :return: user choice of action
    """
    report_display = display_screen(header, buttons, button_padding, entry_message)
    return report_display


