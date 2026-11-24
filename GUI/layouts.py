import PySimpleGUI as sg # library for GUI
import time

# CONSTANTS

APP_NAME_SIZE = 40
MAIN_FONT = "Default font"
TITLE_SIZE = 30
SUBTITLE_SIZE = 20
INPUT_OUTPUT_SIZE = 28
MAIN_BUTTON_SIZE = 18
FRAME_TITLE_SIZE = 12
FRAME_BORDER_SIZE = 5
SINGLE_FRAME_SIZE = (500,250)
DUAL_FRAME_SIZE = (250,250)
DUAL_COLUMN_SIZE = (350, 350)
MAIN_FRAME_SIZE = (1000,700)
DUAL_FRAME_BUTTON_SIZE = (27,1)
TEXTBOX_SIZE = (30,7)
MESSAGING_PAGE_SIZE = (700,400)
MESSAGE_SENDER_SIZE = 15
MESSAGE_SIZE = 12
TIME_SIZE = 8
MESSAGE_PADDING = 5
PROMPTBOX_SIZE = (15,1)
DESCRIPTION_SIZE = 10
ROOM_FRAME_SIZE = (300,100)
INITIAL_METADATA = 0
ICON_SIZE = 4
BACK_BUTTON_SIZE = 3
BACKGROUND_COLOUR = "grey94"
APP_THEME = "SystemDefault1"

sg.theme(APP_THEME)  # sets theme

# LAYOUTS

SIGNUP_LAYOUT = [
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
    ], size=DUAL_FRAME_SIZE, border_width=False), sg.Frame("", [
        [sg.VPush()],
        [sg.Text("enter password:")],
        [sg.Input(password_char="*", size=INPUT_OUTPUT_SIZE, key="-SIGNUP-PASSWORD-"),
         sg.Button("", image_filename="media\\eye_open.png", image_subsample=ICON_SIZE, metadata=INITIAL_METADATA,
                   key="-VIEW-SIGNUP-PASSWORD-")],
        [sg.Text("confirm password:")],
        [sg.Input(password_char="*", size=INPUT_OUTPUT_SIZE, key="-SIGNUP-CONFIRMPASSWORD-"),
         sg.Button("", image_filename="media\\eye_open.png", image_subsample=ICON_SIZE, metadata=INITIAL_METADATA,
                   key="-VIEW-SIGNUP-CONFIRMPASSWORD-")],
        [sg.VPush()],
        [sg.Text("")]
    ], size=DUAL_FRAME_SIZE, border_width=False), sg.Push()],
    [sg.Push(), sg.Button("sign up", font=(MAIN_FONT, SUBTITLE_SIZE), key="-SIGN-UP-"), sg.Push()],
    [sg.Text("")]
]

CUSTOMISE_PROFILE_LAYOUT = [
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
# new image file       ^^^^^^^^^^^^^^^^^
                [sg.Text("example_username", # placeholder for username
                         size=INPUT_OUTPUT_SIZE, key="-CUSTOMISE-USERNAME-")],
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

LOGIN_LAYOUT = [
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
         sg.Button("",
                   image_filename="media\\eye_open.png",
                   image_subsample=ICON_SIZE,
                   metadata=INITIAL_METADATA,
                   key="-VIEW-LOGIN-PASSWORD-")],
        [sg.Button("forgot password", key="-RECOVERY-FROM-LOGIN-")],
        [sg.Text(key="-LOGIN-OUTPUT-")],
    ], size=SINGLE_FRAME_SIZE, border_width=False),
     sg.Push()],
    [sg.Push(), sg.Button("log in", font=(MAIN_FONT, SUBTITLE_SIZE), key="-LOGIN-"), sg.Push()],
    [sg.Text("")]
]

HOME_LAYOUT = [
    [sg.VPush()],
    [ # two centralised columns (frames)
        sg.Push(),
        # column 1 - Friends List
        sg.Frame("", [
            [sg.Text("Friends List:", font= (MAIN_FONT, TITLE_SIZE))],
            [sg.Column([], size=DUAL_COLUMN_SIZE, scrollable=True, vertical_scroll_only=True, key="-FRIENDS-COLUMN-")] # todo friends list goes here
        ], size=DUAL_COLUMN_SIZE, border_width=FRAME_BORDER_SIZE),
        # column 2 - Chat Rooms
        sg.Frame("", [
            [sg.Text("Open chat rooms:", font= (MAIN_FONT, TITLE_SIZE))],
            [sg.Text("No open rooms! Click below to open a new room", visible=False, key="-NO-ROOMS-")],
            [sg.Button("Create new room", font=(MAIN_FONT, MAIN_BUTTON_SIZE), k="-NEW-ROOM-")],
            [sg.Column([], size=DUAL_COLUMN_SIZE, scrollable=True, vertical_scroll_only=True, key="-CHATROOM-COLUMN-")],
        ], size=DUAL_COLUMN_SIZE, border_width=FRAME_BORDER_SIZE),
        sg.Push()
    ],
    [sg.VPush()]
]

