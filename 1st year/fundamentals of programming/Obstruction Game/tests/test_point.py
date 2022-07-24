import unittest
from domain.point import Point


class TestPoint(unittest.TestCase):

    def setUp(self) -> None:
        self._point = Point(3, 2)

    def tearDown(self) -> None:
        pass

    def test_getters(self):
        self.assertEqual(self._point.get_y(), 2)
        self.assertEqual(self._point.get_x(), 3)

    if __name__ == "__main__":
        unittest.main()
