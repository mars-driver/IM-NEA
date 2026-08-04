import PySimpleGUI as sg # library for GUI
from GUI import layouts, page_classes

# GUI

def GUI_signup_login(accounts, server_ip, port):

    layout = layouts.main_layout

    window = sg.Window("sign up / log in", layout, resizable=True, finalize=True)

    pages = {
        "-SIGNUP-": page_classes.SignUp("-SIGNUP-", window, accounts, layouts.signup_layout),
        "-CUSTOMISE-": page_classes.Customise("-CUSTOMISE-", window, accounts, layouts.customise_profile_layout),
        "-LOGIN-": page_classes.LogIn("-LOGIN-", window, accounts, layouts.login_layout),
        "-HOME-": page_classes.Home("-HOME-", window, accounts, layouts.home_layout),
        "-MESSAGING-": page_classes.Messaging("-MESSAGING-", window, accounts, layouts.messagingroom_layout, server_ip, port)
    }

    window["-SIGNUP-"].update(visible=True)
    current_page = pages["-SIGNUP-"]

    while True:
        if current_page is None:
            break
        else:
            current_page = current_page.run_events(pages, window_closed)
    window.close()

def window_closed(event):
    return event == sg.WIN_CLOSED