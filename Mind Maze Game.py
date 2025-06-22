

# This will be my prototype text-based game
# The object of the game is to find all 6 items
# The player should go to each room using directional commands
# prefixed with 'go'. If a room has an item in it then
# they can add that item to their inventory using "get <iem>".
# If the player enters a room with the villain inside
# they lose. Once the player finds all 6 items they win the game


###################################################################################################################
###################################################################################################################

# Defining rooms dictionary to contain all the rooms, the valid directions from each room, and the items (if any)
# in that room. The item is also a dictionary with its own key:values

rooms = {
    'Sunlit Atrium': {
        'description': 'The Sunlit Atrium boasts magnificent architecture, with a mosaic floor and a glass ceiling\n'
                       'that allows natural light to gently kiss every corner. Grand glass doors lead to rooms in the\n'
                       'North, East, and West.\n',
        'North': 'Hall of Bravery',
        'East': 'Forge of Resilience',
        'West': 'Room of Comfort'},

    'Room of Comfort': {
        'description': 'The Room of Comfort immediately surrounds you with a sense of comfort and tranquility. A soft\n'
                       'ambient light filters through sheer curtains on the East wall, casting a gentle glow over the\n'
                       'room. A door to the North leads to another area.\n',
        'North': 'Library of Validation',
        'East': 'Sunlit Atrium',
        'item': {'name': 'Blanket of Solace',
                 'description': 'As you touch the blanket you immediately get the sense that this is the Blanket of Solace.\n'
                                'The soft and luxurious silkiness of the blanket brings a wave of calmness as it\n'
                                'brushes against your skin. The blanket embodies comforting moments and evokes a deep\n'
                                ' reassurance as your trace your fingers along the intricate and mesmerizing patterns,\n'
                                'before tucking it away in your inventory.\n',
                 'type': 'blanket',
                 'end': ' wraps you in a comforting embrace, soothing your doubts and providing reassurance\n'
                        'during difficult times.',
                 'hasItem': False},
    },

    'Library of Validation': {
        'description': 'The Library of Validation is lined meticulously with large, towering bookshelves that stretch\n'
                       'towards the ceiling. The shelves are filled with volumes of all sizes with promises of wisdom\n'
                       'and knowledge. A vacant desk to the East stands as the sole area that has collected dust over\n'
                       'the years, rendering its surface untouched and forgotten. Soft light filters through tall,\n'
                       'arched windows that cast a soft glow on the polished wooden floors and the doors to the South\n'
                       'and East\n',
        'East': 'Hall of Bravery',
        'South': 'Room of Comfort',
        'item': {'name': 'Letter of Recognition',
                 'description': 'Once you pick up this elegant letter, words scribble themselves on the parchment in unknown ink.\n'
                                'As the ink settles, the message becomes clear, imparting a very validating message\n'
                                'from an old professor, each word chosen with care. The letter acknowledges your hard\n'
                                'work and perseverance, reminding you how dedicated you are and dispelling any\n'
                                'self-doubt you started feeling. It then becomes apparent to you what this is when you\n'
                                'fold the parchment up and tuck it away, mouthing the exact item it is - the Letter of Recognition.\n',
                 'type': 'letter',
                 'end': ' acknowledges your hard work and perseverance, dispelling any lingering\n'
                        'self-doubt and validating your efforts.',
                 'hasItem': False}
    },

    'Hall of Bravery': {
        'description': "The Hall of Bravery engulfs you in a whirling darkness, where the flickers of lit sconces\n"
                       "along the brick walls struggle to pierce the gloom. Soft, but meaningful whispers float\n"
                       "through the air, carrying a palpable sense of resonating confidence, but also despair. A large\n"
                       "red carpet lines the middle of the floor in the hall, leading from one end to the other.\n"
                       "The flickering flames from the sconces illuminate the hall just enough to see a door embedded\n"
                       "in the middle of the wall in each direction.",
        'North': 'Garden of Reflection',
        'East': 'Sanctuary of Acceptance',
        'South': 'Sunlit Atrium',
        'West': 'Library of Validation',
        'item': {'name': 'Medal of Confidence',
                 'description': 'As you pick the medal up from the pedestal along the wall in the hallway its glow\n'
                                'intensifies, casting a comforting light around you. The weight feels substantial and\n'
                                'heavy, a shining testament to the inner strength and confidence it represents.\n'
                                'You trace your fingers along the intricate design, taking note of the sunburst pattern\n'
                                'etched around the edges. Turning it over words begin to etch themselves on the back:\n'
                                '"Your confidence lights the way". You are suddenly filled with a great burst of\n'
                                'confidence as you gently place the Medal of Confidence in your inventory.\n',
                 'type': 'medal',
                 'end': ' reinforces your confidence, reminding you of your inner strength and\n'
                        'ability to overcome challenges.',
                 'hasItem': False
                 }
    },

    'Garden of Reflection': {
        'description': 'The enchanting Garden of Reflection brightens even the most darkest of moods with the vibrant\n'
                       'colors of flowers and vines growing in a harmonious display. Hues from deep purples to\n'
                       'radiant yellows create a tapestry of color that delights the senses. A large glass dome\n'
                       'encloses the entire garden, allowing vibrant light to filter through and reflect the vitality\n'
                       'of the garden. Vines twist and climb elegantly around trellises and archways, their lush\n'
                       'greenery a testament to the garden\'s exuberance. A large wooden door with vines and leaves\n'
                       'growing around it silently sits in the wall to the South and a similar one in the wall\n'
                       'to the East.\n',
        'East': 'Chamber of Shadows',
        'South': 'Hall of Bravery',
        'item': {'name': 'Mirror of Revelation',
                 'description': 'The moment you touch the mirror\'s intricate frame, you hear the words "Mirror of Revelation"\n'
                                'whisper in your head. The frame is adorned with delicate carvings of vines and leaves,\n'
                                'as if it were a natural extension of the garden. The glass is pristine and clear,\n'
                                'reflecting not only your image but a deeper, more introspective view of yourself.\n'
                                'As you gaze into the glass you see a montage of your memories, thoughts, and emotions.\n'
                                'Engraved along the top are the words: "In knowing yourself, you find your true strength".\n'
                                'A profound sense of self-awareness washes over you as you read the words.\n'
                                'You place the mirror in your inventory with a new, uplifting sense of yourself\n',
                 'type': 'mirror',
                 'end': ' reflects your true self, revealing the strength you possess within\n'
                        'helping you recognize your worth.',
                 'hasItem': False
                 }
    },

    'Chamber of Shadows': {
        'description': 'The darkness from the Chamber of Shadows reaches out to you with vigor and painfully snatches\n'
                       'you in its embrace. Your worries and woes have come to life and are inescapable.\n',
        'villain': True,
        'West': 'Garden of Reflection',
        'South': 'Sanctuary of Acceptance'},

    'Sanctuary of Acceptance': {
        'description': 'The room is softly illuminated by gentle, golden light that seems to emanate from the walls\n'
                       'themselves. The air is filled with a delicate, but calming fragrance, reminiscent of\n'
                       'blooming flowers and fresh rain. The words "Sanctuary of Acceptance" etched on the stone\n'
                       'archway in the middle of the room renders a tranquil sense of harmony in yourself.\n'
                       'As you walk further in the soft, lush carpeting muffles your footsteps, further enhancing the\n'
                       'sense of peace and quiet. Along the walls, you notice tapestries depicting scenes of unity\n'
                       'and harmony, their intricate designs telling stories of acceptance and understanding. Characters\n'
                       'depicted in the stories look vaguely familiar to you, but you are unable to recall\n'
                       'names for any of them. You take notice of the large door to the North and the one to the West.\n',

        'North': 'Chamber of Shadows',
        'West': 'Hall of Bravery',
        'South': 'Forge of Resilience',
        'item': {'name': 'Stone of Belonging',
                 'description': 'The smooth and polished stone has a gentle glow with an inviting warmth. It\'s adorned\n'
                                'with with intricate carvings of purposeful and harmonious interwoven symbols,\n'
                                'symbolizing unity and harmony. As you reach to pick up the stone a faint cacophony\n'
                                'of whispers gently brush your ear with: "Stone of Belonging". Picking up the stone you\n'
                                'have a sudden sense of peace and connection wash over you. The weight of the stone\n'
                                'feels perfectly balanced in your hand, further enhancing the senses of grounding and\n'
                                ' reassurance. The carvings come to life as you look the stone over and start to form\n'
                                'the words: "You are enough. You belong." causing them to profoundly resonate within\n'
                                'yourself. You begin to tear up a little as you delicately place the stone in your\n'
                                'inventory, feeling the sense of harmony and belonging stronger than before.\n',
                 'type': 'stone',
                 'end': ' grounds you with a deep sense of connection, making you feel that you\n'
                        'truly belong and are loved.',
                 'hasItem': False
                 }
    },

    'Forge of Resilience': {
        'description': 'The thick air with the smell of molten metal and the hissing sounds of pressurized air releasing\n'
                       'immediately swarm your senses as you walk in. In the far corner, a forge glows with an intense heat,\n'
                       'casting long shadows that dance on the stone walls. To the right of the forge stands an anvil,\n'
                       'forged from an unbreakable metal, its surface scarred by countless strikes. Each time the\n'
                       'pressurized air escapes, it seems to carry a whisper, echoing the name - Forge of Resilience.\n',
        'North': 'Sanctuary of Acceptance',
        'West': 'Sunlit Atrium',
        'item': {
            'name': 'Unbreakable Chain',
            'description': 'The links of the chain have a glossy sheen, a clear indication of its indestructible condition.\n'
                           'As you gently caress the chains, faint whispers of its name reverberate in your mind - Unbreakable Chain.\n'
                           ' A sense of resilience stirs within you, as if the chain itself is a reminder of the strength\n'
                           'you possess.You have a refreshed sense of tenacity as you place the chain in your inventory.\n',
            'type': 'chain',
            'end': ' symbolizes your resilience, unyielding and strong, a reminder that you can\n'
                   'withstand any challenge.',
            'hasItem': False
        }
    }

}


