class Chat:
    def __init__(self, new_roomname, new_members):
        self.roomname = new_roomname
        self.members = new_members


class ChatRoom(Chat):
    def __init__(self, new_roomname, new_members, new_host, new_roomtype):
        super().__init__(new_roomname, new_members)
        self.host = new_host
        self.roomtype = new_roomtype


class User:
    def __init__(self, new_username):
        self.username = new_username