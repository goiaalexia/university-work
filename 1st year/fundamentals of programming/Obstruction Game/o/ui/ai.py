import random
import copy


class AI:
    @staticmethod
    def get_input(b):
        winner = AI.get_win(b)
        if winner is not None:
            return winner
        moves = b.get_move_list()
        return random.choice(moves)

    @staticmethod
    def get_win(b):
        moves = b.get_move_list()
        for move in moves:
            board_copy = copy.deepcopy(b)
            board_copy.execute_move(move)
            if board_copy.available_moves == 0:
                return move

        return None
