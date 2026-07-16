import PySimpleGUI as sg # library for GUI

sg.theme("SystemDefault1") # sets theme

signup_layout = [[sg.Push(), sg.Text("Sign Up", font= ("Default font", 30)), sg.Push()],
                 [sg.Text("enter username:")],
                 [sg.Input(key="SIGNUP-USERNAME")],
                 [sg.Text("enter email address:")],
                 [sg.Input(key="SIGNUP-EMAIL")],
                 [sg.Text("enter password:")],
                 [sg.Input(key="SIGNUP-PASSWORD")],
                 [sg.Text(size=(40, 1), key="SIGNUP-OUTPUT")],
                 [sg.Text("Already have an account?"), sg.Button("log in here")],
                 [sg.Text("")],
                 [sg.Push(), sg.Button("sign up", font= ("Default font", 15)), sg.Push()],
                 [sg.Text("")]]

login_layout = [[sg.Push(), sg.Text("Log In", font= ("Default font", 30)), sg.Push()],
                [sg.Text("")],
                [sg.Text("enter username:")],
                [sg.Input(key="LOGIN-USERNAME")],
                [sg.Text("enter password:")],
                [sg.Input(key="LOGIN-PASSWORD")],
                [sg.pin(sg.Button("forgot password")), sg.Push()],
                [sg.Text(size=(40, 1), key="LOGIN-OUTPUT")],
                [sg.Text("Don't have an account?"), sg.Button("sign up here")],
                [sg.Text("")],
                [sg.Push(), sg.Button("log in", font= ("Default font", 15)), sg.Push()]]