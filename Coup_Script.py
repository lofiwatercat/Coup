

import random



# This is the script for the card game Coup

# Making a list of the character cards

char_deck = ['Duke', 'Duke', 'Duke', 'Assassin', 'Assassin', 'Assassin', 'Ambassador', 'Ambassador', 'Ambassador', 'Captain', 'Captain', 'Captain', 'Contessa', 'Contessa', 'Contessa']

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

    # method to add coins
    def add(self, number):
        self.coins = self.coins + number 

    # method to remove coins
    def remove(self, number):
        self.coins = self.coins - number

# making a list of the players
players = {}

# making an order of players
order_of_players = []

# BEGINNING MOD ACTIONS

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
        x.player_stats()

# shows the names of the players and their coins
def stats():
    for x in order_of_players:
        print()
        print(x.name)
        print(x.coins, 'coins')
        if len(x.revealed) != 0:
            print(x.revealed)

# initalizes the players
def init(*args):
    
    

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

# reveals a character card
def kill(Player, str):
    str = str.capitalize()
    for x in Player.cards:
        if x[0] == str and x[1] == 'hidden':
            x[1] = 'revealed'
            Player.revealed.append(x[0])

            
p1 = Player('Wilson')
players['Alan'] = Player('Alan')
players['Colin'] = Player('Colin')
order_of_players.append(p1)
stats()
kill(p1, 'Assassin')
stats()
stats_mod()
