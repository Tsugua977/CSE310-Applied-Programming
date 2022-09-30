#Imports arcade library.
import arcade

#Creates a screen for the game.
#Constants
SCREEN_WIDTH = 600
SCREEN_LENGTH = 800
SCREEN_TITLE = "Space Shooter"
SCALING = 2.0

#Classes
class SpaceShooterGame (arcade.Window):
    #Built like Space Invaders.
    #Player's ship will be towards the bottom of the screen.
    #Player will be able to move left and right, but not up or down.

    def __init__(self):

        super().__init__(SCREEN_WIDTH, SCREEN_LENGTH, SCREEN_TITLE)

        #Settng up the empty game Lists
        self.all_sprites = arcade.SpriteList()

    #Sets up the game.
    def setup(self):

        #Picks the color for the background of the screen.
        arcade.set_background_color(arcade.color.BLACK)

        #Sets up the player.
        self.player = arcade.Sprite("spaceship.png", SCALING)
        self.player.center_y = self.height / 2
        self.all_sprites.append(self.player)

    #Class tells the program what keys are being pressed.
    def pressing_key(self, symbol, modifiers):
        #If the left arrow key is being pressed, the ship moves left.
        if symbol == arcade.key.LEFT:
            self.player.change_x = -5

        #If the right arrow key is being pressed, the ship moves right.
        if symbol == arcade.key.RIGHT:
            self.player.change_x = 5

    #Class tells the program what keys are being released.
    def releasing_key(self, symbol: int, modifiers: int):
        #If either the left or right arrow keys are not being pressed, the ship's speed goes to zero.
        if (
            symbol == arcade.key.LEFT
            or symbol== arcade.key.RIGHT
        ):
            self.player.change_x = 0

    #Updates the game so the objects ingame move.
    def on_update(self):

        self.all_sprites.update()

        #If the player hits the left or right side of the screen,
        #this updates the player's ship to stay inside.
        if self.player.right > self.width:
            self.player.right = self.width
        if self.player.left < 0:
            self.player.left = 0

    #Draws the game objects onto the screen.
    def on_draw(self):
        arcade.start_render()
        self.all_sprites.draw()

#Allows for the game to be run.
def main():
    window = SpaceShooterGame()
    window.setup()
    arcade.run()

if __name__ == "__main__":
    main()