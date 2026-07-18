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
            sg.Tab("", layouts.customise_profile_layout, visible=True, k="-CUSTOMISE-"),
            sg.Tab("", layouts.login_layout, visible=True, k="-LOGIN-")
        ]]), sg.Push()],
    ]

    window = sg.Window("sign up / log in", layout, resizable=True)

    while True:
        event, values = window.read()
        if event == sg.WINDOW_CLOSED:
            break
        if event == "sign up":
            relevant_values = [values["SIGNUP-USERNAME"], values["SIGNUP-EMAIL"], values["SIGNUP-PASSWORD"], values["SIGNUP-CONFIRMPASSWORD"]]
            result = sign_up.proto_sign_up(relevant_values, accounts)
            window["SIGNUP-OUTPUT"].update(result)
            if result == "Sign up successful.":
                window["-CUSTOMISE-"].update(visible=True)
                window["-SIGNUP-"].update(visible=False)
        if event == "log in":
            relevant_values = [values["LOGIN-USERNAME"], values["LOGIN-PASSWORD"]]
            result = log_in.proto_log_in(relevant_values, accounts)
            window["LOGIN-OUTPUT"].update(result)
        if event == "sign up here":
            window["-SIGNUP-"].update(visible=True)
            window["-LOGIN-"].update(visible=False)
        if event == "log in here":
            window["-LOGIN-"].update(visible=True)
            window["-SIGNUP-"].update(visible=False)


# sg.theme("SystemDefault1")