import PySimpleGUI as sg # library for GUI

sg.theme("SystemDefault1") # sets theme

# constants
title_size = 30
input_output_size = 30
padding = ((64,0),0)

signup_layout = [
    [sg.Push(), sg.Text("Already have an account?")],
    [sg.Push(), sg.Button("log in here", size=18)],
    [sg.Text("")],
    [sg.Push(), sg.Text("Sign Up", font= ("Default font", title_size)), sg.Push()],
    [sg.Text("")],
    [sg.Text("enter username:"), sg.Text("enter password:", pad=((121,0),0))],
    [sg.Input(key="SIGNUP-USERNAME", size=input_output_size), sg.Input(key="SIGNUP-PASSWORD", size=input_output_size, password_char="*")],
    [sg.Text("enter email address:"), sg.Text("confirm password:", pad=((98,0),0))],
    [sg.Input(key="SIGNUP-EMAIL", size=input_output_size), sg.Input(key="SIGNUP-CONFIRMPASSWORD", size=input_output_size, password_char="*")],
    [sg.Text(size=input_output_size, key="SIGNUP-OUTPUT")],
    [sg.Text("")],
    [sg.Push(), sg.Button("sign up", font= ("Default font", 20)), sg.Push()],
    [sg.Text("")]
]

customise_profile_layout = [
[sg.Push(), sg.Text("Already have an account?")],
    [sg.Push(), sg.Button("log in here", size=18)],
    [sg.Text("")],
    [sg.Push(), sg.Text("Customise Profile", font= ("Default font", title_size)), sg.Push()],
    [sg.Push(), sg.Frame("", [
        [sg.Text("Profile Preview:")],
        [sg.Text("image"), sg.Text(size=input_output_size, key="CUSTOMISE-USERNAME")],
        [sg.Text("Bio:")],
        [sg.Text(key="CUSTOMISE-SHOWBIO", size=(25,10), background_color="#ffffff")]
    ], size=(200,200)), sg.Frame("", [
        [sg.Text("Upload profile picture")],
        [sg.FileBrowse(button_text="choose file", key="CUSTOMISE-PFP")],
        [sg.Text("Write bio")],
        [sg.Input(default_text="Start typing...",key="CUSTOMISE-BIO", size=(25, 50), background_color="#ffffff")]
    ], size=(200,200)), sg.Push()],
    [sg.Push(), sg.Button("Confirm", font= ("Default font", title_size)), sg.Push()]
]

login_layout = [
    [sg.Push(), sg.Text("Don't have an account?")],
[sg.Push(), sg.Button("sign up here", size=16)],
    [sg.Push(), sg.Text("Log In", font= ("Default font", title_size)), sg.Push()],
    [sg.Text("")],
    [sg.Text("enter username:", pad=padding)],
    [sg.Push(), sg.Input(key="LOGIN-USERNAME"), sg.Push()],
    [sg.Text("")],
    [sg.Text("enter password:", pad=padding)],
    [sg.Push(), sg.Input(key="LOGIN-PASSWORD"), sg.Push()],
    [sg.Button("forgot password", pad=padding)],
    [sg.Text(size=input_output_size, key="LOGIN-OUTPUT")],
    [sg.Push(), sg.Button("log in", font= ("Default font", 20)), sg.Push()],
    [sg.Text("")]
]



account_recovery_layout = [
    [sg.Push(), sg.Text("Account Recovery", font= ("Default font", 30)), sg.Push()],
]