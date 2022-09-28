#Imports arcade library.
from re import S
import arcade

#Creates a screen for the game.
#Constants
SCREEN_WIDTH = 600
SCREEN_LENGTH = 800
SCREEN_TITLE = "Space Shooter"
SCALING = 2.0

#Classes
class SpaceShooterGame (arcade.window):
    #Built like Space Invaders.
    #Player's ship will be towards the bottom of the screen.
    #Player will be able to move left and right, but not up or down.

    def __init__(self, width, height, title):

        super().__init__(width, height, title)

        #Settng up the empty game Lists
        self.all_sprites() = arcade.SpriteList()

    #Sets up the game.
    def setup():

        #Picks the color for the background of the screen.
        arcade.set_background_color(arcade.color.BLACK)

        #Sets up the player.
        self.player = arcade.Sprite()

        