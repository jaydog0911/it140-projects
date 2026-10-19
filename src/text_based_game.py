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

    # TODO: Create the gameplay loop.
    # Within the loop:
    #   - Show player status.
    #   - Prompt for the player's next command.
    #   - Handle valid movement commands.
    #   - Handle valid get-item commands.
    #   - Validate invalid commands.
    #   - Update room/inventory state when appropriate.
    #   - Detect and display the required winning outcome.
    #   - Detect and display the required losing outcome.
    #   - End the loop when the player has won or lost.
    pass


if __name__ == "__main__":
    main()
