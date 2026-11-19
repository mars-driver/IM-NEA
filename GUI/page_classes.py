from modules import sign_up, log_in, client # my modules
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

    def run_events(self, accounts, current_user):
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

class SignUp(Page):
    def run_events(self, accounts, current_user):
        """
        function to handle running the respective events for the Sign Up page
        """
        window = self.get_window()
        window_closed = self.get_window_closed()
        while True:
            event, values = window.read()
            if event == window_closed:
                break
            elif event == "-SIGN-UP-":
                relevant_values = (values["-SIGNUP-USERNAME-"], values["-SIGNUP-EMAIL-"], values["-SIGNUP-PASSWORD-"], values["-SIGNUP-CONFIRMPASSWORD-"])
                result = sign_up.sign_up(relevant_values, accounts)
                window["-SIGNUP-OUTPUT-"].update(result)
                if result == "Sign up successful.":
                    current_user.set_username(values["-SIGNUP-USERNAME-"])
                    return self.change_page("-CUSTOMISE-PAGE-"), current_user
            elif event == "-LOGIN-FROM-SIGNUP-":
                return self.change_page("-LOGIN-PAGE-"), current_user  # returns new page and current user

class LogIn(Page):
    def run_events(self, accounts, current_user):
        """
        function to handle running the respective events for the Log In page
        """
        window = self.get_window()
        window_closed = self.get_window_closed()
        while True:
            event, values = window.read()
            if event == window_closed:
                break
            elif event == "-LOGIN-":
                relevant_values = [values["-LOGIN-USERNAME-"], values["-LOGIN-PASSWORD-"]]
                result = log_in.log_in(relevant_values, accounts)
                window["-LOGIN-OUTPUT-"].update(result)
                if result == "Login successful.":
                    current_user.set_username(values["-LOGIN-USERNAME-"])
                    return self.change_page("-MESSAGING-PAGE-"), current_user
            elif event == "-SIGNUP-FROM-LOGIN-":
                return self.change_page("-SIGNUP-PAGE-"), current_user # returns new page name and current user

class Customise(Page):
    def run_events(self, accounts, current_user):
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
                return self.change_page("-MESSAGING-PAGE-"), current_user
            elif event == "-LOGIN-FROM-CUSTOMISE-":
                return self.change_page("-LOGIN-PAGE-"), current_user
            elif event == "-CUSTOMISE-PFP-":
                new_pfp_raw = values["-CUSTOMISE-PFP-"]
                new_pfp_image = Image.open(new_pfp_raw).resize(IMAGE_SIZE)
                new_pfp_image.save("media\\pfp.png", format="png")
                new_pfp_image.close()
                new_pfp = "media\\pfp.png"
                window["-SHOW-PFP-"].update(new_pfp)

class Messaging(Page):
    def run_events(self, accounts, current_user):
        """
        procedure to handle running the respective events for the Messaging page
        """
        window = self.get_window()
        window_closed = self.get_window_closed()
        client_object = current_user.get_client_object()
        messages = []

        Thread(target=client_object.receive, daemon=True).start()

        while True:
            event, values = window.read()
            if event == window_closed:
                break

            elif event == "-SEND-MESSAGE-":
                message = values["-MESSAGE-"]
                messages.append("You: " + message)
                client_object.send(message)
                update_messages(messages, window)

            elif event[0] == "-RECEIVED-":
                message_type = event[1]
                message_dict = values[event]

                if message_type == "-TEXT-": # A message sent from a user to a chat room
                    sender = message_dict["sender"]
                    content = message_dict["content"]
                    message = f"{sender}: {content}"
                    print("new message:", message)

                elif message_type == "-JOIN-": # A message sent by the server when a user joins the chat room
                    user = message_dict["user"]
                    message = f"{user} joined the chat."

                elif message_type == "-DISCONNECT-": # A message sent by the server when a user leaves the chat room
                    user = message_dict["user"]
                    message = f"{user} has left the chat."

                else:
                    message = "Error: unknown message"

                messages.append(message)
                update_messages(messages, window)

def update_messages(messages, window):
    """
    procedure to handle updating the display with the most recent messages
    """
    num_rows = 5
    visible_messages = messages[::-1]
    if len(messages) < num_rows:
        for _ in range(num_rows - len(messages)):
            visible_messages.append("")
    visible_messages = visible_messages[:num_rows][::-1]
    for i in range(num_rows):
        row = f"-OUTPUT{i+1}-"
        window[row].update(visible_messages[i])