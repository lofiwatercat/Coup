# This is the script for the card game Coup

import random
import copy

# Making a list of the character cards

char_deck = ['Duke', 'Assassin', 'Ambassador', 'Captain', 'Contessa'] * 3
random.shuffle(char_deck)

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
            print(str(x[0]) + ": " + x[1])
        print('Coins:', self.coins)

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
    print('\nNumber of characters in deck:', len(char_deck))
    for x in order_of_players:
        print()
        players[x].player_stats()
    print()

# shows the names of the players and their coins
def stats():
    for x in order_of_players:
        print()
        print(x)
        print("Coins:", players[x].coins)
        if len(players[x].revealed) != 0:
            print("Revealed: ", end="")
            for elem in players[x].revealed:
                print(elem, end=" ")
            print()
    print()

# adds coins to a player
def add(player, coins):
    coins = int(coins)
    player.coins = player.coins + coins

# removes coins from a player
def remove(player, coins):
    coins = int(coins)
    if player.coins >= coins:
        player.coins = player.coins - coins
    else:
        player.coins = 0

# initalizes the players
def init(player_list):
    global players, order_of_players, char_deck
    players = {}
    order_of_players = []
    char_deck = ['Duke', 'Assassin', 'Ambassador', 'Captain', 'Contessa'] * 3
    random.shuffle(char_deck)

    print("Initialized: ", end='')
    for x in player_list:
        print(x, end=' ')
        players[x] = Player(x)
        order_of_players.append(x)
    print('\n')

# shows two characters from the deck (read-only)
def get_two():
    print(char_deck[-1], char_deck[-2] + '\n')
    random.shuffle(char_deck)

# now need to add characters back to the deck
def add_char(*args):
    for x in args:
        char_deck.append(x.capitalize())
    random.shuffle(char_deck)

# if abused by mod, this doesn't stop the mod from reviving a dead player by
# exchanging two cards with new cards, or restoring a card to a player by
# exchanging two cards with new cards when a player only has 1 left.
# input validation has not yet been made for if the mod grants a player
# cards that are not available in the deck; this behavior may break the system
# finally, exchanging 1 card when a player has 2 cards will swap the first card
# with the new card, do not do this
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
def kill(player, str):
    str = str.capitalize()
    for x in player.cards:
        if x[0] == str and x[1] == 'hidden':
            x[1] = 'revealed'
            player.revealed.append(x[0])
            break

# replaces the player's character card with a random card from the deck
def replace(player, str):
    str = str.capitalize()
    for x in player.cards:
        if x[0] == str and x[1] == 'hidden':
            x[0] = char_deck.pop()
            char_deck.append(str)
            break
    random.shuffle(char_deck)


############# END OF MOD ACTIONS #############

# testing
'''
init('Alan', 'Colin', 'Wilson') 
players['Alan'].player_stats()
kill(players['Alan'], 'Assassin')
stats()
replace(players['Alan'], 'Duke')
players['Alan'].player_stats()
remove(players['Alan'], 2)
players['Alan'].player_stats()
stats()
'''


# utility functions

# non-case sensitive comparison
def str_in_list(s, str_list):
    for elem in str_list:
        if s.lower() == elem.lower():
            return True
    return False

'''
Checks the following:
    - [Number] arguments can be cast properly to ints
    - The # of arguments is correct
    - The player being referenced is in the player list
    - [Card] arguments are valid
'''

def command_verified(cmd_tokens, players):
    if len(cmd_tokens) < 1:
        return False
    
    cards = ['Duke', 'Assassin', 'Captain', 'Ambassador', 'Contessa']
    cmd = cmd_tokens[0]

    if cmd in ["help", "help_rules", "help_actions", "stats", "stats_mod", "get_two"]:
        return len(cmd_tokens) == 1
    elif cmd == "init":
        return len(cmd_tokens) >= 4 and len(cmd_tokens) <= 7 # allow 3 to 6 players, plus the "init" token in the command
   
    # require that players is initialized by init before running player-specific commands (add, remove, etc.)
    if len(players) > 0:
        if cmd == "add" or cmd == "remove":
            # verifies that the number argument is castable
            try:
                int(cmd_tokens[2])
                return len(cmd_tokens) == 3 and cmd_tokens[1] in players.keys() 
            except ValueError:
                return False
        elif cmd == "exchange":
            if len(cmd_tokens) == 3:
                return cmd_tokens[1] in players.keys() and str_in_list(cmd_tokens[2], cards)
            elif len(cmd_tokens) == 4:
                return cmd_tokens[1] in players.keys() and str_in_list(cmd_tokens[2], cards) and str_in_list(cmd_tokens[3], cards)
            else:
                return False
        elif cmd == "replace" or cmd == "kill":
            return len(cmd_tokens) == 3 and str_in_list(cmd_tokens[2], cards) and cmd_tokens[1] in players.keys() 
        else:
            return False
    else:
        return False


def function_signature(cmd):
    if cmd in ["help", "help_rules", "help_actions", "stats", "stats_mod", "get_two"]:
        return cmd
    elif cmd == "init":
        return "init [player1] [player2] [...] [playern]"
    elif cmd in ["add", "remove"]:
        return cmd + " [player] [number]"
    elif cmd == "exchange":
        return "exchange [player] [card1] [optional, card2]"
    elif cmd in ["replace", "kill"]:
        return cmd + " [player] [card]"
    else:
        return "not found"

# game loop
while True:
    cmd_tokens = input("Enter command: ").lower().split()

    invalid_input = (len(cmd_tokens) < 1) or not command_verified(cmd_tokens, players)
    while invalid_input:
        if len(cmd_tokens) < 1:
            cmd_tokens = input("\nEmpty command entered, please try again.\nEnter command: ").lower().split()
        elif function_signature(cmd_tokens[0]) == "not found":
            cmd_tokens = input("\nCommand not found, please try again.\nEnter command: ").lower().split()
        else:
            print("\nIncorrect command arguments. Function signature of " + str(cmd_tokens[0]) + " is: ")
            print(function_signature(cmd_tokens[0]))
            print("\nCheck that you have initialized players, that the player and card names are matching \nand that number arguments can be converted to integers.\n")

            cmd_tokens = input("Enter command: ").lower().split()

        invalid_input = (len(cmd_tokens) < 1) or not command_verified(cmd_tokens, players)
 

    # call functions here, now that they're verified to be correct:
    cmd = cmd_tokens[0]
    if cmd == "help":
        help()
    elif cmd == "help_rules":
        help_rules()
    elif cmd == "help_actions":
        help_actions()
    elif cmd == "stats":
        stats()
    elif cmd == "stats_mod":
        stats_mod()
    elif cmd == "get_two":
        get_two()
    elif cmd == "init":
        init(cmd_tokens[1:])
    elif cmd == "add":
        add(players[cmd_tokens[1]], cmd_tokens[2])
    elif cmd == "remove":
        remove(players[cmd_tokens[1]], cmd_tokens[2])
    elif cmd == "exchange":
        if len(cmd_tokens) == 4:
            exchange(players[cmd_tokens[1]], cmd_tokens[2], cmd_tokens[3])
        elif len(cmd_tokens) == 3:
            exchange(players[cmd_tokens[1]], cmd_tokens[2])
    elif cmd == "replace":
        replace(players[cmd_tokens[1]], cmd_tokens[2])
    elif cmd == "kill":
        kill(players[cmd_tokens[1]], cmd_tokens[2])

