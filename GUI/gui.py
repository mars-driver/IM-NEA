import PySimpleGUI as sg # library for GUI
from GUI import layouts, page_classes

sg.set_options(suppress_raise_key_errors=False, suppress_error_popups=True, suppress_key_guessing=True) # for error handling

# CONSTANTS

PAGES = {
    "-CONNECTING-PAGE-": page_classes.Connecting("-CONNECTING-PAGE-", layouts.CONNECTING_LAYOUT, sg.WIN_CLOSED),
    "-SIGNUP-PAGE-": page_classes.SignUp("-SIGNUP-PAGE-", layouts.SIGNUP_LAYOUT, sg.WIN_CLOSED),
    "-LOGIN-PAGE-": page_classes.LogIn("-LOGIN-PAGE-", layouts.LOGIN_LAYOUT, sg.WIN_CLOSED),
    "-CUSTOMISE-PAGE-": page_classes.Customise("-CUSTOMISE-PAGE-", layouts.CUSTOMISE_PROFILE_LAYOUT, sg.WIN_CLOSED),
    "-HOME-PAGE-": page_classes.Home("-HOME-PAGE-", layouts.HOME_LAYOUT, sg.WIN_CLOSED),
    "-MESSAGING-PAGE-": page_classes.Messaging("-MESSAGING-PAGE-", layouts.MESSAGING_LAYOUT, sg.WIN_CLOSED)
}

PAGE_TABS = [[sg.Tab("", page.get_layout(), visible=False, k=page.get_name()) for page in PAGES.values()]]

LAYOUT = layouts.create_main_layout(PAGE_TABS)

WINDOW = sg.Window("", LAYOUT, resizable=True)

for page in PAGES.values():
    page.set_window(WINDOW)

# MAIN PROGRAM

def GUI_main(server_ip, port): # need server_ip and port
    """
    main program
    """
    PAGES["-CONNECTING-PAGE-"].set_server_ip(server_ip)
    PAGES["-CONNECTING-PAGE-"].set_port(port)
    current_page = PAGES["-CONNECTING-PAGE-"]
    current_user = User()

    while True:
        try:
            new_page_name, current_user = current_page.run_events(current_user)
            current_page = PAGES[new_page_name]
        except TypeError:
            print("You closed the window.")
            break
    WINDOW.close()

class User:
    def __init__(self):
        self.__username = None
        self.__client_object = None

    # GETTERS & SETTERS
    def get_username(self):
        return self.__username
    def get_client_object(self):
        return self.__client_object
    def set_username(self, new_username):
        self.__username = new_username
        self.__client_object.set_username(new_username)
    def set_client_object(self, new_client_object):
        self.__client_object = new_client_object
    def set_current_room_id(self, new_room_id):
        self.__client_object.set_current_room_id(new_room_id)