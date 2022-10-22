import arcade
import classes
import colors

WIDTH = 800
HEIGHT = 600
SCREEN_TITLE = "Chess"

WIDTH_MARGIN = WIDTH / 16
HEIGHT_MARGIN = HEIGHT / 16

class MyGame(arcade.Window):

    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        arcade.set_background_color(colors.BACKGROUND_COLOR)

    def setup(self):
        self.create_grid()

    def create_grid(self):
        self.squareList = arcade.SpriteList()
        for x in range(8):
            for y in range(8):
                square = classes.Square("images/square.png")
                square.width = (WIDTH - WIDTH_MARGIN * 2) / 8
                square.height = (HEIGHT - HEIGHT_MARGIN * 2) / 8
                x_pos = (WIDTH_MARGIN + square.width / 2) + (square.width * x)
                y_pos = (HEIGHT_MARGIN + square.width / 2) + (square.height * y)
                square.x = x
                square.y = y
                square.set_position(x_pos, y_pos)
                if x % 2 == 0:
                    if y % 2 == 0:
                        square.is_dark = True
                else:
                    if y % 2 == 1:
                        square.is_dark = True
                square.update_color()

                self.squareList.append(square)

    def on_draw(self):
        self.clear()

        self.squareList.draw()

    def on_update(self, delta_time):
        pass

    def on_key_press(self, key, key_modifiers):
        pass

    def on_key_release(self, key, key_modifiers):
        pass

    def on_mouse_motion(self, x, y, delta_x, delta_y):
        pass

    def on_mouse_press(self, x, y, button, key_modifiers):
        pass

    def on_mouse_release(self, x, y, button, key_modifiers):
        pass


def main():
    game = MyGame(WIDTH, HEIGHT, SCREEN_TITLE)
    game.setup()
    arcade.run()


if __name__ == "__main__":
    main()