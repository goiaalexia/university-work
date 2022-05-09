import unittest
from src.domain.client import Client
from src.repository.repository import *


class ClientTests(unittest.TestCase):
    def setUp(self) -> None:
        self._repository = Repository()

    def tearDown(self) -> None:
        pass

    def test_repository_delete(self):
        self._repository.add_item(1)
        del self._repository[0]

    def test_repository_len(self):
        self.assertEqual(len(self._repository),0)

    def test_repository_pop(self):
        self._repository.add_item(1)
        self._repository.pop(0)

    def test_repository_str(self):
        self._repository.add_item("1")
        self.assertEqual(str(self._repository), "<class 'str'> list:\n\n1\n")

    def test_repository_add(self):
        c = Client(0,"Theresa")
        self._repository.add_item(c)
        with self.assertRaises(RepoError):
            self._repository.add_item(c)
