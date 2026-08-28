# ACCESSES: PSG, PAGE CLASSES

import PySimpleGUI as sg # library for GUI
from GUI import page_classes

sg.theme("SystemDefault1")  # sets theme

# CONSTANTS
app_name_size = 40
title_size = 30
subtitle_size = 20
input_output_size = 30
main_button_size = 18
dual_frame_size = (250,250)
dual_frame_button_size = (27,1)
textbox_size = (30,7)
background_colour = "grey94"

# LAYOUTS

# Connection

connection_layout = [
    [sg.VPush()],
    [sg.Push(), sg.Text("NOT CONNECTED", font=("Default font", title_size)), sg.Push()],
    [sg.Push(), sg.Button("Connect", k="-CONNECT-"), sg.Push()],
    [sg.VPush()]
]

# Signup

signup_layout = [
    [sg.Push(), sg.Frame("", [
        [sg.Text("Already have an account?")],
        [sg.Button("log in here", s=main_button_size, k="-LOGIN-FROM-SIGNUP-")],
    ], border_width=False)],
    [sg.Text("")],
    [sg.Push(), sg.Text("Sign Up", font=("Default font", title_size)), sg.Push()],
    [sg.Push(), sg.Frame("", [
        [sg.VPush()],
        [sg.Text("enter username:")],
        [sg.Input(k="-SIGNUP-USERNAME-", default_text="admin")],
        [sg.Text("enter email address:")],
        [sg.Input(k="-SIGNUP-EMAIL-")],
        [sg.VPush()],
        [sg.Text(k="-SIGNUP-OUTPUT-")],
    ], s=dual_frame_size, border_width=False), sg. Frame("", [
        [sg.VPush()],
        [sg.Text("enter password:")],
        [sg.Input(k="-SIGNUP-PASSWORD-", password_char="*")],
        [sg.Text("confirm password:")],
        [sg.Input(k="-SIGNUP-CONFIRMPASSWORD-", password_char="*")],
        [sg.VPush()],
        [sg.Text("")]
    ], s=dual_frame_size, border_width=False), sg.Push()],
    [sg.Push(), sg.Button("sign up", font=("Default font", subtitle_size), k="-SIGN-UP-"), sg.Push()],
    [sg.Text("")]
]



# Customise

customise_profile_layout = [
    [sg.Push(), sg.Frame("", [
        [sg.Text("Already have an account?")],
        [sg.Button("log in here", s=main_button_size, k="-LOGIN-FROM-CUSTOMISE-")],
    ], border_width=False)],
    [sg.Text("")],
    [sg.Push(), sg.Text("Customise Profile", font=("Default font", title_size)), sg.Push()],
    [sg.Text("")],
    [sg.Push(), sg.Frame("", [
        [sg.Text("Profile Preview:")],
        [sg.Frame("", [
            [sg.Image("media\\no_pfp.png", k="-SHOW-PFP-"), sg.Frame("", [
                [sg.Text("example_username", s=input_output_size, k="-CUSTOMISE-USERNAME-")],
                [sg.Text("• Online", s=input_output_size)]
            ], border_width=False)],
            [sg.Text("Bio:")],
            [sg.Text(k="-CUSTOMISE-SHOWBIO-", s=textbox_size, background_color="#ffffff")]
        ], border_width=False)]], s=dual_frame_size, border_width=False), sg.Frame("", [
        [sg.Text("Upload profile picture")],
        [sg.FileBrowse(button_text="choose file", file_types=(('PNG Image', '.png'),('JPEG Image', '.jpg')),
                       s=dual_frame_button_size, enable_events=True, k="-CUSTOMISE-PFP-")],
        [sg.Text("Write bio")],
        [sg.Multiline(default_text="Start typing...",k="-CUSTOMISE-BIO-", s=textbox_size, background_color="#ffffff")],
        [sg.Button("save", k="-SAVE-")]
    ], s=dual_frame_size, border_width=False), sg.Push()],
    [sg.Push(), sg.Button("Confirm", font=("Default font", subtitle_size), k="-CONFIRM-"), sg.Push()]
]



# Login

login_layout = [
    [sg.Push(), sg.Frame("", [
        [sg.Push(), sg.Text("Don't have an account?"), sg.Push()],
        [sg.Button("sign up here", s=main_button_size, k ="-SIGNUP-FROM-LOGIN-")]
    ], border_width=False)],
    [sg.Push(), sg.Text("Log In", font=("Default font", title_size)), sg.Push()],
    [sg.Text("")],
    [sg.Push(),
     sg.Frame("", [
        [sg.Text("enter username:")],
        [sg.Push(), sg.Input(k="-LOGIN-USERNAME-", default_text="admin"), sg.Push()],
        [sg.Text("")],
        [sg.Text("enter password:")],
        [sg.Push(), sg.Input(k="-LOGIN-PASSWORD-"), sg.Push()],
        [sg.Button("forgot password", k="-RECOVERY-FROM-LOGIN-")],
        [sg.Text(k="-LOGIN-OUTPUT-")],
    ], border_width=False),
     sg.Push()],
    [sg.Push(), sg.Button("log in", font=("Default font", subtitle_size), k="-LOGIN-"), sg.Push()],
    [sg.Text("")]
]



