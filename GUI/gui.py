import PySimpleGUI as sg # library for GUI
import sign_up
import log_in
from GUI import layouts
from GUI import page_classes

# GUI

"""
sg.user_settings_filename(filename='my_settings.json')
print(sg.user_settings_filename())
settings = sg.UserSettings()
settings.load()
print(settings)
"""

def GUI_signup_login(accounts):
    layout = [
        [sg.Text("")],
        [sg.Text("APP NAME", font=("Default font", 40))],
        [sg.Text("")],
        [sg.Push(),
        sg.TabGroup([[
            sg.Tab("", layouts.signup_layout, visible=True, k="-SIGNUP-"),
            sg.Tab("", layouts.customise_profile_layout, visible=False, k="-CUSTOMISE-"),
            sg.Tab("", layouts.login_layout, visible=False, k="-LOGIN-")
        ]]), sg.Push()],
    ]

    window = sg.Window("sign up / log in", layout, resizable=True)
    pages = {
        "-SIGNUP-":page_classes.SignUp("-SIGNUP-"),
        "-CUSTOMISE-":page_classes.Customise("-CUSTOMISE-"),
        "-LOGIN-":page_classes.LogIn("-LOGIN-")
    }
    current_page = pages["-SIGNUP-"]

    while True:
        event, values = window.read()
        if event == sg.WINDOW_CLOSED:
            break
        current_page = current_page.run_events(window, event, values, pages, accounts)


# sg.theme("SystemDefault1")