MESSAGING_LAYOUT = [
    [sg.VPush()],
    [sg.Push(), sg.Frame("", [
        [
            sg.Button("", image_filename="media\\back.png", image_subsample=BACK_BUTTON_SIZE, key="-LEAVE-ROOM-"),
            sg.Text("", font=(MAIN_FONT, SUBTITLE_SIZE), key="-ROOM-NAME-"),
            sg.Push(),
            sg.Text("", key="-MEMBERS-")
        ],
        [sg.Multiline(
            reroute_cprint=True,
            expand_x=True,
            expand_y=True,
            autoscroll=True,
            background_color=BACKGROUND_COLOUR,
            border_width=False,
            disabled=True,
            key="-TEXT-OUTPUT-")],
        [
            sg.Text("Type message here:", size=PROMPTBOX_SIZE),
            sg.Input(size=PROMPTBOX_SIZE, key="-MESSAGE-", expand_x=True, do_not_clear=False),
            sg.Button("send", bind_return_key=True, key="-SEND-MESSAGE-"), sg.Push()
        ],
    ], size=MESSAGING_PAGE_SIZE, border_width=1), sg.Push()],
    [sg.VPush()]
]

CONNECTING_LAYOUT = [
    [sg.Push(), sg.Text("Connecting...", font=(MAIN_FONT, TITLE_SIZE)), sg.Push()],
    [sg.Text("Please wait.")],
]

def create_main_layout(page_tabs):
    layout = [
        [sg.Push(), sg.Frame("", [
    [sg.Text("")],
        [sg.Text("", font=(MAIN_FONT, APP_NAME_SIZE))], #app name
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
    return layout

def update_chatroom_column(window, chatroom_list):
    if len(chatroom_list) == 0: # if there are no rooms available
        window["-NO-ROOMS-"].update(visible=True)
    else:
        chatroom_list_layout = []
        for i in range(len(chatroom_list)):
            try:
                key = chatroom_list[i]['id']
                frame = window[key]
            except KeyError:
                print("adding new room with id", chatroom_list[i]['id'])
                new_frame = [sg.Frame("", [
                [sg.VPush()],
                [sg.Button(
                    button_text=f"{chatroom_list[i]['name']}",
                    font=(MAIN_FONT, FRAME_TITLE_SIZE),
                    tooltip="Click to join!",
                    border_width=False,
                    k=f"-ROOM-{i}-"
                )],
                [sg.Text(f"Host: {chatroom_list[i]['host']}", font=(MAIN_FONT, DESCRIPTION_SIZE), k=f"-HOST{i}-")],
                [sg.Text(f"Members: {str(len(chatroom_list[i]['members']))}", font=(MAIN_FONT, DESCRIPTION_SIZE), k=f"-MEMBERS{i}-")],
                [sg.VPush()]
                ], size=ROOM_FRAME_SIZE, key=chatroom_list[i]['id'])]
                chatroom_list_layout.append(new_frame)

        window.extend_layout(window["-CHATROOM-COLUMN-"], chatroom_list_layout)
    window["-CHATROOM-COLUMN-"].contents_changed()


def update_screen(message_dict):
    """
    procedure to handle updating the display with the most recent messages
    """

    message_type = message_dict["message_type"]

    if message_type == "-TEXT-":  # A message sent from a user to a chat room
        sender = message_dict["sender"]
        content = message_dict["content"] + " "
        time_sent = message_dict["time_sent"]
        time_sent_string = "(" + get_time_string(time_sent) + ")"
        sg.cprint(sender, font=(MAIN_FONT, MESSAGE_SENDER_SIZE))
        sg.cprint(content, font=(MAIN_FONT, MESSAGE_SIZE), end="")
        sg.cprint(time_sent_string, font=(MAIN_FONT, TIME_SIZE))
        sg.cprint()

    if message_type == "-SENT-":
        sender = "You" + "  "
        content = " " + message_dict["content"] + "   "
        time_sent = time.time()
        time_sent_string = "(" + get_time_string(time_sent) + ")"
        justification = "right"
        sg.cprint(sender, font=(MAIN_FONT, MESSAGE_SENDER_SIZE), justification=justification)
        sg.cprint(time_sent_string, font=(MAIN_FONT, TIME_SIZE), justification=justification, end="")
        sg.cprint(content, font=(MAIN_FONT, MESSAGE_SIZE), justification=justification)
        sg.cprint()



    elif message_type == "-JOIN-":  # A message sent by the server when a user joins the chat room
        user = message_dict["user"]
        message = f"{user} joined the chat."
        sg.cprint(message, font=(MAIN_FONT, MESSAGE_SIZE))
        sg.cprint()

    elif message_type == "-DISCONNECT-":  # A message sent by the server when a user leaves the chat room
        user = message_dict["user"]
        message = f"{user} has left the chat."
        sg.cprint(message, font=(MAIN_FONT, MESSAGE_SIZE))
        sg.cprint()

    elif message_type == "-WELCOME-":
        room_name = message_dict["room_name"]
        message = f"Welcome to {room_name}!"
        sg.cprint(message, font=(MAIN_FONT, MESSAGE_SIZE))
        sg.cprint()

    else:
        message = "Error: unknown message"
        print("[pc]", message)

def clear_screen(window):
    window["-TEXT-OUTPUT-"].update("")

def get_time_string(epoch_time):
    time_struct = time.localtime(epoch_time)
    hour, minute = time_struct.tm_hour, time_struct.tm_min
    if minute < 10:
        minute = "0" + str(minute)
    time_sent = f"{hour}:{minute}"
    return time_sent