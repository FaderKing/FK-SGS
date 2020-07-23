from client import Client

player = Client("127.0.0.1", 3345, 3345, 3346)

player.create_room("test_room")

player.join_room("test_room")