import PySimpleGUI as sg
import threading
from modules import client

def proto_GUI_client(server_ip, port):

    # ------------------- WINDOW CREATION ------------------
    layout = [[sg.VPush()],
              [sg.Text("THIS IS THE CLIENT")],
              [sg.Text("Server address:"), sg.Text(server_ip)],
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

    window = sg.Window("PROTO client", layout, resizable=True, element_justification="center")

    # ----------------- RUNNING THE CLIENT -----------------
    client_object = client.ChatClient(server_ip, port, window)
    connected = False
    messages = []

    # --------------------- EVENT LOOP ---------------------
    while not connected:
        event, values = window.read()
        print("event:", event, "values:", values)
        if event == sg.WINDOW_CLOSED:
            client_object.socket.close()
            break
        elif event == "send":
            name = values["-MESSAGE-"]
            client_object.connect(name)
            connected = True

    threading.Thread(target=client_object.receive).start()
    window["-PROMPT-"].update("Type message here:")

    while True:
        event, values = window.read()
        if event == sg.WINDOW_CLOSED:
            client_object.socket.close()
            break
        elif event == "send":
            message = values["-MESSAGE-"]
            messages.append(("You:", message))
            client_object.send(message)
            update_messages(messages, window)
        elif event == "-RECEIVED-":
            message = values["-RECEIVED-"]
            messages.append(("", message))
            update_messages(messages, window)

    client_object.socket.close()
    window.close()


def update_messages(messages, window):
    num_rows = 5
    visible_messages = messages[::-1]
    if len(messages) < num_rows:
        for _ in range(num_rows - len(messages)):
            visible_messages.append("")
    visible_messages = visible_messages[:num_rows][::-1]
    for i in range(num_rows):
        row = f"-OUTPUT{i+1}-"
        window[row].update(" ".join(visible_messages[i]))