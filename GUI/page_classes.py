# ACCESSES: MODULES

from modules import log_in, sign_up, client
from threading import Thread
from PIL import Image


class Page:
    def __init__(self, new_name, new_layout):
        self.__name = new_name
        self.__visibility = False
        self.__window = None
        self.__layout = new_layout

    def show_password(self, event):
        switch = (self.get_window()[event].metadata + 1) % 2  # keeps track of whether button is on or off
        element = event[5::]  # gets the name of the element (removes "-VIEW")
        char = ("*", "")[switch]  # switches between which one to show
        icon = ("media\\eye_open.png", "media\\eye_shut.png")[switch] # switches between icons
        self.get_window()[element].update(password_char=char)
        self.get_window()[event].update(image_filename=icon, image_subsample=4)
        self.get_window()[event].metadata = switch

    # GETTERS & SETTERS
    def get_name(self):
        return self.__name
    def get_window(self):
        return self.__window
    def get_layout(self):
        return self.__layout
    def set_window(self, new_window):
        self.__window = new_window
    def set_visibility(self):
        self.__window[self.__name].update(visible=True)


    # METHODS
    def run_events(self, constants):
        print("Error: No events for superclass Page")

class SignUp(Page):
    def run_events(self, constants):
        user, client_object, pages, window_closed = constants.user, constants.client_object, constants.pages, constants.window_closed
        return_values = {"-OLD-PAGE-": self, "-CURRENT-USER-": user, "-CLIENT-": client_object}
        while True:
            event, values = self.get_window().read()
            if window_closed(event):
                break
            elif event == "-SIGN-UP-":
                result = sign_up.sign_up((
                    values["-SIGNUP-USERNAME-"],
                    values["-SIGNUP-EMAIL-"],
                    values["-SIGNUP-PASSWORD-"],
                    values["-SIGNUP-CONFIRMPASSWORD-"]
                ))
                self.get_window()["-SIGNUP-OUTPUT-"].update(result)
                if result == "Sign up successful.":
                    username = values["-SIGNUP-USERNAME-"]
                    user.set_username(username)
                    return_values["-NEW-PAGE-"] = change_page(self.get_window(), self, pages["-CUSTOMISE-PAGE-"])
                    return return_values
            elif event == "-LOGIN-FROM-SIGNUP-":
                return_values["-NEW-PAGE-"] = change_page(self.get_window(), self, pages["-LOGIN-PAGE-"])
                return return_values
            elif event in ("-VIEW-SIGNUP-PASSWORD-", "-VIEW-SIGNUP-CONFIRMPASSWORD-"):
                self.show_password(event)


class Customise(Page):
    def run_events(self, constants):
        user, client_object, pages, window_closed = constants.user, constants.client_object, constants.pages, constants.window_closed
        pages = constants.pages
        return_values = {"-OLD-PAGE-": self, "-CURRENT-USER-": user, "-CLIENT-": client_object}
        username = user.get_username()
        self.get_window()["-CUSTOMISE-USERNAME-"].update(username)
        while True:
            event, values = self.get_window().read()
            if window_closed(event):
                break
            elif event == "-SAVE-":
                new_bio = values["-CUSTOMISE-BIO-"]
                self.get_window()["-CUSTOMISE-SHOWBIO-"].update(new_bio)
                user.set_bio(new_bio)
            elif event == "-CONFIRM-":
                self.get_window()["-LOGGED-IN?-"].update("LOGGED IN")
                return_values["-NEW-PAGE-"] = change_page(self.get_window(), self, pages["-CONNECT-PAGE-"])
                return return_values
            elif event == "-LOGIN-FROM-CUSTOMISE-":
                return_values["-NEW-PAGE-"] = change_page(self.get_window(), self, pages["-LOGIN-PAGE-"])
                return return_values
            elif event == "-CUSTOMISE-PFP-":
                new_pfp_raw = values["-CUSTOMISE-PFP-"]
                new_pfp_image = Image.open(new_pfp_raw).resize((50,50))
                new_pfp_image.save("media\\pfp.png", format="png")
                new_pfp_image.close()
                new_pfp = "media\\pfp.png"
                self.get_window()["-SHOW-PFP-"].update(new_pfp)
                user.set_pfp(new_pfp)


