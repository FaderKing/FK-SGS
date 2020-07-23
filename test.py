from client import Client

# Add Client instance to your game
client = Client("127.0.0.1", 1234, 1234, 1235)

# Get room list (room_id, nb_players, capacity)
rooms = client.get_rooms()

# You can join a room using room identifier
client.join_room("id")

# You can autojoin the first available room client.autojoin()
# Or you can create a new room with client.create_room("room_name")

# In your game main loop
while game_is_running:
    # Data to send
    data = {"foo": "bar", "baz": "gu"}

    # Send data to all players in the room
    client.send(data)
  
    # Send data to one player in the room
    client.sendto(someone.identifier, data)

    # Send data to multiple players in room
    players_ids = [player1.identifier, player2.identifier]
    client.sendto(players_ids, data)

    # Read received messages
    messages = client.get_messages()
    if len(messages) != 0:
        for message in message:
            do_something_with_message(message)