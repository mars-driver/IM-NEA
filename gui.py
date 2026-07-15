import PySimpleGUI as sg # library for GUI
import sign_up
import log_in

# GUI
def proto_GUI_signup(accounts):
    layout = [[sg.Text("Sign Up")],
              [sg.Text("enter username:")],
              [sg.Input(key="USERNAME")],
              [sg.Text("enter email address:")],
              [sg.Input(key="EMAIL")],
              [sg.Text("enter password:")],
              [sg.Input(key="PASSWORD")],
              [sg.Text(size=(40, 1), key="OUTPUT")],
              [sg.Text("Already have an account?"), sg.Button("log in")],
              [sg.Button("ok"), sg.Button("quit")]]
    window = sg.Window("PROTO sign up", layout, resizable=True)
    while True:
        event, values = window.read()
        if event == sg.WINDOW_CLOSED or event == 'quit':
            break
        if event == "ok":
            result = sign_up.proto_sign_up(values.values(), accounts)
            window["OUTPUT"].update(result)
        if event == "log in":
            window.close()
            print(proto_GUI_login(accounts))


def proto_GUI_login(accounts):
    layout = [[sg.VPush()],
              [sg.Text("Log In")],
              [sg.Text("enter username:")],
              [sg.Input(key="USERNAME")],
              [sg.Text("enter password:")],
              [sg.Input(key="PASSWORD")],
              [sg.Button("forgot password")],
              [sg.Text(size=(40, 1), key="OUTPUT")],
              [sg.Text("Don't have an account?"), sg.Button("sign up")],
              [sg.Button("ok"), sg.Button("quit")],
              [sg.VPush()]]
    window = sg.Window("PROTO log in", layout, element_justification='center',resizable=True)
    while True:
        event, values = window.read()
        if event == sg.WINDOW_CLOSED or event == 'quit':
            break
        if event == "ok":
            result = log_in.proto_log_in(values.values(), accounts)
            window["OUTPUT"].update(result)
        if event == "sign up":
            window.close()
            print(proto_GUI_signup(accounts))