def instructions():
    print(
        "**************************************************************************************************************************")
    print("You have been inducted into the Mind Maze by the villain, Imposter Syndrome")
    print("You must explore the rooms and find the 6 items to defeat the villain.\n")
    print(
        "To move to a room use the command 'go' followed by a direction: North, East, South, or West.\n\n Example: "
        "'go North'\n\n")
    print(
        "To add an item to your inventory use the command 'get' followed by the item name.\n\nExample: 'get Shield'\n\n")
    print("If at any time you would like to exit the game simply type 'exit'!\n")
    print(
        "The villain is lurking in one of the rooms - if you enter a room with them in there before getting all of "
        "the items")
    print("you will be overcome by self-doubt from Imposter Syndrome. Good luck!")
    print(
        "**************************************************************************************************************************")


def commandInstructions():
    print("***************************************************************")
    print("The list of valid commands are:")
    print("'go North'")
    print("'go East'")
    print("'go South'")
    print("'go West'")
    print("'get <item>' without the <>")
    print("***************************************************************")


# The display status function will be called after every command received from the player
# It takes in the player_position and inventory arguments for display purposes
def display_status(player_position, inventory):
    print("***************************************************************")
    print(f"* You are currently in: {player_position:<30}*")
    if player_position == 'Sunlit Atrium' or rooms[player_position]['item'].get('hasItem', True):
        print("*                                                              ")
        print(f"* This room has no items available!")
    print("*                                                              ")
    print(f"* Inventory: {', '.join(inventory) if inventory else 'Empty':<40}*")
    print("***************************************************************")


