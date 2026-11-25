from modules import client # my modules
from GUI import layouts
from PIL import Image
from threading import Thread

# CONSTANTS
IMAGE_SIZE = (50,50)

class Page:
    def __init__(self, new_name, new_layout, new_windowclosed):
        self.__name = new_name
        self.__layout = new_layout
        self.__window = None
        self.__window_closed = new_windowclosed

    # GETTERS & SETTERS

    def get_name(self):
        return self.__name
    def get_layout(self):
        return self.__layout
    def get_window(self):
        return self.__window
    def get_window_closed(self):
        return self.__window_closed
    def set_window(self, new_window):
        self.__window = new_window

    # METHODS

    def run_events(self, current_user):
        """
        generic run_events method - this will not do anything and only exists as a template
        """
        pass

    def change_page(self, new_page_name):
        """
        method to change the current visible page
        """
        window = self.get_window()
        window[new_page_name].update(visible=True)
        window[self.get_name()].update(visible=False)
        return new_page_name # returns the name of the new page

class Connecting(Page):
    def __init__(self, new_name, new_layout, new_windowclosed):
        super().__init__(new_name, new_layout, new_windowclosed)
        self.__server_ip = None
        self.__port = None

    def get_server_ip(self):
        return self.__server_ip
    def get_port(self):
        return self.__port
    def set_server_ip(self, new_server_ip):
        self.__server_ip = new_server_ip
    def set_port(self, new_port):
        self.__port = new_port

    def run_events(self, current_user):
        window = self.get_window()
        window_closed = self.get_window_closed()

        while True:
            event, values = window.read(timeout=100)
            if event == window_closed:
                break
            else:
                try:
                    client_object = client.ChatClient(self.get_server_ip(), self.get_port(), window)
                    client_object.connect()
                    current_user.set_client_object(client_object)
                    return self.change_page("-SIGNUP-PAGE-"), current_user
                except ConnectionRefusedError:
                    pass

class SignUp(Page):
    def run_events(self, current_user):
        """
        function to handle running the respective events for the Sign Up page
        """
        window = self.get_window()
        window_closed = self.get_window_closed()
        client_object = current_user.get_client_object()
        while True:
            event, values = window.read()
            if event == window_closed:
                break
            elif event == "-SIGN-UP-":
                relevant_values = (values["-SIGNUP-USERNAME-"], values["-SIGNUP-EMAIL-"], values["-SIGNUP-PASSWORD-"], values["-SIGNUP-CONFIRMPASSWORD-"])
                result = client_object.sign_up(relevant_values)
                window["-SIGNUP-OUTPUT-"].update(result)
                if result == "-SUCCESS-":
                    current_user.set_username(values["-SIGNUP-USERNAME-"])
                    return self.change_page("-CUSTOMISE-PAGE-"), current_user
            elif event == "-LOGIN-FROM-SIGNUP-":
                return self.change_page("-LOGIN-PAGE-"), current_user  # returns new page and current user
            elif event in ("-VIEW-SIGNUP-PASSWORD-", "-VIEW-SIGNUP-CONFIRMPASSWORD-"):
                show_password(event, window)

class LogIn(Page):
    def run_events(self, current_user):
        """
        function to handle running the respective events for the Log In page
        """
        window = self.get_window()
        window_closed = self.get_window_closed()
        client_object = current_user.get_client_object()
        while True:
            event, values = window.read()
            if event == window_closed:
                break
            elif event == "-LOGIN-":
                username = values["-LOGIN-USERNAME-"]
                password = values["-LOGIN-PASSWORD-"]
                result = client_object.log_in(username, password)
                window["-LOGIN-OUTPUT-"].update(result)
                if result == "-SUCCESS-":
                    current_user.set_username(values["-LOGIN-USERNAME-"])
                    return self.change_page("-HOME-PAGE-"), current_user
            elif event == "-SIGNUP-FROM-LOGIN-":
                return self.change_page("-SIGNUP-PAGE-"), current_user # returns new page name and current user
            elif event == "-VIEW-LOGIN-PASSWORD-":
                show_password(event, window)

