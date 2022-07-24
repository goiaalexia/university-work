from src.repository.file_repository import *
from src.repository.binary_repository import *
import random
from src.domain.movie import *
from src.repository.repository import *

class MovieServices:

    def __init__(self, settings):
        if settings.repo_type == "inmemory":
            self._movie_repo = Repository()
        elif settings.repo_type == "file":
            self._movie_repo = FileRepository(settings.movies_file, Movie)
        elif settings.repo_type == "binary":
            self._movie_repo = BinaryRepository(settings.movies_file)
        #self.generate_random_movies()

    @property
    def movie_repo(self):
        return self._movie_repo

    def movie_setter(self, movie_index, movie):
        self._movie_repo[movie_index] = movie

    def get_movie_with_certain_id(self, movie_id):
        """
        the function that gets a movie with a certain ID
        :param movie_id: the movie's id
        :return: the movie we want to get
        """
        the_movie = 0
        for i in self._movie_repo:
            if i.id == movie_id:
                the_movie = i
        return the_movie

    def generate_random_movies(self):
        """
        the function that generates 20 random movies
        :return: None
        """
        movie_names = ["Outlander", "Guardians of the Galaxy Vol. 2", "Titanic", "Lord of the Rings", "Doctor Strange",
                       "Fifty Shades of Gray", "A Serbian Film", "Ouija 2", "Vertigo", "365 days", "Interstellar",
                       "Ender's Game", "The Social Dilemma", "The Big Short", "Nothing to Hide", "The Shack", "Crime & "
                                                                                                              "Prejudice",
                       "Miami Bici", "Toy Story 3", "Mad Max 3", "Men in Black", "Dune"]
        genre_names = ["action", "comedy", "sci-fi", "romance", "drama", "thriller", "horror"]
        for i in range(0, 20):
            c = Movie(i, random.choice(movie_names), f"Description {i}", random.choice(genre_names))
            movie_names.remove(c.title)
            self._movie_repo.add_item(c)

    def add_movie(self, movie):
        """
        the function that adds a movie to the movie repo
        :param movie: the movie to be added
        :return: None
        """
        can_we_add = True
        for i in self._movie_repo:
            if movie.id == getattr(i, "id"):  # the consequences of working with a list
                can_we_add = False
        if can_we_add is True:
            self._movie_repo.add_item(movie)
        else:
            raise RepoError("There is already a movie with that ID!")

    def update_movie(self, updated_movie):
        """
        the function that updates an existing movie
        :param updated_movie: the new information for the movie
        :return: None
        """
        did_we_update = False
        for i in range(0, len(self._movie_repo)):
            if getattr(self._movie_repo[i], "id") == updated_movie.id:
                self._movie_repo[i] = updated_movie
                did_we_update = True
        if did_we_update is False:
            raise ValueError("There is no movie with that ID to be updated!")

    def remove_movie(self, movie_to_be_removed_index):
        """
        the function that removes a certain movie from the repository
        :param movie_to_be_removed_index: the movie's id
        :return: None
        """
        did_we_remove = False
        list_thingy = []
        for i in self._movie_repo:
            if i.id == movie_to_be_removed_index:
                list_thingy.append(i)
                did_we_remove = True
        self._movie_repo.data = [x for x in self._movie_repo.data if x not in list_thingy]  # the consequences of lists
        if did_we_remove is False:
            raise ValueError("There is no movie with that ID to be removed!")

    def search_movies(self, search_term, which_field):
        """
        function that searches and returns a list of movies
        :param search_term: what to search by
        :param which_field: the field to search by
        :return: the list
        """
        returned_list = []
        search_term = search_term.strip()
        search_term = search_term.lower()
        which_field = which_field.strip()
        which_field = which_field.lower()
        if which_field == "id":
            search_term = int(search_term)  # TRY EXCEPT IN UI
            for i in self._movie_repo:
                if search_term == i.id:
                    returned_list.append(i)
        elif which_field == "title":
            for i in self._movie_repo:
                if search_term in i.title.lower():
                    returned_list.append(i)
        elif which_field == "description":
            for i in self._movie_repo:
                if search_term in i.description.lower():
                    returned_list.append(i)
        elif which_field == "genre":
            for i in self._movie_repo:
                if search_term in i.genre.lower():
                    returned_list.append(i)
        else:
            raise ValueError("Not a valid field!")
        if len(returned_list) > 0:
            return returned_list
        returned_list.append("The search returned no results!")
        return returned_list

    def __str__(self):
        s = f"\033[1;35;40mMovie repository:\033[0;0m\n\n"
        for i in self._movie_repo:
            s += f"{i}\n"
        return s