# The get_command function should take in the arguments for a player input (the command), player_position, and inventory
# in order to call the right functions and pass the right arguments.
# We split the command to extract either 'go', 'get', or 'exit' and call the right function
# We then pass our player_position and inventory as needed to those functions and then return player_position,
# inventory, and our flag (boolean) as a tuple

# NOTE: This function should always receive the three arguments in that specific order AND this function will always
# pass player_position, inventory, and our flag in the specified order - since a tuple with 3 values in it is returned
# the receiving variables should be in the same order otherwise TypeErrors can occur (inventory is a list)
def get_command(input_command, player_position, inventory):
    flag = True
    command = input_command.split()
    if command[0] == 'go' and len(command) > 1:
        player_position, flag = move_player(command[1], player_position)
    elif command[0] == 'get' and len(command) > 1:
        inventory, flag = add_to_inventory(" ".join(command[1:]), player_position, inventory)
    elif command[0] == 'exit':
        print("Exiting the game. Thanks for playing!")
        return player_position, inventory, False
    else:
        # Want to reinstate the valid commands with the commandInstructions method
        print("Sorry, that command isn't recognized")
        commandInstructions()

    return player_position, inventory, flag


def move_player(direction, player_position):
    flag = True
    if direction.capitalize() in rooms[player_position]:
        player_position = rooms[player_position][direction.capitalize()]
        print(f"You have moved to the {player_position}\n")
        print(f"{rooms[player_position]['description']}\n")

        if 'item' in rooms[player_position] and rooms[player_position]['item']['hasItem'] is False:
            print(f"You also see a {rooms[player_position]['item']['type']}\n")

        if 'villain' in rooms[player_position] and rooms[player_position]['villain']:
            return player_position, game_over()

    else:
        # This is not the right error to populate...this populates if the direction is NOT capitalized
        print("No room in that direction!\n")
    return player_position, flag