class Customise(Page):
    def run_events(self, current_user):
        """
        function to handle running the respective events for the Customise Profile page
        """
        window = self.get_window()
        window_closed = self.get_window_closed()
        username = current_user.get_username()
        window["-CUSTOMISE-USERNAME-"].update(username) # updates the username
        while True:
            event, values = window.read()
            if event == window_closed:
                break
            elif event == "-SAVE-":
                new_bio = values["-CUSTOMISE-BIO-"]
                window["-CUSTOMISE-SHOWBIO-"].update(new_bio)
            elif event == "-CONFIRM-":
                return self.change_page("-HOME-PAGE-"), current_user
            elif event == "-LOGIN-FROM-CUSTOMISE-":
                return self.change_page("-LOGIN-PAGE-"), current_user
            elif event == "-CUSTOMISE-PFP-":
                new_pfp_raw = values["-CUSTOMISE-PFP-"]
                new_pfp_image = Image.open(new_pfp_raw).resize(IMAGE_SIZE)
                new_pfp_image.save("media\\pfp.png", format="png")
                new_pfp_image.close()
                new_pfp = "media\\pfp.png"
                window["-SHOW-PFP-"].update(new_pfp)

class Home(Page):
    def run_events(self, current_user):
        window = self.get_window()
        window_closed = self.get_window_closed()
        client_object = current_user.get_client_object()

        current_chatroom_list = client_object.get_chatrooms()
        layouts.update_chatroom_column(window, current_chatroom_list)

        while True:
            event, values = window.read()
            if event == window_closed:
                break
            elif event.split("-")[1] == "ROOM":
                room_index = int(event.split("-")[2])
                selected_room = current_chatroom_list[room_index]
                current_user.set_current_room_id(selected_room["id"])
                return self.change_page("-MESSAGING-PAGE-"), current_user


class Messaging(Page):
    def run_events(self, current_user):
        """
        procedure to handle running the respective events for the Messaging page
        """
        window = self.get_window()
        window_closed = self.get_window_closed()
        client_object = current_user.get_client_object()
        layouts.clear_screen(window) # clears the screen of any old messages

        # displays the room info on the window
        room_details = client_object.get_room_details()
        room_name = room_details["name"]
        window["-ROOM-NAME-"].update(room_name)

        layouts.update_screen({"message_type": "-WELCOME-", "room_name": room_name, "members": room_details["members"]}, window)

        Thread(target=client_object.receive, daemon=True).start()

        while True:
            event, values = window.read()
            if event == window_closed:
                break

            elif event == "-LEAVE-ROOM-":
                client_object.leave_room()
                return self.change_page("-HOME-PAGE-"), current_user

            elif event == "-SEND-MESSAGE-":
                message = values["-MESSAGE-"]
                if message != "":
                    message_dict = {
                        "message_type": "-SENT-",
                        "content": message,
                    }
                    client_object.send_text(message_dict)
                    layouts.update_screen(message_dict, window)
                else:
                    print("cannot send an empty string")

            elif event[0] == "-RECEIVED-":
                message_dict = values[event]
                layouts.update_screen(message_dict, window)


def show_password(event, window):
    """
    procedure to make change password visibility (makes visible if hidden, or hides if visible)
    """
    switch = (window[event].metadata + 1) % 2  # keeps track of whether button is on or off
    element = event[5::]  # gets the name of the element (removes "-VIEW")
    char = ("*", "")[switch]  # switches between which one to show
    icon = ("media\\eye_open.png", "media\\eye_shut.png")[switch] # switches between icons
    window[element].update(password_char=char)
    window[event].update(image_filename=icon, image_subsample=4)
    window[event].metadata = switch