import arcade
import colors

class Square(arcade.Sprite):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.x = 0
        self.y = 0
        self.is_dark = False

    def update_color(self):
        if self.is_dark:
            self.color = colors.DARK_SQUARE
        else:
            self.color = colors.LIGHT_SQUARE