import PySimpleGUI as sg # library for GUI
from GUI import layouts, page_classes

# GUI

def GUI_signup_login(accounts, server_ip, port):
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
            sg.Tab("", layouts.home_layout, visible=False, k="-HOME-"),
            sg.Tab("", layouts.messagingroom_layout, visible=False, k="-MESSAGING-"),
        ]],
            selected_background_color = background_colour,
            background_color = background_colour,
            border_width=0,
            tab_border_width=0
        ), sg.Push()],
    ]

    window = sg.Window("sign up / log in", layout, resizable=True)
    pages = {
        "-SIGNUP-":page_classes.SignUp("-SIGNUP-", window, accounts),
        "-CUSTOMISE-":page_classes.Customise("-CUSTOMISE-", window, accounts),
        "-LOGIN-":page_classes.LogIn("-LOGIN-", window, accounts),
        "-HOME-":page_classes.Home("-HOME-", window, accounts),
        "-MESSAGING-":page_classes.Messaging("-MESSAGING-", window, accounts, server_ip, port)
    }

    current_page = pages["-SIGNUP-"]

    while True:
        if current_page is None:
            break
        else:
            current_page = current_page.run_events(pages, window_closed)
    window.close()

def window_closed(event):
    return event == sg.WIN_CLOSED