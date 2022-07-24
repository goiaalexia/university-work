from domain.point import Point


class MoveError(Exception):
    pass


class Board:
    def __init__(self, rows, columns):
        self.__rows = rows
        self.__columns = columns
        self.__board = []
        self._turn = "first"

    def get_turn(self):
        return self._turn

    def get_rows(self):
        return self.__rows

    def get_columns(self):
        return self.__columns

    def get_board(self):
        return self.__board

    def set_columns(self, columns):
        self.__columns = columns

    def set_rows(self, rows):
        self.__rows = rows

    def set_turn(self, turn):
        self._turn = turn

    def set_move(self, point):
        x = point.get_x()
        y = point.get_y()
        if self._turn == "first":
            self.__board[x][y] = 'X'
            self.set_turn("second")
        else:
            self.__board[x][y] = 'O'
            self.set_turn("first")

    def available_moves(self):
        """
        the function that returns the amount of available moves to be made on the board
        :return: available_move_counter -> number of available moves
        """
        available_move_counter = 0
        rows = self.get_rows()
        columns = self.get_columns()
        for row in range(rows):
            for column in range(columns):
                if self.__board[row][column] == '.':
                    available_move_counter += 1
        return available_move_counter

    def execute_move(self, point):
        """
        the function that executes a move on the board
        :param point: the move to be executed, represented by its coordinates
        :return: None
        """
        self.validate_move(point)  # might raise a MoveError if the move is not valid
        self.set_move(point)
        self.mark_borders_of_move(point)

    def create_board(self):
        """
        the function that creates the beginning board
        :return: None
        """
        for row in range(self.get_rows()):
            work_list = []
            for column in range(self.get_columns()):
                work_list.append('.')
            self.__board.append(work_list)

    def potential_move_is_valid(self, point):
        """
        function that checks whether a potential move is valid
        :param point: the move
        :return: boolean value depending on the truth value of the validity
        """
        x = int(point.get_x())
        y = int(point.get_y())
        if x > self.get_rows() - 1 or x < 0 or y > self.get_columns() - 1 or y < 0:
            return False
        if self.__board[x][y] != '.':
            return False
        return True


    def validate_move(self, point):
        """
        function that validates a move to be made
        :param point: the point where the move is intended to be done
        :return: None
        """
        try:
            x = int(point.get_x())
            y = int(point.get_y())
        except ValueError:
            raise MoveError("Not a valid move! (move coordinates should be integers, dude)")
        if x > self.get_rows() - 1 or x < 0 or y > self.get_columns() - 1 or y < 0:
            raise MoveError("Not a valid move! (outside the board)")
        if self.__board[x][y] != '.':
            raise MoveError("Not a valid move! (too close to another point)")

    def get_move_list(self):
        """
        function that gets the list of available moves
        :return: list of moves
        """
        m = []
        rows = self.get_rows()
        columns = self.get_columns()
        for row in range(rows):
            for column in range(columns):
                if self.__board[row][column] == '.':
                    m.append(Point(row, column))
        return m

    def mark_borders_of_move(self, point):
        """
        function that marks all the bordering squares of an already placed move
        :param point: the point where the move has been done
        :return: None
        """
        x = point.get_x()
        y = point.get_y()
        if x - 1 >= 0 and y - 1 >= 0 and self.__board[x - 1][y - 1] == '.':  # upper left corner
            self.__board[x - 1][y - 1] = '*'
        if x - 1 >= 0 and self.__board[x - 1][y] == '.':  # directly above the move
            self.__board[x - 1][y] = '*'
        if x - 1 >= 0 and y + 1 < self.get_columns() and self.__board[x - 1][y + 1] == '.':  # upper right corner
            self.__board[x - 1][y + 1] = '*'
        if y - 1 >= 0 and self.__board[x][y - 1] == '.':  # directly to the left of the move
            self.__board[x][y - 1] = '*'
        if y + 1 < self.get_columns() and self.__board[x][y + 1] == '.':  # directly to the right of the move
            self.__board[x][y + 1] = '*'
        if x + 1 < self.get_rows() and y - 1 >= 0 and self.__board[x + 1][y - 1] == '.':  # lower left corner
            self.__board[x + 1][y - 1] = '*'
        if x + 1 < self.get_rows() and self.__board[x + 1][y] == '.':  # directly under the move
            self.__board[x + 1][y] = '*'
        if x + 1 < self.get_rows() and y + 1 < self.get_columns() and self.__board[x + 1][y + 1] \
                == '.':  # lower right corner (AHH WHY IS IT ON 2 ROWS YEX)
            self.__board[x + 1][y + 1] = '*'

    def __str__(self):
        """
        overriding the initial str to show a beautiful board <3
        :return: the string xD
        """
        s = "\nx\n"
        row = 0
        for element in self.__board:
            s += f"{row} {element}\n"
            row += 1
        row = self.__board[0]
        s += "  "
        for column in range(0, len(row)):
            s += f"  {column}  "
        s += "  y"
        return s


if __name__ == "__main__":
    pass
