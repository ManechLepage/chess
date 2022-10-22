import arcade
import classes
import colors

WIDTH = 800
HEIGHT = 800
SCREEN_TITLE = "Chess"

WIDTH_MARGIN = WIDTH / 16
HEIGHT_MARGIN = HEIGHT / 16
PIECE_MARGIN = 10

class MyGame(arcade.Window):

    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        arcade.set_background_color(colors.BACKGROUND_COLOR)

    def setup(self):
        self.create_grid()
        self.create_pieces()

        self.generate_from_fen("rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR")

    def create_grid(self):
        self.squareList = arcade.SpriteList()
        self.grid = []
        for x in range(8):
            row = []
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
                row.append(square)
            self.grid.append(row)

    def create_pieces(self):
        self.white_pieces = arcade.SpriteList()
        self.black_pieces = arcade.SpriteList()

    def generate_from_fen(self, fen):
        row_list = fen.split("/")
        print(row_list)
        for i in range(len(row_list)):
            val = [*row_list[i]]
            print(val)
            square_column = 0
            for j in range(len(val)):
                try:
                    int(val[j])
                    print(val[j])
                    square_column += val[j]
                except:
                    isPiece = True
                    if val[j] == "p" or val[j] == "P":
                        piece = classes.Pawn("images/pieces/pawn.png")
                    elif val[j] == "r" or val[j] == "R":
                        piece = classes.Rook("images/pieces/rook.png")
                    elif val[j] == "b" or val[j] == "B":
                        piece = classes.Bishop("images/pieces/bishop.png")
                    elif val[j] == "n" or val[j] == "N":
                        piece = classes.Knight("images/pieces/knight.png")
                    elif val[j] == "q" or val[j] == "Q":
                        piece = classes.Queen("images/pieces/queen.png")
                    elif val[j] == "k" or val[j] == "K":
                        piece = classes.King("images/pieces/king.png")
                    else:
                        isPiece = False
                    if isPiece:
                        if val[j].islower():
                            self.black_pieces.append(piece)
                            piece.is_dark = True
                        else:
                            self.white_pieces.append(piece)

                        piece.x = square_column
                        piece.y = i
                        piece.set_position(self.grid[piece.x][piece.y].center_x, self.grid[piece.x][piece.y].center_y)
                        piece.update_color()
                        piece.width = ((WIDTH - WIDTH_MARGIN * 2) / 8) - PIECE_MARGIN
                        piece.height = ((HEIGHT - HEIGHT_MARGIN * 2) / 8) - PIECE_MARGIN
                        self.grid[piece.x][piece.y].is_occupied = True
                        square_column += 1



    def on_draw(self):
        self.clear()

        self.squareList.draw()
        self.white_pieces.draw()
        self.black_pieces.draw()

    def on_update(self, delta_time):
        self.white_pieces.update()
        self.black_pieces.update()

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