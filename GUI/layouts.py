# ACCESSES: PSG, PAGE CLASSES

import PySimpleGUI as sg # library for GUI
from GUI import page_classes

sg.theme("SystemDefault1")  # sets theme

# CONSTANTS
APP_NAME_SIZE = 40
MAIN_FONT = "Default font"
TITLE_SIZE = 30
SUBTITLE_SIZE = 20
INPUT_OUTPUT_SIZE = 28
MAIN_BUTTON_SIZE = 18
SINGLE_FRAME_SIZE = (500, 250)
DUAL_FRAME_SIZE = (250,250)
MAIN_FRAME_SIZE = (700,700)
DUAL_FRAME_BUTTON_SIZE = (27,1)
TEXTBOX_SIZE = (30,7)
INITIAL_METADATA = 0
ICON_SIZE = 4
BACKGROUND_COLOUR = "grey94"
APP_THEME = "SystemDefault1"


sg.theme(APP_THEME)  # sets theme

# LAYOUTS

# Connection

connection_layout = [
    [sg.VPush()],
    [sg.Push(), sg.Text("Click below to join the chat room!", font=(MAIN_FONT, SUBTITLE_SIZE)), sg.Push()],
    [sg.Push(), sg.Button("JOIN", size=MAIN_BUTTON_SIZE, key="-CONNECT-"), sg.Push()],
    [sg.VPush()]
]

# Signup

signup_layout = [
    [sg.Push(), sg.Frame("", [
        [sg.Text("Already have an account?")],
        [sg.Button("log in here", size=MAIN_BUTTON_SIZE, key="-LOGIN-FROM-SIGNUP-")],
    ], border_width=False)],
    [sg.Text("")],
    [sg.Push(), sg.Text("Sign Up", font=(MAIN_FONT, TITLE_SIZE)), sg.Push()],
    [sg.Push(), sg.Frame("", [
        [sg.VPush()],
        [sg.Text("enter username:")],
        [sg.Input(default_text="admin", key="-SIGNUP-USERNAME-")],
        [sg.Text("enter email address:")],
        [sg.Input(key="-SIGNUP-EMAIL-")],
        [sg.VPush()],
        [sg.Text(key="-SIGNUP-OUTPUT-")],
    ], size=DUAL_FRAME_SIZE, border_width=False), sg. Frame("", [
        [sg.VPush()],
        [sg.Text("enter password:")],
        [sg.Input(password_char="*", size=INPUT_OUTPUT_SIZE, key="-SIGNUP-PASSWORD-"),
         sg.Button("", image_filename="media\\eye_open.png", image_subsample=ICON_SIZE, metadata=INITIAL_METADATA, key="-VIEW-SIGNUP-PASSWORD-")],
        [sg.Text("confirm password:")],
        [sg.Input(password_char="*", size=INPUT_OUTPUT_SIZE, key="-SIGNUP-CONFIRMPASSWORD-"),
         sg.Button("", image_filename="media\\eye_open.png", image_subsample=ICON_SIZE, metadata=INITIAL_METADATA, key="-VIEW-SIGNUP-CONFIRMPASSWORD-")],
        [sg.VPush()],
        [sg.Text("")]
    ], size=DUAL_FRAME_SIZE, border_width=False), sg.Push()],
    [sg.Push(), sg.Button("sign up", font=(MAIN_FONT, SUBTITLE_SIZE), key="-SIGN-UP-"), sg.Push()],
    [sg.Text("")]
]



# Customise

