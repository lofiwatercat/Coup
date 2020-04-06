# This is the script for the card game Coup

import random

# Making a list of the character cards

char_deck = ['Duke', 'Assassin', 'Ambassador', 'Captain', 'Contessa'] * 3

random.shuffle(char_deck)

# making the treasury
treasury = 50

# Making a class for the players

class Player:
    def __init__(self, name):
        self.name = name
        self.cards = [[char_deck.pop(), 'hidden'], [char_deck.pop(), 'hidden']]
        self.coins = 2
    
    # method to get player stats
    def player_stats(self):
        print(self.name)
        for x in self.cards:
            print(x)
        print('coins:', self.coins)

    # method to add/remove coins
    def change_coins(self, number):
        self.coins = self.coins + number 

# making a list of the players, mapping name to the Player object

players = {}

############# START OF MOD ACTIONS #############

# this method prints everything a mod needs, including the rules and explanation of the mod actions 
def help():
    pass

# prints the rules
def help_rules():
    pass

# prints the mod actions and explanations for using them
def help_actions():
    pass
    
# making some methods to view the stats
def stats():
    print('Treasury:', treasury)
    print('Number of characters in deck:', len(char_deck))
    for x in players:
        print()
        x.player_stats()

# initializes the game state and returns outputs for each player
def init(names):



# pops a character from the deck
def get_one():
    print(char_deck.pop())
    random.shuffle(char_deck)

# pops two characters from the deck
def get_two():
    print(char_deck.pop(), char_deck.pop())
    random.shuffle(char_deck)

# now need to add characters back to the deck
def add_char(*args):
    for x in args:
        char_deck.append(x)
    random.shuffle(char_deck)

############# END OF MOD ACTIONS #############

# utility functions

'''
Checks the following:
    - [Number] arguments can be cast properly to ints
    - The # of arguments is correct
    - The player being referenced is in the player list
    - [Card] arguments are valid
'''

def command_verified(cmd_tokens, players=None):
    if len(cmd_tokens) < 1:
        return False
    
    cards = ['duke', 'assassin', 'captain', 'ambassador', 'captain', 'contessa']
    cmd = cmd_tokens[0]

    if cmd in ["help", "stats", "stats_mod", "get_two"]:
        return True
    elif cmd == "init":
        return len(cmd_tokens) >= 4 and len(cmd_tokens) <= 7 # allow 3 to 6 players, plus the "init" token in the command
   
    # require that players is initialized by init before running player-specific commands (add, remove, etc.)
    if type(players) is dict:
        if cmd == "add" or cmd == "remove":
            # verifies that the number argument is castable
            try:
                int(cmd[2])
                return len(cmd_tokens) == 3 and cmd[1] in players.keys() 
            except ValueError:
                return False
        elif cmd == "exchange":
            if len(cmd_tokens) == 3:
                return cmd[1] in players.keys() and cmd[2] in cards
            elif len(cmd_tokens) == 4:
                return cmd[1] in players.keys() and cmd[2] in cards and cmd[3] in cards
            else:
                return False
        elif cmd == "replace" or cmd == "kill":
            return len(cmd_tokens) == 3 and cmd[2] in cards and cmd[1] in players.keys()
        else:
            return False
    else:
        return False


def function_signature(cmd):
    if cmd == "help":
        return "help"
    elif cmd == "stats":
        return "stats"
    elif cmd == "stats_mod":
        return "stats_mod"
    elif cmd == "init":
        return "init [player1] [player2] [...] [playern]"
    elif cmd == "add":
        return "add [player] [number]"
    elif cmd == "remove":
        return "remove [player] [number]"
    elif cmd == "exchange":
        return "exchange [player] [card1] [optional, card2]"
    elif cmd == "replace":
        return "replace [player] [card]"
    elif cmd == "kill":
        return "kill [player] [card]"
    elif cmd == "get_two":
        return "get_two"
    else:
        return "not found"

'''
p1 = Player('Alan')
p2 = Player('Colin')
players.append(p1)
players.append(p2)
print(p2.name)
players.append(Player('Wilson'))
print(players.name)
'''

while True:
    cmd_tokens = input("Enter command: ").lower().split()

    invalid_input = (len(cmd_tokens) < 1) or not command_verified(cmd_tokens)
    while invalid_input:
        if len(cmd_tokens < 1):
            cmd_tokens = input("Empty command entered, please try again. Enter command: ").split()
        elif function_signature(cmd_tokens[0]) == "not found":
            cmd_tokens = input("Command not found, please try again. Enter command: ").split()
        else:
            print("Incorrect command arguments. Function signature of " + str(cmd_tokens[0]) + " is: ")
            print(function_signature(cmd_tokens[0]))
            print("Check that you have initialized players, that the player and card names are matching \nand that number arguments can be converted to integers.")

            cmd_tokens = input("Enter command: ")

        invalid_input = (len(cmd_tokens) < 1) or not command_verified(cmd_tokens)
 

    # call functions here, now that they're verified to be correct
    '''
    cmd = cmd_tokens[0]
    if cmd == "help":
        
    elif cmd == "stats":
        asdf
    elif cmd == "init":
        asdf
    else:
    '''