class LogIn(Page):
    def run_events(self, constants):
        user, client_object, pages, window_closed = constants.user, constants.client_object, constants.pages, constants.window_closed
        return_values = {"-OLD-PAGE-": self, "-CURRENT-USER-": user, "-CLIENT-": client_object}
        while True:
            event, values = self.get_window().read()
            if window_closed(event):
                break
            elif event == "-LOGIN-":
                result = log_in.log_in((values["-LOGIN-USERNAME-"], values["-LOGIN-PASSWORD-"]))
                self.get_window()["-LOGIN-OUTPUT-"].update(result)
                if result == "Login successful.":
                    username = values["-LOGIN-USERNAME-"]
                    user.set_username(username)
                    self.get_window()["-LOGGED-IN?-"].update("LOGGED IN")
                    return_values["-NEW-PAGE-"] = change_page(self.get_window(), self, pages["-CONNECT-PAGE-"])
                    return return_values
            elif event == "-SIGNUP-FROM-LOGIN-":
                return_values["-NEW-PAGE-"] = change_page(self.get_window(), self, pages["-SIGNUP-PAGE-"])
                return return_values
            elif event == "-RECOVERY-FROM-LOGIN-":
                return_values["-NEW-PAGE-"] = change_page(self.get_window(), self, pages["-RECOVERY-PAGE-"])
                return return_values
            elif event == "-VIEW-LOGIN-PASSWORD-":
                self.show_password(event)

class Recovery(Page):
    def run_events(self, constants):
        user, client_object, pages, window_closed = constants.user, constants.client_object, constants.pages, constants.window_closed
        return_values = {"-OLD-PAGE-": self, "-CURRENT-USER-": user, "-CLIENT-": client_object}
        while True:
            event, values = self.get_window().read()
            if window_closed(event):
                break
            if event == "-LOGIN-FROM-RECOVERY-":
                return_values["-NEW-PAGE-"] = change_page(self.get_window(), self, pages["-LOGIN-PAGE-"])
                return return_values
            if event == "-SEND-EMAIL-":
                pass

class Connect(Page):
    def run_events(self, constants):
        user, client_object, pages, window_closed = constants.user, constants.client_object, constants.pages, constants.window_closed
        return_values = {"-OLD-PAGE-": self, "-CURRENT-USER-": user, "-CLIENT-": client_object}
        while True:
            event, values = self.get_window().read()
            if window_closed(event):
                break
            elif event == "-CONNECT-":
                name = user.get_username()
                print("name:", name)
                client_object = client.initialise_client(constants.server_ip, constants.port, self.get_window())
                client_object.connect(name)
                self.get_window()["-CONNECTED?-"].update("CONNECTED")
                return_values["-CLIENT-"] = client_object
                return_values["-NEW-PAGE-"] = change_page(self.get_window(), self, pages["-MESSAGING-PAGE-"])
                return return_values

class Home(Page): #not in use
    def run_events(self, constants):
        user, client_object, pages, window_closed = constants.user, constants.client_object, constants.pages, constants.window_closed
        return_values = {"-OLD-PAGE-": self, "-CURRENT-USER-": user, "-CLIENT-": client_object}
        while True:
            event, values = self.get_window().read()
            if window_closed(event):
                break
            if event == "-NEW-ROOM-":
                return_values["-NEW-PAGE-"] = change_page(self.get_window(), self, pages["-MESSAGING-PAGE-"])
                return return_values


class Messaging(Page):
    def __init__(self, new_name, new_layout):
        super().__init__(new_name, new_layout)
        self.__client_object = None

    # GETTERS & SETTERS
    def get_client(self):
        return self.__client_object
    def set_client(self, new_client):
        self.__client_object = new_client

    # METHODS
    def run_events(self, constants):
        user, client_object, pages, window_closed = constants.user, constants.client_object, constants.pages, constants.window_closed
        return_values = {"-OLD-PAGE-": self, "-CURRENT-USER-": user, "-CLIENT-": client_object}

        messages = []
        Thread(target=client_object.receive).start()
        self.get_window()["-PROMPT-"].update("Type message here:")

        while True:
            event, values = self.get_window().read()
            if window_closed(event):
                client_object.socket.close()
                break
            elif event == "-SEND-MESSAGE-":
                message = values["-MESSAGE-"]
                messages.append(("You:", message))
                client_object.send(message)
                self.update_messages(messages)
            elif event == "-RECEIVED-":
                message = values["-RECEIVED-"]
                messages.append(("", message))
                self.update_messages(messages)
            elif event == "-LEAVE-ROOM-":
                client_object.socket.close()
                self.get_window()["-CONNECTED?-"].update("NOT CONNECTED")
                return_values["-NEW-PAGE-"] = change_page(self.get_window(), self, pages["-CONNECT-PAGE-"])
                return return_values

    def update_messages(self, messages):
        num_rows = 5
        visible_messages = messages[::-1]
        if len(messages) < num_rows:
            for _ in range(num_rows - len(messages)):
                visible_messages.append("")
        visible_messages = visible_messages[:num_rows][::-1]
        for i in range(num_rows):
            row = f"-OUTPUT{i + 1}-"
            self.get_window()[row].update(" ".join(visible_messages[i]))



def change_page(window, current_page_object, new_page_object): #todo: move this under Page?
    window[new_page_object.get_name()].update(visible=True)
    window[current_page_object.get_name()].update(visible=False)
    return new_page_object