# Recovery

account_recovery_layout = [
    [sg.Text("")],
    [sg.Push(), sg.Button("back to log in", s=main_button_size, k="-LOGIN-FROM-RECOVERY-")],
    [sg.Text("")],
    [sg.Push(), sg.Frame("", [
        [sg.Push(), sg.Text("Account Recovery", font=("Default font", title_size)), sg.Push()],
        [sg.Text("")],
        [sg.Push(),
         sg.Frame("", [
             [sg.Text("enter email associated with your account:")],
             [sg.Push(), sg.Input(k="-EMAIL-"), sg.Push()],
             [sg.Text(k="-RECORVERY-OUTPUT-")],
         ], border_width=False),
         sg.Push()],
        [sg.Text("")],
        [sg.Push(), sg.Button("Send email", font=("Default font", subtitle_size), k="-SEND-EMAIL-"), sg.Push()],
    ], border_width=False), sg.Push()],
    [sg.VPush()], [sg.VPush()]
]



# Home
# todo wip

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
friends = []

chatrooms = [
    ("name 1", )
]

friends_layout = [
    [sg.Frame("", [ #todo remove border
                [sg.VPush()], [
                sg.Column([[sg.Image("media\\no_pfp.png", enable_events=True, k=f"-PFP{i}-")]]),
                sg.Column([[sg.Button(friends[i][0], font=("Default font", 15), border_width=0, k=f"-FRIEND{i}-")],
                           [sg.Button(friends[i][1], font=("Default font", 12),
                                      border_width=1, k=f"-LASTMESSAGE{i}-")]])],
                [sg.VPush()]], s=(350,100))
     ] for i in range(len(friends))
]


chatroom_layout = [
    [sg.Text("Open chat rooms", font= ("Default font", subtitle_size))],
    (
        [sg.Frame("", [ #todo remove border
            [sg.VPush()],
            [sg.Button(f"Room Name {i}", font=("Default font", 12), border_width=0, k=f"-ROOM{i}-")],
            [sg.Button(f"Host: [host username]", font=("Default font", 10), border_width=0, k=f"-HOST{i}-")],
            [sg.Button(f"Members: 0", font=("Default font", 15), border_width=0, k=f"-MEMBERS{i}-")],
            [sg.VPush()]
        ], border_width=1)]
        for i in range(1,4)
    )
]

home_layout = [
    [sg.VPush()],
    [ # two centralised columns
        sg.Push(),
        # column 1 - Friends List
        sg.Frame("", [ #todo remove border
            [sg.Text("Friends List:", font= ("Default font", title_size))],
            [sg.Column(friends_layout, scrollable=True)]
        ], border_width=1),
        # column 2 - Chat Rooms
        sg.Frame("", [ #todo remove border
            [sg.Text("Open chat rooms", font= ("Default font", title_size))],
            [sg.Text("No open rooms! Click below to open a new room")],
            [sg.Column([#chatrooms_layout goes here
                        ])],
            [sg.Button("Create new room", font=("Default font", main_button_size), k="-NEW-ROOM-")]
        ], border_width=1),
        sg.Push()
    ],
    [sg.VPush()],
]


# Messaging
# todo wip

messagingroom_layout = [[sg.VPush()],
              [sg.Text("NOT CONNECTED")],
              #[sg.Text("Server address:"), sg.Text(server_ip)],
              [sg.Text(s=(40, 1), k="-OUTPUT1-")],
              [sg.Text(s=(40, 1), k="-OUTPUT2-")],
              [sg.Text(s=(40, 1), k="-OUTPUT3-")],
              [sg.Text(s=(40, 1), k="-OUTPUT4-")],
              [sg.Text(s=(40, 1), k="-OUTPUT5-")],
              [
                  sg.Push(), sg.Text("Enter your name:", s=(15, 1), k="-PROMPT-"),
                  sg.Input(s=(15, 1), k="-MESSAGE-", do_not_clear=False),
                  sg.Button("send", bind_return_key=True, k="-SEND-MESSAGE-"), sg.Push()
              ],
              [sg.VPush()]]




# MAIN LAYOUT

pages = {
    "-SIGNUP-PAGE-": page_classes.SignUp("-SIGNUP-PAGE-", signup_layout),
    "-CUSTOMISE-PAGE-": page_classes.Customise("-CUSTOMISE-PAGE-", customise_profile_layout),
    "-LOGIN-PAGE-": page_classes.LogIn("-LOGIN-PAGE-", login_layout),
    "-RECOVERY-PAGE-": page_classes.Recovery("-RECOVER-PAGE-", account_recovery_layout),
    "-CONNECT-PAGE-": page_classes.Connect("-CONNECT-PAGE-", connection_layout),
    "-HOME-PAGE-": page_classes.Home("-HOME-PAGE-", home_layout),
    "-MESSAGING-PAGE-": page_classes.Messaging("-MESSAGING-PAGE-", messagingroom_layout)
}

page_tabs = [[sg.Tab("", page.get_layout(), visible=False, k=page.get_name()) for page in pages.values()]]

main_layout = [
    [sg.Text("")],
    [sg.Text("APP NAME", font=("Default font", app_name_size))],
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