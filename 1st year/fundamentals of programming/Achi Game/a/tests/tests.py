import unittest
from domain.board import *
from ui.ai import *


class TestCases(unittest.TestCase):
    def SetUp(self) -> None:
        pass

    def TearDown(self) -> None:
        pass

    def test_game(self):
        board_lol = AIController()
        self.assertEqual(board_lol.winning_moving_move(), False)
        self.assertEqual(board_lol.get_board(), [['.', '.', '.'], ['.', '.', '.'], ['.', '.', '.']])
        board_lol.execute_move(0, 0)
        self.assertEqual(board_lol.get_board(), [['x', '.', '.'], ['.', '.', '.'], ['.', '.', '.']])
        with self.assertRaises(ValueError):
            board_lol.execute_move('a', 'a')
        g = board_lol.get_move_list()
        self.assertEqual(g, [[0, 1], [0, 2], [1, 0], [1, 1], [1, 2], [2, 0], [2, 1], [2, 2]])
        board_lol._board = [['x', 'x', 'O'], ['x', '.', 'O'], ['O', 'O', 'X']]
        board_lol.execute_a_moving_piece(1, 0)
        self.assertEqual(board_lol._board, [['x', 'x', 'O'], ['.', 'O', 'O'], ['O', 'O', 'X']])
        c = board_lol.get_available_moves_around_move(1, 1)
        self.assertEqual(c, [[0, 2], [2, 0]])
        self.assertEqual(board_lol.check_for_win(), True)
        board_lol.do_move()
