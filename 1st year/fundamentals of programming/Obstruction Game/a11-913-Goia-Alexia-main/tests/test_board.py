import unittest
from domain.board import Board, MoveError
from domain.point import Point


class TestBoard(unittest.TestCase):

    def setUp(self) -> None:
        self._board = Board(4, 3)

    def tearDown(self) -> None:
        pass

    def test_getters_and_setters(self):
        self._board.set_rows(10)
        self.assertEqual(self._board.get_rows(), 10)
        self._board.set_columns(8)
        self.assertEqual(self._board.get_columns(), 8)
        self.assertEqual(self._board.get_board(), [])

    def test_create_board(self):
        self._board.create_board()
        self.assertEqual(str(self._board),
                         "\nx\n0 ['.', '.', '.']\n1 ['.', '.', '.']\n2 ['.', '.', '.']\n3 ['.', '.', '.']\n    0    1    2    y")
        turn = self._board.get_turn()
        self.assertEqual(turn, "first")

    def test_moves(self):
        self._board.create_board()
        self.assertEqual(self._board.available_moves(), 12)
        self._board.execute_move(Point(1, 1))
        self._board.execute_move(Point(3, 1))
        self.assertEqual(str(self._board),
                         "\nx\n0 ['*', '*', '*']\n1 ['*', 'X', '*']\n2 ['*', '*', '*']\n3 ['*', 'O', '*']\n    0    1    2    y")
        with self.assertRaises(MoveError):
            self._board.execute_move(Point("a", 1))
        with self.assertRaises(MoveError):
            self._board.execute_move(Point(1, 1))
        with self.assertRaises(MoveError):
            self._board.execute_move(Point(7, 7))
        self.assertEqual(self._board.available_moves(), 0)

    if __name__ == "__main__":
        unittest.main()
