# ACCESSES: PSG, LAYOUTS, USER(?)

import PySimpleGUI as sg # library for GUI
from GUI import layouts
from modules.classes import User, Variables, Constants

# GUI

def GUI_main(server_ip, port):

    # CONSTANTS
    layout = layouts.main_layout
    window = sg.Window("sign up / log in", layout, resizable=True, finalize=True)
    pages = layouts.pages
    window_closed = sg.WIN_CLOSED

    # VARIABLES
    current_user = User()
    client_object = None

    main_constants = {
        "server_ip": server_ip, 
        "port": port, 
        "pages": pages,
        "window": window,
        "window_closed": window_closed
    }
    
    main_variables = {
        "current_user": current_user, 
        "client_object": client_object
    }

    main_variables = Variables(current_user, client_object)
    main_constants = Constants(server_ip, port, pages, window, window_closed)

    window["-SIGNUP-PAGE-"].update(visible=True)
    current_page = pages["-SIGNUP-PAGE-"]

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