customise_profile_layout = [
    [sg.Push(), sg.Frame("", [
        [sg.Text("Already have an account?")],
        [sg.Button("log in here", size=MAIN_BUTTON_SIZE, key="-LOGIN-FROM-CUSTOMISE-")],
    ], border_width=False)],
    [sg.Text("")],
    [sg.Push(), sg.Text("Customise Profile", font=(MAIN_FONT, TITLE_SIZE)), sg.Push()],
    [sg.Text("")],
    [sg.Push(), sg.Frame("", [
        [sg.Text("Profile Preview:")],
        [sg.Frame("", [
            [sg.Image("media\\no_pfp.png", key="-SHOW-PFP-"), sg.Frame("", [
                [sg.Text("example_username", size=INPUT_OUTPUT_SIZE, key="-CUSTOMISE-USERNAME-")],
                [sg.Text("• Online", size=INPUT_OUTPUT_SIZE)]
            ], border_width=False)],
            [sg.Text("Bio:")],
            [sg.Text(key="-CUSTOMISE-SHOWBIO-", size=TEXTBOX_SIZE, background_color="#ffffff")]
        ], border_width=False)]], size=DUAL_FRAME_SIZE, border_width=False), sg.Frame("", [
        [sg.Text("Upload profile picture")],
        [sg.FileBrowse(button_text="choose file", file_types=(('PNG Image', '.png'),('JPEG Image', '.jpg')),
                       size=DUAL_FRAME_BUTTON_SIZE, enable_events=True, key="-CUSTOMISE-PFP-")],
        [sg.Text("Write bio")],
        [sg.Multiline(default_text="Start typing...",key="-CUSTOMISE-BIO-", size=TEXTBOX_SIZE, background_color="#ffffff")],
        [sg.Button("save", key="-SAVE-")]
    ], size=DUAL_FRAME_SIZE, border_width=False), sg.Push()],
    [sg.Push(), sg.Button("Confirm", font=(MAIN_FONT, SUBTITLE_SIZE), key="-CONFIRM-"), sg.Push()]
]



# Login

login_layout = [
    [sg.Push(), sg.Frame("", [
        [sg.Push(), sg.Text("Don't have an account?"), sg.Push()],
        [sg.Button("sign up here", size=MAIN_BUTTON_SIZE, k ="-SIGNUP-FROM-LOGIN-")]
    ], border_width=False)],
    [sg.Push(), sg.Text("Log In", font=(MAIN_FONT, TITLE_SIZE)), sg.Push()],
    [sg.Text("")],
    [sg.Push(),
     sg.Frame("", [
        [sg.Text("enter username:")],
        [sg.Input(expand_x=True, key="-LOGIN-USERNAME-", default_text="admin"),],
        [sg.Text("")],
        [sg.Text("enter password:")],
        [sg.Input(password_char="*", expand_x=True, key="-LOGIN-PASSWORD-"),
         sg.Button("", image_filename="media\\eye_open.png", image_subsample=ICON_SIZE, metadata=INITIAL_METADATA, key="-VIEW-LOGIN-PASSWORD-")],
        [sg.Button("forgot password", key="-RECOVERY-FROM-LOGIN-")],
        [sg.Text(key="-LOGIN-OUTPUT-")],
    ], size=SINGLE_FRAME_SIZE, border_width=False),
     sg.Push()],
    [sg.Push(), sg.Button("log in", font=(MAIN_FONT, SUBTITLE_SIZE), key="-LOGIN-"), sg.Push()],
    [sg.Text("")]
]



# Recovery

account_recovery_layout = [
    [sg.Text("")],
    [sg.Push(), sg.Button("back to log in", size=MAIN_BUTTON_SIZE, key="-LOGIN-FROM-RECOVERY-")],
    [sg.Text("")],
    [sg.Push(), sg.Frame("", [
        [sg.Push(), sg.Text("Account Recovery", font=(MAIN_FONT, TITLE_SIZE)), sg.Push()],
        [sg.Text("")],
        [sg.Push(),
         sg.Frame("", [
             [sg.Text("enter email associated with your account:")],
             [sg.Push(), sg.Input(key="-EMAIL-"), sg.Push()],
             [sg.Text(key="-RECORVERY-OUTPUT-")],
         ], border_width=False),
         sg.Push()],
        [sg.Text("")],
        [sg.Push(), sg.Button("Send email", font=(MAIN_FONT, SUBTITLE_SIZE), key="-SEND-EMAIL-"), sg.Push()],
    ], size=SINGLE_FRAME_SIZE, border_width=False), sg.Push()],
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
                sg.Column([[sg.Image("media\\no_pfp.png", enable_events=True, key=f"-PFP{i}-")]]),
                sg.Column([[sg.Button(friends[i][0], font=(MAIN_FONT, 15), border_width=0, key=f"-FRIEND{i}-")],
                           [sg.Button(friends[i][1], font=(MAIN_FONT, 12),
                                      border_width=1, key=f"-LASTMESSAGE{i}-")]])],
                [sg.VPush()]], size=(350,100))
     ] for i in range(len(friends))
]


