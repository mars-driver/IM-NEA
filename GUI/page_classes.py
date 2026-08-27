from modules import log_in, sign_up, client
from threading import Thread
from PIL import Image


class Page:
    def __init__(self, new_name, new_layout):
        self.__name = new_name
        self.__visibility = False
        self.__window = None
        self.__layout = new_layout

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
    def run_events(self, user, pages, window_closed):
        print("Error: No events for superclass Page")


class SignUp(Page):
    def run_events(self, user, pages, window_closed):
        return_values = {"-OLD-PAGE-": self, "-CURRENT-USER-": user}
        while True:
            event, values = self.get_window().read()
            if window_closed(event):
                break
            elif event == "sign up":
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
                    return_values["-NEW-PAGE-"] = change_page(self.get_window(), self, pages["-CUSTOMISE-"])
                    return return_values
            elif event == "log in here":
                return_values["-NEW-PAGE-"] = change_page(self.get_window(), self, pages["-LOGIN-"])
                return return_values

class Customise(Page):
    def run_events(self, user, pages, window_closed):
        return_values = {"-OLD-PAGE-": self, "-CURRENT-USER-": user}
        username = user.get_username()
        self.get_window()["-CUSTOMISE-USERNAME-"].update(username)
        while True:
            event, values = self.get_window().read()
            if window_closed(event):
                break
            elif event == "save":
                new_bio = values["-CUSTOMISE-BIO-"]
                self.get_window()["-CUSTOMISE-SHOWBIO-"].update(new_bio)
                user.set_bio(new_bio)
            elif event == "Confirm":
                return_values["-NEW-PAGE-"] = change_page(self.get_window(), self, pages["-HOME-"])
                return return_values
            elif event == "log in here0":
                return_values["-NEW-PAGE-"] = change_page(self.get_window(), self, pages["-LOGIN-"])
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
    def run_events(self, user, pages, window_closed):
        return_values = {"-OLD-PAGE-": self, "-CURRENT-USER-": user}
        while True:
            event, values = self.get_window().read()
            if window_closed(event):
                break
            elif event == "log in":
                result = log_in.log_in((values["-LOGIN-USERNAME-"], values["-LOGIN-PASSWORD-"]))
                self.get_window()["-LOGIN-OUTPUT-"].update(result)
                if result == "Login successful.":
                    return_values["-NEW-PAGE-"] = change_page(self.get_window(), self, pages["-HOME-"])
                    return return_values
            elif event == "sign up here":
                return_values["-NEW-PAGE-"] = change_page(self.get_window(), self, pages["-SIGNUP-"])
                return return_values
            elif event == "forgot password":
                return_values["-NEW-PAGE-"] = change_page(self.get_window(), self, pages["-RECOVERY-"])
                return return_values

class Recovery(Page):
    def run_events(self, user, pages, window_closed):
        return_values = {"-OLD-PAGE-": self, "-CURRENT-USER-": user}
        while True:
            event, values = self.get_window().read()
            if window_closed(event):
                break
            if event == "back to log in":
                return_values["-NEW-PAGE-"] = change_page(self.get_window(), self, pages["-LOGIN-"])
                return return_values

class Home(Page):
    def run_events(self, user, pages, window_closed):
        return_values = {"-OLD-PAGE-": self, "-CURRENT-USER-": user}
        while True:
            event, values = self.get_window().read()
            print(event, values) #todo remove
            if window_closed(event):
                break
            if event == "-NEW-ROOM-":
                pass


class Messaging(Page):
    def __init__(self, new_name, new_layout):
        super().__init__(new_name, new_layout)
        self.__server_ip = None
        self.__port = None

    # GETTERS & SETTERS
    def get_server_ip(self):
        return self.__server_ip
    def get_port(self):
        return self.__port
    def set_server_ip(self, new_server_ip):
        self.__server_ip = new_server_ip
    def set_port(self, new_port):
        self.__port = new_port

    # METHODS
    def run_events(self, user, pages, window_closed):
        return_values = {"-OLD-PAGE-": self, "-CURRENT-USER-": user}

        client_object = client.ChatClient(self.get_server_ip(), self.get_port(), self.get_window())
        connected = False
        messages = []

        while not connected:
            event, values = self.get_window().read()
            print("event:", event, "values:", values) #todo remove
            if window_closed(event):
                break
            elif event == "send":
                name = values["-MESSAGE-"]
                client_object.connect(name)
                connected = True

        Thread(target=client_object.receive).start()
        self.get_window()["-PROMPT-"].update("Type message here:")

        while True:
            event, values = self.get_window().read()
            if window_closed(event):
                client_object.socket.close()
                break
            elif event == "send":
                message = values["-MESSAGE-"]
                messages.append(("You:", message))
                client_object.send(message)
                self.update_messages(messages)
            elif event == "-RECEIVED-":
                message = values["-RECEIVED-"]
                messages.append(("", message))
                self.update_messages(messages)

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



def change_page(window, current_page_object, new_page_object):
    window[new_page_object.get_name()].update(visible=True)
    window[current_page_object.get_name()].update(visible=False)
    return new_page_object