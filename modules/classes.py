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
    def __init__(self, new_username):
        self.__username = new_username