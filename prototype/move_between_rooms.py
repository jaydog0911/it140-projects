"""Module Six Milestone starter for the simplified movement prototype."""

# A dictionary for the simplified dragon text game.
# The dictionary links a room to other rooms.
rooms = {
    "Great Hall": {"south": "Bedroom"},
    "Bedroom": {"north": "Great Hall", "east": "Cellar"},
    "Cellar": {"west": "Bedroom"},
}


# Set the player's starting room for the simplified prototype.
current_room = "Great Hall"

# Create the gameplay loop required by the milestone.
while current_room != "exit":
    print()
    print("You are in the", current_room)

    command = input('Enter a movement command or "exit": ').lower().strip()

    if command == "exit":
        current_room = "exit"

    elif command.startswith("go "):
        direction = command[3:]

        if direction in rooms[current_room]:
            current_room = rooms[current_room][direction]
        else:
            print("Invalid direction.")

    else:
        print("Invalid command.")

print()
print("Thanks for playing!")
