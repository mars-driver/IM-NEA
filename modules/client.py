import socket

class ChatClient:
    def __init__(self, host, port, window):
        self.host = host
        self.port = port
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.name = None
        self.window = window

    def send(self, message):
        """
        sends the given message to the server
        """
        message_out = f"{self.name}: {message}"
        self.socket.send(message_out.encode())

    def connect(self, name):
        """
        uses sockets to establish a connection
        """
        self.socket.connect((self.host, self.port))
        self.name = name
        self.socket.send(name.encode())

    def receive(self):
        """
        receives new incoming messages from the server and displays them
        """
        while True:
            message = self.socket.recv(1024).decode()
            self.window.write_event_value("-RECEIVED-", message)