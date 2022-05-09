from domain.board import *
import random
import copy


class AIController(Board):
    def __init__(self):
        super().__init__()

    def block_user_win(self):
        """
        the function that checks whether the computer has to block the user's move
        :return: false if not
        """
        b = super().get_board()
        for i in range(0, 3):
            if b[i][0] == b[i][1] == 'x' and b[i][2] == '.':  # HORIZONTAL WINS
                super().execute_move(i, 2)
                return
            if b[i][1] == b[i][2] == 'x' and b[i][0] == '.':
                super().execute_move(i, 0)
                return
            if b[0][i] == b[1][i] == 'x' and b[2][i] == '.':
                super().execute_move(2, i)
                return
            if b[1][i] == b[2][i] == 'x' and b[0][i] == '.':  # VERTICAL WINS
                super().execute_move(0, i)
                return
        if b[0][0] == b[1][1] == 'x' and b[2][2] == '.':
            super().execute_move(2, 2)
            return
        if b[2][2] == b[1][1] == 'x' and b[0][0] == '.':
            super().execute_move(0, 0)  # MAIN DIAG
            return
        if b[2][0] == b[1][1] == 'x' and b[0][2] == '.':
            super().execute_move(0, 2)
            return
        if b[0][2] == b[1][1] == 'x' and b[2][0] == '.':
            super().execute_move(2, 0)  # SECOND DIAG
            return
        return False

    def winning_move(self):
        """
        the function that tries to see if there are any winning moves
        :return: false if not
        """
        b = super().get_board()
        for i in range(0, 3):
            if b[i][0] == b[i][1] == 'O' and b[i][2] == '.':  # HORIZONTAL WINS
                super().execute_move(i, 2)
                return
            if b[i][1] == b[i][2] == 'O' and b[i][0] == '.':
                super().execute_move(i, 0)
                return
            if b[0][i] == b[1][i] == 'O' and b[2][i] == '.':
                super().execute_move(2, i)
                return
            if b[1][i] == b[2][i] == 'O' and b[0][i] == '.':  # VERTICAL WINS
                super().execute_move(0, i)
                return
        if b[0][0] == b[1][1] == 'O' and b[2][2] == '.':
            super().execute_move(2, 2)
            return
        if b[2][2] == b[1][1] == 'O' and b[0][0] == '.':
            super().execute_move(0, 0)  # MAIN DIAG
            return
        if b[2][0] == b[1][1] == 'O' and b[0][2] == '.':
            super().execute_move(0, 2)
            return
        if b[0][2] == b[1][1] == 'O' and b[2][0] == '.':
            super().execute_move(2, 0)  # SECOND DIAG
            return
        return False

    def winning_moving_move(self):
        """
        the function that checks whether there can be done any winning moves MOVEMENT PHASE
        :return: False if not
        """
        g = super().get_move_list()
        x = super().get_available_moves_around_move(g[0][0], g[0][1])
        for i in x:
            board_copy = Board()
            board_copy._board = copy.deepcopy(self._board)  # GETTING THE NORMAL BOARD TO TEST SHIT ON
            try:
                board_copy.execute_a_moving_piece(x[0][0], x[0][1])
            except ValueError:
                continue
            if board_copy.check_for_win() is True:
                self.execute_a_moving_piece(x[0][0], x[0][1])
                return
        return False

    def do_move(self):
        """
        the function that does a move for the computer
        :return: none
        """
        if self.block_user_win() is False:
            if self.winning_move() is False:
                move = random.choice(super().get_move_list())
                super().execute_move(move[0], move[1])

    def do_moving_move(self):
        """
        the function that does a move for the computer MOVEMENT PHASE
        :return: none
        """
        if self.winning_moving_move() is False:
            x = super().get_move_list()
            move = random.choice(super().get_available_moves_around_move(x[0][0], x[0][1]))
            super().execute_a_moving_piece(move[0], move[1])


