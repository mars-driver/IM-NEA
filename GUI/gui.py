import PySimpleGUI as sg # library for GUI
from GUI import layouts

# GUI

def GUI_main(server_ip, port):

    layout = layouts.main_layout
    window = sg.Window("sign up / log in", layout, resizable=True, finalize=True)

    pages = layouts.pages
    for page in pages.values():
        page.set_window(window)
    pages["-MESSAGING-"].set_server_ip(server_ip)
    pages["-MESSAGING-"].set_port(port)


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