import socket
import cbor2
from modules import sign_up, encryption

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

    def send_text(self, message_dict): # replaces old send()
        """
        takes a message as an input from the user and sends it to the server
        """
        message_bytes = message_to_bytes("-TEXT-", message_dict)
        self.encrypt_and_send(message_bytes)

    def receive(self): # replaces old receive()
        """
        receives new incoming messages from the server and displays them
        """
        self.__socket.settimeout(1) # times out if user has left room
        while True:
            try:
                incoming_message = self.__socket.recv(1024)
                if self.__encryption_cipher is not None:
                    message_bytes = encryption.decrypt_message(incoming_message, self.__encryption_cipher)
                else:
                    message_bytes = incoming_message
                message_dict = cbor2.loads(message_bytes)
                message_type = message_dict["message_type"]
                self.__window.write_event_value(("-RECEIVED-", message_type), message_dict)

            except TimeoutError: # constantly checks that user is still in room
                if not self.get_in_room():
                    return None # ends the thread if the user has left


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
        """
        sends the server the room id of the new room just joined
        """
        self.__in_room = True
        message_bytes = message_to_bytes("-SET-ROOM-ID-", {"room_id": new_room_id})
        self.encrypt_and_send(message_bytes)

    def sign_up(self, values):
        values_dict, message = sign_up.sign_up(values)
        if values_dict:
            message_bytes = message_to_bytes("-SIGN-UP-", values_dict)
            self.encrypt_and_send(message_bytes)
            incoming_message = self.__socket.recv(1024)
            response_bytes = encryption.decrypt_message(incoming_message, self.__encryption_cipher)
            response_dict = cbor2.loads(response_bytes)
            assert response_dict["message_type"] == "-SIGN-UP-RESULT-"
            result = response_dict["outcome"]
            if result == "-SUCCESS-":
                return result
            if result == "-ERROR-":
                error_message = "Username already exists."
                return error_message
        else:
            return message

    def log_in(self, username, password):
        message_bytes = message_to_bytes("-LOG-IN-", {"username": username})
        self.encrypt_and_send(message_bytes)
        incoming_message = self.__socket.recv(1024)
        response_bytes = encryption.decrypt_message(incoming_message, self.__encryption_cipher)
        response_dict = cbor2.loads(response_bytes)
        message_type = response_dict["message_type"]

        if message_type == "-ERROR-":
            result = response_dict["outcome"]
            if result == "-NOT-FOUND-":
                error_message = "Username not found."
            elif result == "-LOCKED-":
                error_message = "Error. Account is locked."
            else: error_message = result
            return error_message

        salt = response_dict["salt"]
        hashed_password = encryption.generate_hashed_password(password, salt)
        message_bytes = message_to_bytes("-HASHED-PASSWORD-", {"hashed_password": hashed_password})
        self.encrypt_and_send(message_bytes)
        incoming_message = self.__socket.recv(1024)
        result_bytes = encryption.decrypt_message(incoming_message, self.__encryption_cipher)
        result_dict = cbor2.loads(result_bytes)
        assert result_dict["message_type"] == "-RESULT-"
        result = result_dict["result"]
        if result == "-SUCCESS-":
            return result
        else:
            return "Password incorrect."

    def get_room_details(self):
        """
        asks the server for the details for the current room, returns the response
        """
        message_bytes = message_to_bytes("-GET-ROOM-DETAILS-", {})
        self.encrypt_and_send(message_bytes)
        incoming_message = self.__socket.recv(1024)
        room_details_bytes = encryption.decrypt_message(incoming_message, self.__encryption_cipher)
        room_details_dict = cbor2.loads(room_details_bytes)
        assert room_details_dict["message_type"] == "-ROOM-DETAILS-"
        room_details = room_details_dict["room_dict"]
        return room_details

    def get_chatrooms(self):
        self.__socket.settimeout(None)
        """
        asks the server for a list of all the currently open chat rooms and returns the result
        """
        message_bytes = message_to_bytes("-GET-CHATROOMS-", {})
        self.encrypt_and_send(message_bytes)
        incoming_message = self.__socket.recv(1024)
        chatrooms_bytes = encryption.decrypt_message(incoming_message, self.__encryption_cipher)
        chatrooms_dict = cbor2.loads(chatrooms_bytes)
        assert chatrooms_dict["message_type"] == "-CHATROOMS-"
        chatrooms = chatrooms_dict["chatrooms"]
        return chatrooms

    def leave_room(self):
        """
        informs the server that the user has left the current room
        """
        self.set_in_room(False)
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