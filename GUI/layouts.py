import PySimpleGUI as sg # library for GUI
from GUI import page_classes

sg.theme("SystemDefault1")  # sets theme

# CONSTANTS
title_size = 30
subtitle_size = 20
input_output_size = 30
padding = ((64,0),0)
background_colour = "grey94"

# LAYOUTS


# SIGNUP

signup_layout = [
    [sg.Push(), sg.Text("Already have an account?")],
    [sg.Push(), sg.Button("log in here", size=18)],
    [sg.Text("")],
    [sg.Push(), sg.Text("Sign Up", font= ("Default font", title_size)), sg.Push()],
    [sg.Text("")],
    [sg.Push(), sg.Column([
        [sg.Text("enter username:")],
        [sg.Input(key="SIGNUP-USERNAME", size=input_output_size)],
        [sg.Text("enter email address:")],
        [sg.Input(key="SIGNUP-EMAIL", size=input_output_size)]
    ]), sg. Column([
        [sg.Text("enter password:")],
        [sg.Input(key="SIGNUP-PASSWORD", size=input_output_size, password_char="*")],
        [sg.Text("confirm password:")],
        [sg.Input(key="SIGNUP-CONFIRMPASSWORD", size=input_output_size, password_char="*")]
    ]), sg.Push()],
    [sg.Text(size=input_output_size, key="SIGNUP-OUTPUT")],
    [sg.Text("")],
    [sg.Push(), sg.Button("sign up", font= ("Default font", subtitle_size), bind_return_key=True), sg.Push()],
    [sg.Text("")]
]



# CUSTOMISE

customise_profile_layout = [
[sg.Push(), sg.Text("Already have an account?")],
    [sg.Push(), sg.Button("log in here", size=18)],
    [sg.Text("")],
    [sg.Push(), sg.Text("Customise Profile", font= ("Default font", title_size)), sg.Push()],
    [sg.Push(), sg.Frame("", [
        [sg.Text("Profile Preview:")],
        [sg.Frame("", [
            [sg.Image("media\\no_pfp.png", subsample=5), sg.Column([
                [sg.Text("example_username", size=input_output_size, key="CUSTOMISE-USERNAME")],
                [sg.Text("• Online", size=input_output_size)]
            ])],
            [sg.Text("Bio:")],
            [sg.Text(key="CUSTOMISE-SHOWBIO", size=(30,6), background_color="#ffffff")]
        ])]], size=(250,250), border_width=0), sg.Frame("", [
        [sg.Text("Upload profile picture")],
        [sg.FileBrowse(button_text="choose file", size=(27,1), key="CUSTOMISE-PFP")],
        [sg.Text("Write bio")],
        [sg.Multiline(default_text="Start typing...",key="CUSTOMISE-BIO", size=(30, 7), background_color="#ffffff")],
        [sg.Button("save")]
    ], size=(250,250), border_width=0), sg.Push()],
    [sg.Push(), sg.Button("Confirm", font= ("Default font", subtitle_size), bind_return_key=True), sg.Push()]
]



# LOGIN

login_layout = [
    [sg.Push(), sg.Text("Don't have an account?")],
[sg.Push(), sg.Button("sign up here", size=16)],
    [sg.Push(), sg.Text("Log In", font= ("Default font", title_size)), sg.Push()],
    [sg.Text("")],
    [sg.Text("enter username:", pad=padding)],
    [sg.Push(), sg.Input(key="LOGIN-USERNAME", default_text="admin"), sg.Push()],
    [sg.Text("")],
    [sg.Text("enter password:", pad=padding)],
    [sg.Push(), sg.Input(key="LOGIN-PASSWORD"), sg.Push()],
    [sg.Button("forgot password", pad=padding)],
    [sg.Text(size=input_output_size, key="LOGIN-OUTPUT")],
    [sg.Push(), sg.Button("log in", font= ("Default font", subtitle_size), bind_return_key=True), sg.Push()],
    [sg.Text("")]
]



# RECOVERY

account_recovery_layout = [
    [sg.Push(), sg.Text("Account Recovery", font= ("Default font", title_size)), sg.Push()],
]



# HOME todo