def game_over():
    print("Oh this is bad...this is really bad...")
    print("Imposter Syndrome was able to take over your mind...")
    print("There is no coming back now....")
    print("You have lost :(")
    return False


def add_to_inventory(item, player_position, inventory):
    # Want to check if this item already exists in the inventory
    # and if so, print a message and return the inventory without
    # adding an item
    for inv_item in inventory:
        if item.lower() in inv_item.lower():
            print(f"You already have the {inv_item}\n")
            return inventory, True

    # If the 'item' key exists in our dictionary and 'hasItem' is not set to False
    # compare that the input value matches the 'type' key of the item in the room
    # then as long as the 'hasItem' is not set to False, append item to inventory
    # Then display the item's description and set the items 'hasItem' key to True (preventing
    # duplicate items) then do a check_inventory call
    if 'item' in rooms[player_position] and not rooms[player_position]['item'].get('hasItem', False):
        if rooms[player_position]['item']['type'].lower() == item.lower():
            if not rooms[player_position]['item'].get('hasItem', False):
                inventory.append(rooms[player_position]['item']['name'])
                print(f"{rooms[player_position]['item']['name']} added to inventory!\n")
                print("*" * 40, "\n")
                print(f"{rooms[player_position]['item']['description']}")
                rooms[player_position]['item']['hasItem'] = True

                flag = check_inventory(inventory)
                return inventory, flag
            else:
                print("You already have this item!")
        else:
            print(f"There is no {item} here!")
    else:
        # If the item isn't in the room
        print("This room doesn't have any items available.")

    return inventory, True


# Once the user obtains 6 items then they win the game
# Returning True or False for our flag to continue the game
def check_inventory(inv):
    if len(inv) == 6:
        print("\nYou have collected all of the items needed! Great job!")

        for item_name in inv:
            for room, details in rooms.items():
                if 'item' in details and details['item']['name'] == item_name:
                    print(f"\nThe {item_name} {details['item']['end']}")
        print("\nAll of these items have helped you overcome Imposter Syndrome!")
        return False
    return True


def main_game():

    # Our flag for the main game to continue running
    flag = True
    player_position = 'Sunlit Atrium'
    inventory = []

    instructions()
    print(f"{rooms[player_position]['description']}")

    while flag:
        display_status(player_position, inventory)
        command = input("Command>> ")
        player_position, inventory, flag = get_command(command, player_position, inventory)

# Run the game
main_game()
