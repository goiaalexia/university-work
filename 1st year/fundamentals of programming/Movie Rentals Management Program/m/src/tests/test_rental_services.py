import unittest
import datetime
from src.services.movie_services import MovieServices, Movie
from src.services.client_services import ClientServices, Client
from src.services.rental_services import RentalServices, Rental
from src.services.undo_services import *
from src.repository.repository import *


class RentalTests(unittest.TestCase):
    def setUp(self) -> None:
        self._movie_service = MovieServices()
        self._client_service = ClientServices()
        self._rental_service = RentalServices()
        self._undo_service = UndoServices()

    def tearDown(self) -> None:
        pass

    def test_rental_init(self):
        self.assertEqual(len(self._rental_service.rental_repo), 20)

    def test_rental_add(self):
        self._rental_service.add_rental(
            Rental(20, 1, 18, datetime.date(2003, 1, 25), datetime.date(2003, 1, 30), datetime.date(2003, 1, 27)))
        with self.assertRaises(ValueError):
            self._rental_service.add_rental(
                Rental("a", 1, 18, datetime.date(2003, 1, 25), datetime.date(2003, 1, 30), datetime.date(2003, 1, 27)))
        with self.assertRaises(ValueError):
            self._rental_service.add_rental(
                Rental(20, "a", 18, datetime.date(2003, 1, 25), datetime.date(2003, 1, 30), datetime.date(2003, 1, 27)))
        with self.assertRaises(ValueError):
            self._rental_service.add_rental(
                Rental(20, 1, "a", datetime.date(2003, 1, 25), datetime.date(2003, 1, 30), datetime.date(2003, 1, 27)))
        with self.assertRaises(ValueError):
            self._rental_service.add_rental(
                Rental(20, 1, 18, "a", datetime.date(2003, 1, 30), datetime.date(2003, 1, 27)))
        with self.assertRaises(ValueError):
            self._rental_service.add_rental(
                Rental(20, 1, 18, datetime.date(2003, 1, 25), 2, datetime.date(2003, 1, 27)))
        with self.assertRaises(ValueError):
            self._rental_service.add_rental(
                Rental(20, 1, 18, datetime.date(2003, 1, 25), datetime.date(2003, 1, 30), 3))
        self._rental_service.add_rental(
            Rental(22, 1, 18, datetime.date(2003, 1, 25), datetime.date(2003, 1, 30), "not returned"))
        self.assertEqual(len(self._rental_service.rental_repo), 22)

    def test_rental_getters(self):
        self._rental_service.add_rental(
            Rental(20, 1, 18, datetime.date(2003, 1, 25), datetime.date(2003, 1, 30), datetime.date(2003, 1, 27)))
        self.assertEqual(self._rental_service.rental_repo[20].id, 20)
        self.assertEqual(self._rental_service.rental_repo[20].client_id, 18)
        self.assertEqual(self._rental_service.rental_repo[20].movie_id, 1)
        self.assertEqual(self._rental_service.rental_repo[20].rented_date, datetime.date(2003, 1, 25))
        self.assertEqual(self._rental_service.rental_repo[20].due_date, datetime.date(2003, 1, 30))
        self.assertEqual(self._rental_service.rental_repo[20].returned_date, datetime.date(2003, 1, 27))

    def test_rental_setters(self):
        self._rental_service.add_rental(
            Rental(20, 1, 18, datetime.date(2003, 1, 25), datetime.date(2003, 1, 30), datetime.date(2003, 1, 27)))
        self._rental_service.rental_repo[20].movie_id = 1
        self._rental_service.rental_repo[20].client_id = 18
        self._rental_service.rental_repo[20].due_date = datetime.date(2003, 1, 30)
        self._rental_service.rental_repo[20].rented_date = datetime.date(2003, 1, 25)
        self._rental_service.rental_repo[20].returned_date = datetime.date(2003, 1, 27)
        with self.assertRaises(ValueError):
            self._rental_service.rental_repo[20].rented_date = datetime.date(2003, 2, 26)
        with self.assertRaises(ValueError):
            self._rental_service.rental_repo[20].returned_date = datetime.date(2003, 1, 24)
        with self.assertRaises(ValueError):
            self._rental_service.rental_repo[20].due_date = datetime.date(2003, 1, 24)

    def test_rental_str(self):
        r = Rental(20, 1, 18, datetime.date(2003, 1, 25), datetime.date(2003, 1, 30), datetime.date(2003, 1, 27))
        self.assertEqual(str(r),
                         "Rental with ID 20 of the movie with ID 1 belonging to client 18\nRent date: 2003-01-25\nDue "
                         "date: 2003-01-30\nReturned date: 2003-01-27")
        r = Rental(20, 1, 18, datetime.date(2003, 1, 25), datetime.date(2003, 1, 30), datetime.date.max)
        self.assertEqual(str(r),
                         "Rental with ID 20 of the movie with ID 1 belonging to client 18\nRent date: 2003-01-25\nDue "
                         "date: 2003-01-30\nReturned date: NOT RETURNED! (DUE DATE PASSED)")
        r = Rental(20, 1, 18, datetime.date(2020, 1, 25), datetime.date(2022, 1, 30), datetime.date.max)
        self.assertEqual(str(r),
                         "Rental with ID 20 of the movie with ID 1 belonging to client 18\nRent date: 2020-01-25\nDue "
                         "date: 2022-01-30\nReturned date: NOT RETURNED!")

    def test_add_rental(self):
        r = Rental(20, 1, 18, datetime.date(2003, 1, 25), datetime.date(2003, 1, 30), datetime.date(2003, 1, 27))
        self._rental_service.add_rental(r)
        with self.assertRaises(RepoError):
            self._rental_service.add_rental(r)
        r = Rental(21, 1, 18, datetime.date(2003, 1, 25), datetime.date(2003, 1, 30), datetime.date.max)
        self._rental_service.add_rental(r)
        with self.assertRaises(RepoError):
            self._rental_service.add_rental(r)

    def test_return_undo_redo_rental(self):
        r = Rental(20, 1, 18, datetime.date(2003, 1, 25), datetime.date(2003, 1, 30), datetime.date.max)
        self._rental_service.add_rental(r)
        thing = datetime.date.today()
        self._rental_service.return_rental(20, thing)
        self.assertEqual(r.returned_date, thing)
        undo = Call(self._rental_service.unreturn_rental, 20)
        redo = Call(self._rental_service.return_rental, 20, thing)
        op = Operation(undo, redo)
        self._undo_service.record(op)
        self._undo_service.undo()
        self.assertEqual(r.returned_date, datetime.date.max)
        self._undo_service.redo()
        self.assertEqual(r.returned_date, thing)

    def test_statistics_rental(self):
        self._rental_service._rental_repo = [
            Rental(0, 0, 0, datetime.date(2003, 1, 25), datetime.date(2003, 1, 30), datetime.date.max)]
        self._movie_service._movie_repo = [Movie(0, "aaaaaa", "a", "a")]
        self._client_service._client_repo = [Client(0, "Jjjjjj")]
        a = str(self._rental_service.most_rented_movies(self._movie_service.movie_repo)[0])
        b = str(Movie(0, "aaaaaa", "a", "a"))
        self.assertEqual(a, b)
        a = str(self._rental_service.most_active_clients(self._client_service.client_repo)[0])
        b = str(Client(0, "Jjjjjj"))
        self.assertEqual(a, b)
        a = str(self._rental_service.late_rentals(self._movie_service._movie_repo)[0])
        b = str(Movie(0, "aaaaaa", "a", "a"))
        self.assertEqual(a, b)

    def test_remove_rentals(self):
        self._rental_service._rental_repo = Repository()
        self._rental_service._rental_repo.add_item(
            Rental(0, 0, 0, datetime.date(2003, 1, 25), datetime.date(2003, 1, 30), datetime.date.max))
        self._rental_service._rental_repo.add_item(
            Rental(1, 1, 0, datetime.date(2003, 1, 25), datetime.date(2003, 1, 30), datetime.date.max))
        self._movie_service._movie_repo = [Movie(0, "Title", "Description", "Genre"), Movie(1, "aaa", "aaaa", "aaaa")]
        self._client_service._client_repo = [Client(0, "Adela Popescu")]
        self._rental_service.remove_certain_rentals_client(0)
        self.assertEqual(len(self._rental_service._rental_repo), 0)
        self._rental_service._rental_repo.add_item(
            Rental(0, 0, 0, datetime.date(2003, 1, 25), datetime.date(2003, 1, 30), datetime.date.max))
        self._rental_service._rental_repo.add_item(
            Rental(1, 1, 0, datetime.date(2003, 1, 25), datetime.date(2003, 1, 30), datetime.date.max))
        self._rental_service.remove_certain_rentals_movie(1)
        self.assertEqual(len(self._rental_service._rental_repo), 1)
        self._rental_service.remove_rental(0)
        self.assertEqual(len(self._rental_service._rental_repo), 0)

    def test_getter_rentals(self):
        self._rental_service._rental_repo = Repository()
        self._movie_service._movie_repo = [Movie(0, "Title", "Description", "Genre"), Movie(1, "aaa", "aaaa", "aaaa")]
        self._client_service._client_repo = [Client(0, "Avicii"), Client(1, "Steve Aoki")]
        self.assertEqual(self._rental_service.get_the_rentals_of_a_certain_movie(0), [])
        self.assertEqual(self._rental_service.get_the_rentals_of_a_certain_client(0), [])
        self._rental_service.add_rental(
            Rental(1, 1, 0, datetime.date(2003, 1, 25), datetime.date(2003, 1, 30), datetime.date.max))
        self.assertEqual(self._rental_service.get_the_rentals_of_a_certain_movie(0), [])
        self.assertEqual(self._rental_service.get_the_rentals_of_a_certain_client(1), [])

    def test_str_rentals(self):
        self._rental_service._rental_repo = Repository()
        self._rental_service._rental_repo.add_item(
            Rental(1, 1, 0, datetime.date(2003, 1, 25), datetime.date(2003, 1, 30), datetime.date.max))
        self.assertEqual(str(self._rental_service.rental_repo),
                         "<class 'src.domain.rental.Rental'> list:\n\nRental with ID 1 of the movie with ID 1 belonging to client 0\nRent date: 2003-01-25\nDue date: 2003-01-30\nReturned date: NOT RETURNED! (DUE DATE PASSED)\n")


if __name__ == '__main__':
    unittest.main()
