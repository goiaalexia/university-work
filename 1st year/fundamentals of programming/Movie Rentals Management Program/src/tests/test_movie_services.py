import unittest
from src.services.movie_services import MovieServices, Movie
from src.repository.repository import *
from src.services.undo_services import *

class MovieTests(unittest.TestCase):
    def setUp(self) -> None:
        self._movie_service = MovieServices()
        self._undo_service = UndoServices()

    def tearDown(self) -> None:
        pass

    def test_movie_init(self):
        self.assertEqual(len(self._movie_service.movie_repo), 20)

    def test_movie_add(self):
        self._movie_service.add_movie(Movie(22, "The Movie", "DESCRIPTION", "GENRE"))
        self.assertEqual(self._movie_service.movie_repo[20].description, "DESCRIPTION")
        self.assertEqual(self._movie_service.movie_repo[20].genre, "GENRE")
        self.assertEqual(len(self._movie_service.movie_repo), 21)
        with self.assertRaises(ValueError):
            self._movie_service.add_movie(Movie(22, 2, "DESCRIPTION", "GENRE"))
        with self.assertRaises(ValueError):
            self._movie_service.add_movie(Movie(22, "The Movie", 2, "GENRE"))
        with self.assertRaises(ValueError):
            self._movie_service.add_movie(Movie(22, "The Movie", "DESCRIPTION", 2))
        with self.assertRaises(ValueError):
            self._movie_service.add_movie(Movie("a", "The Movie", "DESCRIPTION", "GENRE"))

    def test_remove_movie(self):
        self._movie_service.remove_movie(0)
        self.assertEqual(len(self._movie_service.movie_repo), 19)

    def test_update_client(self):
        self._movie_service.update_movie(Movie(10, "The Movie", "DESCRIPTION", "GENRE"))
        self.assertEqual(self._movie_service.movie_repo[10].title, "The Movie")

    def test_search_movie(self):
        self.assertEqual(self._movie_service.search_movies("10", "id        "),
                         [self._movie_service.movie_repo[10]])
        self._movie_service._movie_repo = Repository()
        self._movie_service._movie_repo.add_item(Movie(0,"Title","Description","Genre"))
        self.assertEqual(self._movie_service.search_movies("ge", "genre"), [self._movie_service._movie_repo[0]])
        self.assertEqual(self._movie_service.search_movies("t", "title"), [self._movie_service._movie_repo[0]])
        self.assertEqual(self._movie_service.search_movies("desc", "description"), [self._movie_service._movie_repo[0]])
        with self.assertRaises(ValueError):
            self.assertEqual(self._movie_service.search_movies("ge", "gx"), [self._movie_service._movie_repo[0]])
        self.assertEqual(self._movie_service.search_movies("x", "genre"), ["The search returned no results!"])


    def test_str_movie(self):
        movie = Movie(22, "The Movie", "DESCRIPTION", "GENRE")
        self.assertEqual(str(movie), "The movie The Movie with ID 22 in the GENRE genre: DESCRIPTION")

    def test_add_movie(self):
        m = Movie(21, "aaaaaa", "a", "a")
        self._movie_service.add_movie(m)
        with self.assertRaises(RepoError):
            self._movie_service.add_movie(m)
        undo = Call(self._movie_service.remove_movie, 21)
        redo = Call(self._movie_service.add_movie, m)
        op = Operation(undo, redo)
        cascaded_op = CascadedOperation()
        cascaded_op.add(op)
        self._undo_service.record(cascaded_op)
        self.assertEqual(self._undo_service._history, [cascaded_op])
        cascaded_op.undo()
        cascaded_op.redo()

    def test_movie_getter(self):
        m = 19
        self.assertEqual(self._movie_service.get_movie_with_certain_id(m),self._movie_service.movie_repo[19])



if __name__ == '__main__':
    unittest.main()