chatroom_layout = [
    [sg.Text("Open chat rooms", font= (MAIN_FONT, SUBTITLE_SIZE))],
    (
        [sg.Frame("", [ #todo remove border
            [sg.VPush()],
            [sg.Button(f"Room Name {i}", font=(MAIN_FONT, 12), border_width=0, key=f"-ROOM{i}-")],
            [sg.Button(f"Host: [host username]", font=(MAIN_FONT, 10), border_width=0, key=f"-HOST{i}-")],
            [sg.Button(f"Members: 0", font=(MAIN_FONT, 15), border_width=0, key=f"-MEMBERS{i}-")],
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
            [sg.Text("Friends List:", font= (MAIN_FONT, TITLE_SIZE))],
            [sg.Column(friends_layout, scrollable=True)]
        ], border_width=1),
        # column 2 - Chat Rooms
        sg.Frame("", [ #todo remove border
            [sg.Text("Open chat rooms", font= (MAIN_FONT, TITLE_SIZE))],
            [sg.Text("No open rooms! Click below to open a new room")],
            [sg.Column([#chatrooms_layout goes here
                        ])],
            [sg.Button("Create new room", font=(MAIN_FONT, MAIN_BUTTON_SIZE), key="-NEW-ROOM-")]
        ], border_width=1),
        sg.Push()
    ],
    [sg.VPush()],
]


# Messaging
# todo wip

messagingroom_layout = [
    [sg.VPush()],
    [sg.Push(), sg.Frame("", [
        [
            sg.Button("", image_filename="media\\back.png", image_subsample=ICON_SIZE, key="-LEAVE-ROOM-"),
            sg.Text("Welcome to the chat room!", font=(MAIN_FONT, SUBTITLE_SIZE))],
        [sg.Text(size=(40, 1), key="-OUTPUT1-")],
        [sg.Text(size=(40, 1), key="-OUTPUT2-")],
        [sg.Text(size=(40, 1), key="-OUTPUT3-")],
        [sg.Text(size=(40, 1), key="-OUTPUT4-")],
        [sg.Text(size=(40, 1), key="-OUTPUT5-")],
        [
            sg.Text("Enter your name:", size=(15, 1), key="-PROMPT-"),
            sg.Input(size=(15, 1), key="-MESSAGE-", expand_x=True, do_not_clear=False),
            sg.Button("send", bind_return_key=True, key="-SEND-MESSAGE-"), sg.Push()
        ],
    ], size=SINGLE_FRAME_SIZE, border_width=0), sg.Push()],
    [sg.VPush()]
]

"""
[
            sg.Button("", image_filename="media\\back.png", image_subsample=ICON_SIZE, key="-LEAVE-ROOM-"),
            sg.Text("Room name:", font=(MAIN_FONT, SUBTITLE_SIZE)),
            sg.Text(key="-CURRENT-ROOM-NAME-", font=(MAIN_FONT, SUBTITLE_SIZE)),
            sg.Push(),
            sg.Text("Members:", font=(MAIN_FONT, SUBTITLE_SIZE)),
            sg.Text(key="-MEMBERS-", font=(MAIN_FONT, SUBTITLE_SIZE))
        ],
"""




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

page_tabs = [[sg.Tab("", page.get_layout(), visible=False, key=page.get_name()) for page in pages.values()]]

main_layout = [
    [sg.Push(), sg.Frame("", [
[sg.Text("")],
    [sg.Text("APP NAME", font=(MAIN_FONT, APP_NAME_SIZE))],
    [sg.Text("NOT LOGGED IN", key="-LOGGED-IN?-"), sg.Push(), sg.Text("NOT CONNECTED", key="-CONNECTED?-")],
    [sg.Text("")],
    [sg.Push(),
    sg.TabGroup(
        page_tabs,
        selected_background_color = BACKGROUND_COLOUR,
        background_color = BACKGROUND_COLOUR,
        border_width=False,
        tab_border_width=False
    ), sg.Push()],
    ], border_width=False, size=MAIN_FRAME_SIZE), sg.Push()]
]
