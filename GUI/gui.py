import PySimpleGUI as sg # library for GUI
import sign_up
import log_in
from GUI import layouts

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
    pages = ["-SIGNUP-", "-CUSTOMISE-", "-LOGIN-"]
    current_page = "SIGNUP"

    while True:
        event, values = window.read()
        if event == sg.WINDOW_CLOSED:
            break
        if event == "sign up":
            relevant_values = [values["SIGNUP-USERNAME"], values["SIGNUP-EMAIL"], values["SIGNUP-PASSWORD"], values["SIGNUP-CONFIRMPASSWORD"]]
            result = sign_up.proto_sign_up(relevant_values, accounts)
            window["SIGNUP-OUTPUT"].update(result)
            if result == "Sign up successful.":
                change_page(window, pages, "-CUSTOMISE-")
        if event == "log in":
            relevant_values = [values["LOGIN-USERNAME"], values["LOGIN-PASSWORD"]]
            result = log_in.proto_log_in(relevant_values, accounts)
            window["LOGIN-OUTPUT"].update(result)
        if event == "sign up here":
            change_page(window, pages, "-SIGNUP-")
        if event == "log in here":
            change_page(window, pages, "-LOGIN-")


def change_page(window, pages, new_page):
    window[new_page].update(visible=True)
    for page in pages:
        if page != new_page:
            window[page].update(visible=False)

# sg.theme("SystemDefault1")