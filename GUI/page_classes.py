from modules import log_in, sign_up, client
from threading import Thread


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
    def run_events(self, pages, window_closed):
        print("Error: No events for superclass Page")


class SignUp(Page):
    def run_events(self, pages, window_closed):
        while True:
            event, values = self.get_window().read()
            if window_closed(event):
                break
            elif event == "sign up":
                relevant_values = [values["-SIGNUP-USERNAME-"], values["-SIGNUP-EMAIL-"], values["-SIGNUP-PASSWORD-"], values["-SIGNUP-CONFIRMPASSWORD-"]]
                result = sign_up.sign_up(relevant_values)
                self.get_window()["-SIGNUP-OUTPUT-"].update(result)
                if result == "Sign up successful.":
                    return change_page(self.get_window(), self, pages["-CUSTOMISE-"])
            elif event == "log in here":
                return change_page(self.get_window(), self, pages["-LOGIN-"])

class Customise(Page):
    def run_events(self, pages, window_closed):
        while True:
            event, values = self.get_window().read()
            if window_closed(event):
                break
            elif event == "save":
                self.get_window()["-CUSTOMISE-SHOWBIO-"].update(values["-CUSTOMISE-BIO-"])
            elif event == "Confirm":
                return change_page(self.get_window(), self, pages["-HOME-"])
            elif event == "log in here0":
                return change_page(self.get_window(), self, pages["-LOGIN-"])

class LogIn(Page):
    def run_events(self, pages, window_closed):
        while True:
            event, values = self.get_window().read()
            print(event)
            if window_closed(event):
                break
            elif event == "log in":
                relevant_values = [values["-LOGIN-USERNAME-"], values["-LOGIN-PASSWORD-"]]
                result = log_in.log_in(relevant_values)
                self.get_window()["-LOGIN-OUTPUT-"].update(result)
                if result == "Login successful.":
                    return change_page(self.get_window(), self, pages["-MESSAGING-"])
            elif event == "sign up here":
                return change_page(self.get_window(), self, pages["-SIGNUP-"])
            elif event == "forgot password":
                return change_page(self.get_window(), self, pages["-RECOVERY-"])

class Recovery(Page):
    def run_events(self, pages, window_closed):
        while True:
            event, values = self.get_window().read()
            if window_closed(event):
                break
            if event == "back to log in":
                return change_page(self.get_window(), self, pages["-LOGIN-"])

class Home(Page):
    def run_events(self, pages, window_closed):
        while True:
            event, values = self.get_window().read()
            if window_closed(event):
                break


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
    def run_events(self, pages, window_closed):
        client_object = client.ChatClient(self.get_server_ip(), self.get_port(), self.get_window())
        connected = False
        messages = []

        while not connected:
            event, values = self.get_window().read()
            print("event:", event, "values:", values)
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



def change_page(window, current_page, new_page):
    window[new_page.get_name()].update(visible=True)
    window[current_page.get_name()].update(visible=False)
    return new_page