import socket
import cbor2
from modules import encryption

class ChatClient:
    def __init__(self, host, port, window):
        self.__host = host
        self.__port = port
        self.__window = window
        self.__socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.__username = None
        self.__encryption_cipher = None
        self.__in_room = False

    # GETTERS & SETTERS

    def get_host(self):
        return self.__host
    def get_port(self):
        return self.__port
    def get_window(self):
        return self.__window
    def get_socket(self):
        return self.__socket
    def get_username(self):
        return self.__username
    def get_encryption_cipher(self):
        return self.__encryption_cipher
    def get_in_room(self):
        return self.__in_room
    def set_username(self, new_username):
        self.__username = new_username
        message_bytes = message_to_bytes("-USERNAME-", {"username": new_username})
        self.encrypt_and_send(message_bytes)
    def set_encryption_cipher(self, new_cipher):
        self.__encryption_cipher = new_cipher
    def set_in_room(self, new_in_room):
        self.__in_room = new_in_room

    # METHODS

    def send(self, message): # replaces old send()
        """
        takes a message as an input from the user and sends it to the server
        """
        message_bytes = message_to_bytes("-TEXT-", {
            "sender": self.__username,
            "content": message
        })
        self.encrypt_and_send(message_bytes)

    def receive(self): # replaces old receive()
        """
        receives new incoming messages from the server and displays them
        """
        while True:
            print("[client receive] is client in room:", self.get_in_room())
            if not self.get_in_room():
                print("[client receive] breaking receive loop now")
                break

            self.__socket.settimeout(5)

            try:
                incoming_message = self.__socket.recv(1024)
                print("[client receive] msg", incoming_message)
                if self.__encryption_cipher is not None:
                    message_bytes = encryption.decrypt_message(incoming_message, self.__encryption_cipher)
                else:
                    message_bytes = incoming_message
                message_dict = cbor2.loads(message_bytes)
                message_type = message_dict["message_type"]

                print("[client receive] message type:", message_type)

                print("[client receive] writing event -RECEIVED-")
                self.__window.write_event_value(("-RECEIVED-", message_type), message_dict)
                print("[client receive] event written")

            except TimeoutError:
                print("[client receive TIMEOUT CHECK] is client in room:", self.get_in_room())
                if not self.get_in_room():
                    print("[client receive TC] breaking receive loop now")
                    return None


    def connect(self):
        """
        uses sockets to establish a connection
        """
        self.__socket.connect((self.__host, self.__port))
        client_private_key, client_public_key = encryption.generate_new_keys()

        assert self.__encryption_cipher is None
        message_bytes = message_to_bytes("-KEY-", {
            "client_public_key_string": encryption.key_to_string(client_public_key)
        })
        self.__socket.send(message_bytes)
        server_keys_bytes = self.__socket.recv(1024)
        server_keys_dict = cbor2.loads(server_keys_bytes)
        assert server_keys_dict["message_type"] == "-SERVER-KEYS-"
        server_public_key_string = server_keys_dict["server_public_key_string"]
        server_public_key = encryption.string_to_key(server_public_key_string)
        signature = server_keys_dict["signature"]
        encryption.verify_server(signature, client_public_key, server_public_key)
        encryption_cipher = encryption.generate_cipher(client_private_key, server_public_key)

        self.__encryption_cipher = encryption_cipher

    def encrypt_and_send(self, message_bytes):
        """
        Encrypts the given message and sends it across the socket
        """
        encrypted_message = encryption.encrypt_message(message_bytes, self.__encryption_cipher)
        self.__socket.send(encrypted_message)

    def set_current_room_id(self, new_room_id):
        self.__in_room = True
        message_bytes = message_to_bytes("-CURRENT-ROOM-ID-", {"room_id": new_room_id})
        self.encrypt_and_send(message_bytes)

    def get_chatrooms(self):
        message_bytes = message_to_bytes("-CHATROOMS-", {})
        self.encrypt_and_send(message_bytes)
        print("[client get] waiting for chatrooms...")
        incoming_message = self.__socket.recv(1024) # its just waiting here...
        print("[client get] recieved message.. ready to decrypt")
        chatrooms_bytes = encryption.decrypt_message(incoming_message, self.__encryption_cipher)
        chatrooms_dict = cbor2.loads(chatrooms_bytes)
        print(chatrooms_dict["message_type"])
        assert chatrooms_dict["message_type"] == "-CHATROOMS-"
        chatrooms = chatrooms_dict["chatrooms"]
        print("[client get] chatrooms list aqcuired.. returning now")
        return chatrooms

    def leave_room(self):
        #self.set_in_room(False)
        message_bytes = message_to_bytes("-LEAVE-ROOM-", {})
        self.encrypt_and_send(message_bytes)


def message_to_bytes(message_type, values_dict):
    """
    A function which takes the message type and remaining items as parameters
    and returns the encoded equivalent in bytes
    """
    message_dict = {key: value for key,value in values_dict.items()}
    message_dict["message_type"] = message_type
    message_bytes = cbor2.dumps(message_dict)
    return message_bytes