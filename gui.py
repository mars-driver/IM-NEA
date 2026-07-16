import PySimpleGUI as sg # library for GUI
import sign_up
import log_in

# GUI

sg.user_settings_filename(filename='my_settings.json')
print(sg.user_settings_filename())
settings = sg.UserSettings()
settings.load()
print(settings)

def GUI_signup(accounts):
    layout = [[sg.VPush(background_color="#969696")],
              [sg.Text("Sign Up", font= ("Default font", 30), background_color="#969696")],
              [sg.Text("enter username:", background_color="#969696")],
              [sg.Input(key="USERNAME", background_color="#ffffff")],
              [sg.Text("enter email address:", background_color="#969696")],
              [sg.Input(key="EMAIL", background_color="#ffffff")],
              [sg.Text("enter password:", background_color="#969696")],
              [sg.Input(key="PASSWORD", background_color="#ffffff")],
              [sg.Text(size=(40, 1), key="OUTPUT", background_color="#969696")],
              [sg.Text("Already have an account?", background_color="#969696"), sg.Button("log in")],
              [sg.Button("ok"), sg.Button("quit")],
              [sg.VPush(background_color="#969696")]]
    window = sg.Window("sign up", layout, element_justification='center', resizable=True, background_color="#969696")
    while True:
        event, values = window.read()
        if event == sg.WINDOW_CLOSED or event == 'quit':
            break
        if event == "ok":
            result = sign_up.proto_sign_up(values.values(), accounts)
            window["OUTPUT"].update(result)
        if event == "log in":
            window.close()
            print(GUI_login(accounts))


def GUI_login(accounts):
    layout = [[sg.VPush()],
              [sg.Text("Log In", font= ("Helvetica", 30))],
              [sg.Text("enter username:")],
              [sg.Input(key="USERNAME")],
              [sg.Text("enter password:")],
              [sg.Input(key="PASSWORD")],
              [sg.Push(), sg.pin(sg.Button("forgot password")), sg.Push()],
              [sg.Text(size=(40, 1), key="OUTPUT")],
              [sg.Text("Don't have an account?"), sg.Button("sign up")],
              [sg.Button("ok"), sg.Button("quit")],
              [sg.VPush()]]
    window = sg.Window("log in", layout, element_justification='center', resizable=True)
    while True:
        event, values = window.read()
        if event == sg.WINDOW_CLOSED or event == 'quit':
            break
        if event == "ok":
            result = log_in.proto_log_in(values.values(), accounts)
            window["OUTPUT"].update(result)
        if event == "sign up":
            window.close()
            print(GUI_signup(accounts))

def GUI_signup_login(accounts):
    signup_layout = [[sg.VPush(background_color="#969696")],
                    [sg.Text("Sign Up", font= ("Default font", 30), background_color="#969696")],
                    [sg.Text("enter username:", background_color="#969696")],
                    [sg.Input(key="SIGNUP-USERNAME", background_color="#ffffff")],
                    [sg.Text("enter email address:", background_color="#969696")],
                    [sg.Input(key="SIGNUP-EMAIL", background_color="#ffffff")],
                    [sg.Text("enter password:", background_color="#969696")],
                    [sg.Input(key="SIGNUP-PASSWORD", background_color="#ffffff")],
                    [sg.Text(size=(40, 1), key="SIGNUP-OUTPUT", background_color="#969696")],
                    [sg.Text("Already have an account?", background_color="#969696"), sg.Button("log in here")],
                    [sg.Button("sign up"), sg.Button("quit")],
                    [sg.VPush(background_color="#969696")]]

    login_layout = [[sg.VPush()],
                    [sg.Text("Log In", font= ("Helvetica", 30))],
                    [sg.Text("enter username:")],
                    [sg.Input(key="LOGIN-USERNAME")],
                    [sg.Text("enter password:")],
                    [sg.Input(key="LOGIN-PASSWORD")],
                    [sg.Push(), sg.pin(sg.Button("forgot password")), sg.Push()],
                    [sg.Text(size=(40, 1), key="LOGIN-OUTPUT")],
                    [sg.Text("Don't have an account?"), sg.Button("sign up here")],
                    [sg.Button("log in"), sg.Button("quit")],
                    [sg.VPush()]]

    layout = [[sg.TabGroup([[sg.Tab(title="", layout=signup_layout, k="-SIGNUP-"), sg.Tab("", login_layout, visible=False, k="-LOGIN-")]])]]
    window = sg.Window("sign up / log in", layout, resizable=True, element_justification="center")
    while True:
        event, values = window.read()
        if event == sg.WINDOW_CLOSED or event == 'quit':
            break
        if event == "sign up":
            result = sign_up.proto_sign_up(values.values(), accounts)
            window["SIGNUP-OUTPUT"].update(result)
        if event == "log in":
            result = log_in.proto_log_in(values.values(), accounts)
            window["LOGIN-OUTPUT"].update(result)
        if event == "sign up here":
            window["-SIGNUP-"].update(visible=True)
            window["-LOGIN-"].update(visible=False)
        if event == "log in here":
            window["-LOGIN-"].update(visible=True)
            window["-SIGNUP-"].update(visible=False)