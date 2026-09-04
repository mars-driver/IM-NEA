class Chat:
    def __init__(self, new_roomname, new_members):
        self.__roomname = new_roomname
        self.__members = new_members


class ChatRoom(Chat):
    def __init__(self, new_roomname, new_members, new_host, new_roomtype):
        super().__init__(new_roomname, new_members)
        self.__host = new_host
        self.__roomtype = new_roomtype


class User:
    def __init__(self):
        self.__username = None
        self.__pfp = None
        self.__bio = None

    # GETTERS AND SETTERS
    def get_username(self):
        return self.__username
    def get_pfp(self):
        return self.__pfp
    def get_bio(self):
        return self.__bio
    def set_username(self, new_username):
        self.__username = new_username
    def set_pfp(self, new_pfp):
        self.__pfp = new_pfp
    def set_bio(self, new_bio):
        self.__bio = new_bio

class Constants:
    def __init__(self, new_server_ip, new_port, new_pages, new_window, new_window_closed):
        self.server_ip = new_server_ip
        self.port = new_port
        self.pages = new_pages
        self.window = new_window
        self.window_closed = new_window_closed

class Variables:
    def __init__(self, new_user, new_client_object):
        self.user = new_user
        self.client_object = new_client_object