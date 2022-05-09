import unittest
from src.services.client_services import ClientServices, Client
from src.repository.repository import *


class ClientTests(unittest.TestCase):
    def setUp(self) -> None:
        self._client_service = ClientServices()

    def tearDown(self) -> None:
        pass

    def test_client_init(self):
        self.assertEqual(len(self._client_service.client_repo), 20)

    def test_client_add(self):
        self._client_service.add_client(Client(22, "Ilie Daniel Rus"))
        self.assertEqual(len(self._client_service.client_repo), 21)
        with self.assertRaises(ValueError):
            self._client_service.add_client(Client("a", "a"))
        with self.assertRaises(ValueError):
            self._client_service.add_client(Client(21, 1))

    def test_remove_client(self):
        self._client_service.remove_client(0)
        self.assertEqual(len(self._client_service.client_repo), 19)

    def test_update_client(self):
        self._client_service.update_client(Client(10, "UPDATED NAME"))
        self.assertEqual(self._client_service.client_repo[10].name, "UPDATED NAME")

    def test_search_client(self):
        self.assertEqual(self._client_service.search_clients("10", "id        "),
                         [self._client_service.client_repo[10]])
        self._client_service._client_repo = Repository()
        self._client_service._client_repo.add_item(Client(0, "Monika"))
        self.assertEqual(self._client_service.search_clients("mo","name"), [self._client_service._client_repo[0]])
        with self.assertRaises(ValueError):
            self.assertEqual(self._client_service.search_clients("t", "e"), [self._client_service._client_repo[0]])
        self.assertEqual(self._client_service.search_clients("x","name"), ["The search returned no results!\n"])

    def test_str_client(self):
        client = Client(22, "Ilie Daniel Rus")
        self.assertEqual(str(client), "Client Ilie Daniel Rus with ID 22")

    def test_getter_client(self):
        self._client_service.add_client(Client(22, "Sia"))
        c = Client(22, "Sia")
        self.assertEqual(str(self._client_service.get_client_with_certain_id(22)), str(c))

    def test_str_client_repo(self):
        self._client_service._client_repo = Repository()
        self._client_service._client_repo.add_item(Client(0, "Pearl"))
        self.assertEqual(str(self._client_service._client_repo),
                         "<class 'src.domain.client.Client'> list:\n\nClient Pearl with ID 0\n")


if __name__ == '__main__':
    unittest.main()
