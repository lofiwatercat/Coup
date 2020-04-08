# This is the script for the card game Coup

import random
import copy

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
        self.revealed = []
    
    # method to get player stats
    def player_stats(self):
        print(self.name)
        for x in self.cards:
            print(x)
        print('coins:', self.coins)

# making a list of the players
players = {}

# making an order of players
order_of_players = []

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
def stats_mod():
    print('Treasury:', treasury)
    print('Number of characters in deck:', len(char_deck))
    for x in order_of_players:
        print()
        players[x].player_stats()

# shows the names of the players and their coins
def stats():
    for x in order_of_players:
        print()
        print(x)
        print(players[x].coins, 'coins')
        if len(players[x].revealed) != 0:
            print(players[x].revealed)

# adds coins to a player
def add(Player, int):
    if treasury > 0:
        Player.coins = Player.coins + int

# removes coins from a player
def remove(Player, int):
    if Player.coins >= int:
        Player.coins = Player.coins - int

# initalizes the players
def init(*args):
    for x in args:
        players[x] = Player(x)
        order_of_players.append(x)
        global treasury
        treasury = treasury - 2

# shows two characters from the deck (read-only)
def get_two():
    print(char_deck[-1], char_deck[-2])
    random.shuffle(char_deck)

# now need to add characters back to the deck
def add_char(*args):
    for x in args:
        char_deck.append(x.capitalize())
    random.shuffle(char_deck)

def exchange(player, card1, card2=None):
    card1 = card1.capitalize()

    if card2 == None: # there is one hidden card
        for i, card in enumerate(player.cards): # card[0] is the name of the card, card[1] is the state (hidden or revealed)
            if card[1] == 'hidden':
                # return card to deck
                char_deck.append(card[0])

                # add card1 to player
                player.cards[i][0] = card1

                # remove card1 from deck
                char_deck.remove(card1)

    else: # if you are replacing with 2 cards, both cards held by the player are hidden (replace both)
        card2 = card2.capitalize()

        char_deck.append(player.cards[0][0])
        char_deck.append(player.cards[1][0])

        player.cards[0][0] = card1
        player.cards[1][0] = card2

        char_deck.remove(card1)
        char_deck.remove(card2)

    random.shuffle(char_deck)

# reveals a character card
def kill(Player, str):
    str = str.capitalize()
    for x in Player.cards:
        if x[0] == str and x[1] == 'hidden':
            x[1] = 'revealed'
            Player.revealed.append(x[0])
            break

# replaces the player's character card with a random card from the deck
def replace(Player, str):
    str = str.capitalize()
    for x in Player.cards:
        if x[0] == str and x[1] == 'hidden':
            x[0] = char_deck.pop()
            char_deck.append(str)
            break
    random.shuffle(char_deck)


############# END OF MOD ACTIONS #############

init('Alan', 'Colin', 'Wilson') 
players['Alan'].player_stats()
kill(players['Alan'], 'Assassin')
stats()
replace(players['Alan'], 'Duke')
players['Alan'].player_stats()
remove(players['Alan'], 2)
players['Alan'].player_stats()
stats()
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

# game loop
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



