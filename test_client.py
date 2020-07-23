from client import Client

player = Client("127.0.0.1", 1234, 1234, 1235)

player.create_room("test_room")

player.join_room("test_room")