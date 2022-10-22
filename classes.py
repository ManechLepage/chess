import arcade
import colors

class Square(arcade.Sprite):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.x = 0
        self.y = 0
        self.is_dark = False
        self.is_occupied = False

    def update_color(self):
        if self.is_dark:
            self.color = colors.DARK_SQUARE
        else:
            self.color = colors.LIGHT_SQUARE

class Piece(arcade.Sprite):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.is_dark = False
        self.x = 0
        self.y = 0

    def update_color(self):
        if self.is_dark:
            self.color = colors.DARK_PIECE
        else:
            self.color = colors.LIGHT_PIECE

class Pawn(Piece):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

class Rook(Piece):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

class Knight(Piece):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

class Bishop(Piece):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

class King(Piece):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

class Queen(Piece):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)