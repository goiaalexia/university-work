class Board:
    def __init__(self):
        self._board = [['.', '.', '.'], ['.', '.', '.'], ['.', '.', '.']]
        self._turn = "human"
        self._piece_count = 4

    def __str__(self):
        s = ""
        for i in self._board:
            s += str(i)
            s += "\n"
        return s

    def get_move_list(self):
        l = []
        for i in range(0, 3):
            for j in range(0, 3):
                if self._board[i][j] == '.':
                    l.append([i, j])
        return l

    def get_board(self):
        return self._board

    def get_piece_count(self):
        return self._piece_count

    def get_turn(self):
        return self._turn

    def place_move(self, x, y):
        """
        the function that places a user's already validated move based on coordinates
        :param x: the x coord
        :param y: the y coord
        :return: None
        """
        if self._turn == "human":
            self._board[x][y] = 'x'
            self._turn = "computer"
        else:
            self._board[x][y] = 'O'
            self._turn = "human"

    def execute_move(self, x, y):
        """
        the function that executes a move, that is validating and actually making it
        :param x: the x coord of the move
        :param y: the y coord of the move
        :return: None
        """
        if self.validate_move(x, y) is True:  # if the move can be done as it's valid
            self.place_move(int(x), int(y))
            if self._turn == "human":  # get rid of those pieces, baby
                self._piece_count -= 1
        else:
            raise ValueError(self.validate_move(x, y))

    def validate_move(self, x, y):
        """
        move validator, depending on how much people screw up lmao
        :param x: the x coord of the move
        :param y: the y coord of the move
        :return: True if good move, reason if not
        """
        try:
            x = int(x)
            y = int(y)
        except ValueError:
            return "Not a number!"
        if x > 2 or y > 2 or x < 0 or y < 0:  # OUTSIDE BOARD
            return "Outside board!"
        if self._board[x][y] != '.':
            return "Already occupied!"
        return True

    def check_for_win(self):
        """
        the function that checks whether the win conditions are met.
        :return: False if the game hasn't been won
        """
        for i in self._board:
            if i[0] == i[1] == i[2] != '.':  # IF WE HAVE HORIZONTAL WIN
                return True
        for i in range(0, 3):
            if self._board[0][i] == self._board[1][i] == self._board[2][i] != '.':  # IF WE HAVE VERTICAL WIN
                return True
        if self._board[0][0] == self._board[1][1] == self._board[2][2] != '.':  # IF WE HAVE 1ST DIAG WIN
            return True
        if self._board[0][2] == self._board[1][1] == self._board[2][0] != '.':  # IF WE HAVE 2ND DIAG WIN
            return True
        return False

    def validate_moving_piece(self, x, y):
        """
        VALIDATES A MOVE IN THE MOVEMENT PHASE
        :param x: the x coordinate
        :param y: the y coordinate
        :return: True if the move can be made
        """
        try:
            x = int(x)
            y = int(y)
        except ValueError:
            return "Not a number!"
        if x > 2 or y > 2 or x < 0 or y < 0:  # OUTSIDE BOARD
            return "Outside board!"
        g = self.get_move_list()
        if g[0][0] == x and g[0][1] == y:
            return "There's no piece there!"
        if self._turn == "human":
            if self._board[x][y] == 'O':
                return "Invalid piece to be moved (not yours)!"
        else:  # lol
            pass
        if g[0][0] - 1 != x and g[0][0] + 1 != x and g[0][1] - 1 != y and g[0][1] + 1 != y:
            return "Invalid piece to be moved (too far)!"
        return True

    def move_piece_on_board(self, x, y):
        """
        function that moves a piece on the board MOVEMENT PHASE
        :param x: the x coord
        :param y: the y coord
        :return: None
        """
        g = self.get_move_list()
        if self._turn == "human":
            self._board[g[0][0]][g[0][1]] = 'x'  # TODO: THIS MAY NOT WORK
            self._turn = "computer"
        else:
            self._board[g[0][0]][g[0][1]] = 'O'
            self._turn = "human"
        self._board[int(x)][int(y)] = '.'

    def execute_a_moving_piece(self, x, y):
        """
        function that does a move in the movement phase with validator
        :param x: the coord x
        :param y: the coord y
        :return: raises valueerror if not good
        """
        if self.validate_moving_piece(x, y) is True:
            self.move_piece_on_board(x, y)
        else:
            raise ValueError(self.validate_moving_piece(x, y))

    def get_available_moves_around_move(self, x, y):
        """
        function that gets an available move around a certain move, for movement phase (USED BY THE AI)
        :param x: the x coord
        :param y: the y coord
        :return: list of available moves
        """
        listy = []
        for i in range(0, 3):
            for j in range(0, 3):
                if i != x and j != y:
                    if (i - 1 == x or j - 1 == y or i + 1 == x or j - 1 == y) and self._board[i][j] == 'O':  # IF NEARBY
                        listy.append([i, j])
        return listy


if __name__ == "__main__":
    b = Board()
    g = b.get_move_list()
    print(g)
