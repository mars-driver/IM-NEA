import PySimpleGUI as sg # library for GUI
from GUI import layouts
from modules.classes import User

# GUI

def GUI_main(server_ip, port):

    layout = layouts.main_layout
    window = sg.Window("sign up / log in", layout, resizable=True, finalize=True)
    current_user = User()

    pages = layouts.pages
    for page in pages.values():
        page.set_window(window)
    pages["-MESSAGING-"].set_server_ip(server_ip)
    pages["-MESSAGING-"].set_port(port)


    window["-SIGNUP-"].update(visible=True)
    current_page = pages["-SIGNUP-"]

    while True:
        return_values = current_page.run_events(current_user, pages, window_closed)
        if return_values is None:
            break
        else:
            current_user = return_values.get("-CURRENT-USER-")
            current_page = return_values.get("-NEW-PAGE-")
    window.close()

def window_closed(event):
    return event == sg.WIN_CLOSED