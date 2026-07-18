import sign_up
import log_in

class Page:
    def __init__(self, new_name):
        self.name = new_name
        self.visibility = False

    def set_visibility(self, window):
        window[self.name].update(visible=True)

    def run_events(self, window, event, values, pages, accounts):
        pass


class SignUp(Page):
    def run_events(self, window, event, values, pages, accounts):
        if event == "sign up":
            relevant_values = [values["SIGNUP-USERNAME"], values["SIGNUP-EMAIL"], values["SIGNUP-PASSWORD"], values["SIGNUP-CONFIRMPASSWORD"]]
            result = sign_up.proto_sign_up(relevant_values, accounts)
            window["SIGNUP-OUTPUT"].update(result)
            if result == "Sign up successful.":
                change_page(window, self, pages["-CUSTOMISE-"])
                return pages["-CUSTOMISE-"]
        if event == "log in here":
            change_page(window, self, pages["-LOGIN-"])
            return pages["-LOGIN-"]
        return self

class LogIn(Page):
    def run_events(self, window, event, values, pages, accounts):
        if event == "log in":
            relevant_values = [values["LOGIN-USERNAME"], values["LOGIN-PASSWORD"]]
            result = log_in.proto_log_in(relevant_values, accounts)
            window["LOGIN-OUTPUT"].update(result)
        if event == "sign up here":
            change_page(window, self, pages["-SIGNUP-"])
            return pages["-SIGNUP-"]
        return self

class Customise(Page):
    def run_events(self, window, event, values, pages, accounts):
        if event == "Confirm":
            change_page(window, self, pages["-SIGNUP-"])
            return pages["-SIGNUP-"]
        if event == "log in here0":
            change_page(window, self, pages["-LOGIN-"])
            return pages["-LOGIN-"]
        return pages["-CUSTOMISE-"]

def change_page(window, current_page, new_page):
    window[new_page.name].update(visible=True)
    window[current_page.name].update(visible=False)