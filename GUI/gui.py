# ACCESSES: PSG, LAYOUTS, USER(?)

import PySimpleGUI as sg # library for GUI
from GUI import layouts
from modules.classes import User, Constants, Variables

# GUI

def GUI_main(server_ip, port):

    layout = layouts.main_layout
    window = sg.Window("sign up / log in", layout, resizable=True, finalize=True)
    current_user = User()
    client_object = None
    pages = layouts.pages

    main_variables = Variables(current_user, client_object)
    main_constants = Constants(server_ip, port, pages, window, window_closed)

    window["-SIGNUP-PAGE-"].update(visible=True)
    current_page = pages["-SIGNUP-PAGE-"]

    while True:
        return_values = current_page.run_events(main_variables, main_constants)
        if return_values is None:
            break
        else:
            current_page = return_values.get("-NEW-PAGE-")
            current_user = return_values.get("-CURRENT-USER-")
            client_object = return_values.get("-CLIENT-")
            main_variables = Variables(current_user, client_object)
    window.close()

def window_closed(event):
    return event == sg.WIN_CLOSED