# test data!
friends = [
    ("Friend 1", "hello"),
    ("Friend 2", "hii!"),
    ("Friend 3", "wyu2"),
    ("Friend 4", "buns buns buns"),
    ("Friend 5", "hello"),
    ("Friend 8", "hii!"),
    ("Friend 323", "wyu2"),
    ("Friend 67", "buns buns buns"),
]

chatrooms = [
    ("name 1", )
]

friends_layout = [
    [sg.Frame("", [
                [sg.VPush()], [
                sg.Column([[sg.Image("media\\no_pfp.png", subsample=4, enable_events=True, k=f"-PFP{i}-")]]),
                sg.Column([[sg.Button(friends[i][0], font=("Default font", 15), border_width=0, k=f"-FRIEND{i}-")],
                           [sg.Button(friends[i][1], font=("Default font", 12),
                                      border_width=0, k=f"-LASTMESSAGE{i}-")]])],
                [sg.VPush()]], size=(350,100))
     ] for i in range(len(friends))
]


chatroom_layout = [
    [sg.Text("Open chat rooms", font= ("Default font", subtitle_size))],
    (
        [sg.Frame("", [
            [sg.VPush()],
            [sg.Button(f"Room Name {i}", font=("Default font", 12), border_width=0, k=f"-ROOM{i}-")],
            [sg.Button(f"Host: [host username]", font=("Default font", 10), border_width=0, k=f"-HOST{i}-")],
            [sg.Button(f"Members: 0", font=("Default font", 15), border_width=0, k=f"-MEMBERS{i}-")],
            [sg.VPush()]
        ])]
        for i in range(1,4)
    )
]

home_layout = [
    [sg.VPush()],
    [ # two centralised columns
        sg.Push(),
        # column 1 - Friends List
        sg.Frame("", [
            [sg.Text("Friends List:", font= ("Default font", 30))],
            [sg.Column(friends_layout, scrollable=True)]
        ]),
        # column 2 - Chat Rooms
        sg.Frame("", [
            [sg.Text("Open chat rooms", font= ("Default font", subtitle_size))],
            [sg.Column([#chatrooms_layout goes here
                        ])]
        ]),
        sg.Push()
    ],
    [sg.VPush()],
]


# MESSAGING

messagingroom_layout = [[sg.VPush()],
              [sg.Text("THIS IS THE CLIENT")],
              #[sg.Text("Server address:"), sg.Text(server_ip)],
              [sg.Text(size=(40, 1), key="-OUTPUT1-")],
              [sg.Text(size=(40, 1), key="-OUTPUT2-")],
              [sg.Text(size=(40, 1), key="-OUTPUT3-")],
              [sg.Text(size=(40, 1), key="-OUTPUT4-")],
              [sg.Text(size=(40, 1), key="-OUTPUT5-")],
              [
                  sg.Push(), sg.Text("Enter your name:", size=(15, 1), key="-PROMPT-"),
                  sg.Input(size=(15, 1), key="-MESSAGE-", do_not_clear=False),
                  sg.Button("send", bind_return_key=True), sg.Push()
              ],
              [sg.VPush()]]




##### MAIN LAYOUT #####

pages = {
    "-SIGNUP-": page_classes.SignUp("-SIGNUP-", signup_layout),
    "-CUSTOMISE-": page_classes.Customise("-CUSTOMISE-", customise_profile_layout),
    "-LOGIN-": page_classes.LogIn("-LOGIN-", login_layout),
    "-RECOVERY-": page_classes.Recovery("-RECOVERY-", account_recovery_layout),
    "-HOME-": page_classes.Home("-HOME-", home_layout),
    "-MESSAGING-": page_classes.Messaging("-MESSAGING-", messagingroom_layout)
}

page_tabs = [[sg.Tab("", page.get_layout(), visible=False, k=page.get_name()) for page in pages.values()]]

main_layout = [
    [sg.Text("")],
    [sg.Text("APP NAME", font=("Default font", 40))],
    [sg.Text("")],
    [sg.Push(),
    sg.TabGroup(
        page_tabs,
        selected_background_color = background_colour,
        background_color = background_colour,
        border_width=0,
        tab_border_width=0
    ), sg.Push()],
]