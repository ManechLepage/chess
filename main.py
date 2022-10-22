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

        self.fen_file = open("fens.txt", "r+")
        starting_fen = self.fen_file.readline()
        self.fen_file.close()
        self.generate_from_fen(starting_fen)
        print(self.save_position())

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
        #print(row_list)
        self.pieceList = []
        for i in range(len(row_list)):
            val = [*row_list[i]]
            #print(val)
            square_column = 0
            for j in range(len(val)):
                try:
                    int(val[j])
                    #print(val[j])
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
                        self.pieceList.append(piece)
                        square_column += 1

    def save_position(self):
        #TODO: Horizontal and not vertical FEN
        fen = []
        for x in self.grid:
            fen_row = []
            for y in x:
                space_counter = 0
                if not y.is_occupied:
                    space_counter += 1
                else:
                    if space_counter > 0:
                        fen_row.append(str(space_counter))
                    for piece in self.pieceList:
                        if (piece.x, piece.y) == (y.x, y.y):
                            i = piece
                    if i.__class__.__name__ == "Rook":
                        if y.is_dark:
                            fen_row.append("r")
                        else:
                            fen_row.append("R")
                    elif i.__class__.__name__ == "Pawn":
                        if i.is_dark:
                            fen_row.append("p")
                        else:
                            fen_row.append("P")
                    elif i.__class__.__name__ == "Knight":
                        if i.is_dark:
                            fen_row.append("n")
                        else:
                            fen_row.append("N")
                    elif i.__class__.__name__ == "Bishop":
                        if i.is_dark:
                            fen_row.append("b")
                        else:
                            fen_row.append("B")
                    elif i.__class__.__name__ == "King":
                        if i.is_dark:
                            fen_row.append("k")
                        else:
                            fen_row.append("K")
                    elif i.__class__.__name__ == "Queen":
                        if i.is_dark:
                            fen_row.append("q")
                        else:
                            fen_row.append("Q")
            fen.append(fen_row)
        return fen


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