import arcade

SCREEN_WIDTH = 400
SCREEN_LENGTH = 600
SCREEN_TITLE = "Space Shooter"
SCALING = 1.5
BULLET_SPEED = 10

class SpaceShooterGame (arcade.Window):
    def __init__(self, width, height, title):

        super().__init__(width, height, title)

        self.player_list = None
        self.bullet_list = None
        self.enemy_list = None

    def setup(self):

        self.player_list = arcade.SpriteList()
        self.bullet_list = arcade.SpriteList()
        self.enemy_list = arcade.SpriteList()

        arcade.set_background_color(arcade.color.BLACK)

        self.player = arcade.Sprite("module1/spaceship.png", SCALING)
        self.player.center_x = 200
        self.player.center_y = 50
        self.player_list.append(self.player)

        self.enemy = arcade.Sprite("module1/enemy.png")
        self.enemy.center_x = 200
        self.enemy.center_y = 550
        self.enemy_list.append(self.enemy)

    def on_key_press(self, symbol, modifiers):

        if symbol == arcade.key.ESCAPE:
            arcade.close_window()

        if symbol == arcade.key.LEFT:
            self.player.change_x = -5

        if symbol == arcade.key.RIGHT:
            self.player.change_x = 5

        if symbol == arcade.key.Z:
            bullet = arcade.Sprite("module1/bullet.png")

            bullet.change_y = BULLET_SPEED

            bullet.center_x = self.player.center_x

            bullet.bottom = self.player.top

            self.bullet_list.append(bullet)

    def on_key_release(self, symbol, modifiers):
        if (
            symbol == arcade.key.LEFT
            or symbol== arcade.key.RIGHT
        ):
            self.player.change_x = 0

    def on_update(self, delta_time):

        self.player_list.update()
        self.bullet_list.update()
        self.enemy_list.update()

        if self.player.right > self.width:
            self.player.right = self.width
        if self.player.left < 0:
            self.player.left = 0

        for bullet in self.bullet_list:
            if bullet.bottom > SCREEN_LENGTH:
                bullet.remove_from_sprite_lists()
            if bullet.collides_with_list(self.enemy_list):
                bullet.remove_from_sprite_lists()
                self.enemy.remove_from_sprite_lists()

    def on_draw(self):

        arcade.start_render()
        self.player_list.draw()
        self.bullet_list.draw()
        self.enemy_list.draw()

def main():
    window = SpaceShooterGame(SCREEN_WIDTH, SCREEN_LENGTH, SCREEN_TITLE)
    window.setup()
    arcade.run()

if __name__ == "__main__":
    main()