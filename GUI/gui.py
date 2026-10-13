# ACCESSES: PSG, LAYOUTS, USER(?)

import PySimpleGUI as sg # library for GUI
from GUI import layouts
from modules.classes import User

# GUI

def GUI_main(server_ip, port):

    # CONSTANTS
    LAYOUT = layouts.main_layout
    WINDOW = sg.Window("sign up / log in", LAYOUT, resizable=True, finalize=True)
    PAGES = layouts.pages

    # VARIABLES
    current_user = User()
    client_object = None

    main_constants = {
        "server_ip": server_ip, 
        "port": port, 
        "pages": PAGES, 
        "window": WINDOW, 
        "window_closed": window_closed
    }
    
    main_variables = {
        "current_user": current_user, 
        "client_object": client_object
    }

    WINDOW["-SIGNUP-PAGE-"].update(visible=True)
    current_page = PAGES["-SIGNUP-PAGE-"]

    while True:
        return_values = current_page.run_events(main_constants, main_variables)
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
