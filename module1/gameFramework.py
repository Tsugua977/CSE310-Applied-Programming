#Imports arcade library.
import arcade

#Constants
#Sets the screen width.
SCREEN_WIDTH = 400
#Sets the screen height.
SCREEN_LENGTH = 600
#Names the title of the screen.
SCREEN_TITLE = "Space Shooter"
#Predetermined scaling size to make sprites larger.
SCALING = 1.5
#Predetermined bullet speed.
BULLET_SPEED = 10

#Classes
class SpaceShooterGame (arcade.Window):
    #Built like Space Invaders.
    #Player's ship will be towards the bottom of the screen.
    #Player will be able to move left and right, but not up or down.

    def __init__(self, width, height, title):

        super().__init__(width, height, title)

        #Set the lists to be empty.
        self.player_list = None
        self.bullet_list = None
        self.enemy_list = None

    #Sets up the game.
    def setup(self):

        #Settng up the arcade lists.
        self.player_list = arcade.SpriteList()
        self.bullet_list = arcade.SpriteList()
        self.enemy_list = arcade.SpriteList()

        #Picks the color for the background of the screen.
        arcade.set_background_color(arcade.color.BLACK)

        #Sets up the player's sprite image.
        self.player = arcade.Sprite("module1/spaceship.png", SCALING)
        #Places player on screen with x and y coordinates.
        self.player.center_x = 200
        self.player.center_y = 50
        #Appends player to player list.
        self.player_list.append(self.player)

        #Sets up the enemy's sprite image.
        self.enemy = arcade.Sprite("module1/enemy.png")
        #Places enemy on screen with x and y coordinates.
        self.enemy.center_x = 200
        self.enemy.center_y = 550
        #Appends enemy to enemy list.
        self.enemy_list.append(self.enemy)

    #Class tells the program what keys are being pressed.
    def on_key_press(self, symbol, modifiers):

        #When Q is pressed, the game closes.
        if symbol == arcade.key.ESCAPE:
            arcade.close_window()

        #If the left arrow key is being pressed, the ship moves left.
        if symbol == arcade.key.LEFT:
            self.player.change_x = -5

        #If the right arrow key is being pressed, the ship moves right.
        if symbol == arcade.key.RIGHT:
            self.player.change_x = 5

        #When Z is pressed, a bullet is fired from the player.
        if symbol == arcade.key.Z:
            #Create the bullet by finding its image.
            bullet = arcade.Sprite("module1/bullet.png")

            #Sets the bullet's y speed to the predetermined value.
            bullet.change_y = BULLET_SPEED

            #Centers the bullet at the center x coordinate of the player.
            bullet.center_x = self.player.center_x

            #Places the bottom of the bullet at the top of the player.
            bullet.bottom = self.player.top

            #PAppends newly created bullet into the list.
            self.bullet_list.append(bullet)

    #Class tells the program what keys are being released.
    def on_key_release(self, symbol, modifiers):
        #If either the left or right arrow keys are not being pressed, the ship's speed goes to zero.
        if (
            symbol == arcade.key.LEFT
            or symbol== arcade.key.RIGHT
        ):
            self.player.change_x = 0

    #Updates the game so the objects ingame move.
    def on_update(self, delta_time):

        #Updates the player and bullet lists to move them.
        self.player_list.update()
        self.bullet_list.update()
        self.enemy_list.update()

        #If the player hits the left or right side of the screen,
        #this updates the player's ship to stay inside.
        if self.player.right > self.width:
            self.player.right = self.width
        if self.player.left < 0:
            self.player.left = 0

        #When the bottom of the bullet leaves the top of the screen, 
        #the bullet is removed from the bullet list.
        for bullet in self.bullet_list:
            if bullet.bottom > SCREEN_LENGTH:
                bullet.remove_from_sprite_lists()
            #If a bullet collides with an enemy, both the enemy
            #and the bullet are removed from the list.
            if bullet.collides_with_list(self.enemy_list):
                bullet.remove_from_sprite_lists()
                self.enemy.remove_from_sprite_lists()

    #Draws the game objects onto the screen.
    def on_draw(self):

        #Starts the rendering process.
        arcade.start_render()

        #Draws all the sprites in the lists.
        self.player_list.draw()
        self.bullet_list.draw()
        self.enemy_list.draw()

#Allows for the game to be run.
def main():
    window = SpaceShooterGame(SCREEN_WIDTH, SCREEN_LENGTH, SCREEN_TITLE)
    window.setup()
    arcade.run()

if __name__ == "__main__":
    main()