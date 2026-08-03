import PySimpleGUI as sg # library for GUI
from GUI import layouts, page_classes

# GUI

def GUI_signup_login(accounts):
    background_colour = layouts.set_theme()

    layout = [
        [sg.Text("")],
        [sg.Text("APP NAME", font=("Default font", 40))],
        [sg.Text("")],
        [sg.Push(),
        sg.TabGroup([[
            sg.Tab("", layouts.signup_layout, visible=True, k="-SIGNUP-"),
            sg.Tab("", layouts.customise_profile_layout, visible=False, k="-CUSTOMISE-"),
            sg.Tab("", layouts.login_layout, visible=False, k="-LOGIN-"),
            sg.Tab("", layouts.home_layout, visible=False, k="-HOME-")
        ]],
            selected_background_color = background_colour,
            background_color = background_colour,
            border_width=0,
            tab_border_width=0
        ), sg.Push()],
    ]

    window = sg.Window("sign up / log in", layout, resizable=True)
    pages = {
        "-SIGNUP-":page_classes.SignUp("-SIGNUP-"),
        "-CUSTOMISE-":page_classes.Customise("-CUSTOMISE-"),
        "-LOGIN-":page_classes.LogIn("-LOGIN-"),
        "-HOME-":page_classes.Home("-HOME-"),
        "-MESSAGING-":page_classes.Messaging("-MESSAGING-")
    }

    current_page = pages["-SIGNUP-"]

    while True:
        event, values = window.read()
        if event == sg.WINDOW_CLOSED:
            break
        current_page = current_page.run_events(window, event, values, pages, accounts)
    window.close()