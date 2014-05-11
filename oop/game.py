import core
import pyglet
from pyglet.window import key
from core import GameElement
import sys

#### DO NOT TOUCH ####
GAME_BOARD = None
DEBUG = False
KEYBOARD = None
PLAYER = None
######################

GAME_WIDTH = 6
GAME_HEIGHT = 5

#### Put class definitions here ####
class Rock(GameElement):
    IMAGE = "Rock"
    SOLID = True

class Character(GameElement):
    IMAGE = "Cat"

    def __init__(self):
        GameElement.__init__(self)
        self.inventory = []

    # This tells me the direction coordinates or None
    # @param String up|down|left|right
    # @return Tuple|None
    def next_pos(self, direction):
        if direction == "up":
            return (self.x, self.y-1)
        elif direction == "down":
            return (self.x, self.y+1)
        elif direction == "left":
            return (self.x-1, self.y)
        elif direction == "right":
            return (self.x+1, self.y)
        return None

class Gem(GameElement):
    IMAGE = "BlueGem"
    SOLID = False
    def interact(self, player):
        player.inventory.append(self)
        GAME_BOARD.draw_msg("You just acquired a gem! You have %d items!"%(len(player.inventory)))

####   End class definitions    ####


def initialize():
    """Put game initialization code here"""
    # To create multiple rocks, use a list for the positions and an empty list for the rocks. 
    # Use tuples for the rock positions. 
    # Then loop through the rock positions to initialize and register each rock, appending the rock to the rocks list as you go.

    rock_positions = [(2, 1), (1,2), (3,1), (2,3), (3,3), (4,2)]
    rocks = []
    for position in rock_positions:
        rock = Rock()
        GAME_BOARD.register(rock)
        GAME_BOARD.set_el(position[0], position[1], rock)
        rocks.append(rock)
    for rock in rocks:
        print rock

    #make the last rock in the rocks list not solid
    rocks[-1].SOLID = False

    #Initialize and register the Character
    global PLAYER
    PLAYER = Character()
    GAME_BOARD.register(PLAYER)
    GAME_BOARD.set_el(2,2, PLAYER)
    print PLAYER

    #Add the ability to display a message
    GAME_BOARD.draw_msg("Welcome to my first game.")

    #Add Gem
    gem = Gem()
    GAME_BOARD.register(gem)
    GAME_BOARD.set_el(5,4,gem)

    

def keyboard_handler():
    # Set direction to None to begin. Engine checks every 10th of a second to see if the keyboard state has changed
    direction = None
    if KEYBOARD[key.UP]:
        direction = "up"
    if KEYBOARD[key.DOWN]:
        direction = "down"
    if KEYBOARD[key.LEFT]:
        direction = "left"
    if KEYBOARD[key.RIGHT]:
        direction = "right"

    if direction:
        next_location = PLAYER.next_pos(direction)
        next_x = next_location[0]
        next_y = next_location[1]

        existing_el = GAME_BOARD.get_el(next_x, next_y)
        if existing_el:
            existing_el.interact(PLAYER)

        if existing_el is None or not existing_el.SOLID:
            GAME_BOARD.del_el(PLAYER.x, PLAYER.y)
            GAME_BOARD.set_el(next_x, next_y, PLAYER)





