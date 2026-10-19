"""Project Two starter for the student's text-based adventure game."""

# Jason Dean


def show_instructions():
    """Display the game objective and available commands."""
    print("Welcome to Whisperwood Manor!")
    print("Collect all 6 items before facing the Caretaker.")
    print("Move: go north, go south, go east, go west")
    print("Collect items: get <item name>")
    print("Avoid the Master Bedroom until you have all 6 items!")


def show_status(current_room, inventory, rooms):
    """Display the player's current game status."""
    print("\nCurrent Room:", current_room)
    print("Inventory:", inventory)

    if 'item' in rooms[current_room]:
        if rooms[current_room]['item'] not in inventory:
            print("You see:", rooms[current_room]['item'])


def main():
    """Run the main gameplay loop."""
    rooms = {
        'Front Hall': {
            'North': 'Master Bedroom',
            'West': 'Conservatory'
        },
        'Conservatory': {
            'East': 'Front Hall',
            'North': 'Study',
            'item': 'Lantern'
        },
        'Study': {
            'South': 'Conservatory',
            'North': 'Attic',
            'item': "Caretaker's Journal"
        },
        'Attic': {
            'South': 'Study',
            'East': 'Library',
            'item': 'Music Box'
        },
        'Library': {
            'West': 'Attic',
            'East': 'Kitchen',
            'item': 'Old Key'
        },
        'Kitchen': {
            'West': 'Library',
            'South': 'Basement',
            'item': 'Silver Knife'
        },
        'Basement': {
            'North': 'Kitchen',
            'West': 'Master Bedroom',
            'item': 'Crowbar'
        },
        'Master Bedroom': {
            'South': 'Front Hall',
            'East': 'Basement',
            'villain': 'The Caretaker'
        }
    }

        current_room = 'Front Hall'

        inventory = []

        show_instructions()

        while True:
        show_status(current_room, inventory, rooms)

        command = input("\nEnter your move: ").strip().lower()

        if command == 'quit':
            print("Thanks for playing!")
            break

        elif command.startswith('go '):
            direction = command[3:].strip().capitalize()

            if direction in rooms[current_room]:
                current_room = rooms[current_room][direction]
                print("You moved to the", current_room)
           

                if 'villain' in rooms[current_room]:
                    if len(inventory) == 6:
                        print("Congratulations! You collected all 6 items!")
                        print("You defeated the Caretaker!")
                        print("YOU WIN!")
                    else:
                        print("The Caretaker caught you!")
                        print("GAME OVER!")
                    break

            else:
                print("You can't go that way.")
           

        elif command.startswith('get '):
            item_name = command[4:].strip()
            room_item = rooms[current_room].get('item')

            if room_item and item_name == room_item.lower():
                if room_item not in inventory:
                    inventory.append(room_item)
                    print("You picked up the", room_item)
                else:
                    print("You already have that item.")
            else:
                print("That item is not in this room.")

        else:
            print("Invalid command. Please try again.")
    

if __name__ == "__main__":
    main()
