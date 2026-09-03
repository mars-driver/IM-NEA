import socket

class ChatClient:
    def __init__(self, host, port, window):
        self.host = host
        self.port = port
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.name = None
        self.window = window

    def send(self, message):
        message_out = f"{self.name}: {message}"
        self.socket.send(message_out.encode("utf8"))

    def connect(self, name):
        self.socket.connect((self.host, self.port))
        self.name = name
        self.socket.send(name.encode("utf8"))

    def receive(self):
        while True:
            message = self.socket.recv(1024).decode("utf8")
            self.window.write_event_value("-RECEIVED-", message)

def initialise_client(server_ip, port, window):
    client_object = ChatClient(server_ip, port, window)
    return client_object