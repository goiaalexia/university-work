from src.repository.binary_repository import *
from src.repository.file_repository import *
import random
from src.domain.rental import *
import datetime
import operator
from src.repository.repository import *

class RentalServices:

    def __init__(self, settings):
        if settings.repo_type == "inmemory":
            self._rental_repo = Repository()
        elif settings.repo_type == "file":
            self._rental_repo = FileRepository(settings.rental_file, Rental)
        elif settings.repo_type == "binary":
            self._rental_repo = BinaryRepository(settings.rental_file)
        #self.generate_random_rentals()

    @property
    def rental_repo(self):
        return self._rental_repo

    def generate_random_rentals(self):
        """
        the function that generates 20 random valid rentals
        :return: None
        """
        return_dates = [datetime.date(2021, 1, 3), datetime.date(2021, 9, 25), datetime.date(2021, 8, 17),
                        datetime.date(2021, 10, 30), datetime.date(2021, 1, 17), datetime.date(2021, 1, 14),
                        datetime.date(2021, 10, 17), datetime.date(2021, 11, 29), datetime.date.max]

        due_dates = [datetime.date(2021, 1, 3), datetime.date(2021, 9, 25), datetime.date(2021, 8, 17),
                     datetime.date(2021, 10, 30), datetime.date(2021, 1, 17), datetime.date(2021, 1, 14),
                     datetime.date(2021, 10, 17), datetime.date(2021, 11, 29)]

        rent_dates = [datetime.date(2020, 1, 3), datetime.date(2020, 9, 25), datetime.date(2020, 8, 17),
                      datetime.date(2020, 10, 30), datetime.date(2020, 1, 17), datetime.date(2020, 1, 14),
                      datetime.date(2020, 10, 17), datetime.date(2020, 11, 29)]
        for i in range(0, 20):
            movie = random.randint(0, 19)
            client = random.randint(0, 19)
            r = Rental(i, movie, client, random.choice(rent_dates), random.choice(due_dates),
                       random.choice(return_dates))
            self._rental_repo.add_item(r)

    def add_rental(self, rental):
        """
        the function that adds a rental to the rental repo
        :param rental: the rental to be added
        :return: None
        """
        for i in self._rental_repo:
            if i.id == rental.id:
                raise RepoError("There is already a rental with that ID!")  # identical ID case
            if i.returned_date == datetime.date.max and i.due_date < datetime.date.today() and rental.client_id == i.client_id:
                raise RepoError(
                    "That client has not returned their movies in time, therefore they can't rent another!")  # multiple rentals case
        self._rental_repo.add_item(rental)

    def return_rental(self, rental_id, return_date):
        """
        the function that returns a rental that hasn't been returned
        :param rental_id: the id of the rental to be returned
        :param return_date: the return date, which is today
        :return: None
        """
        can_it_be_returned = False
        to_be_returned = None
        for i in self._rental_repo:
            if rental_id == getattr(i, "id"):  # consequences of working with a list
                can_it_be_returned = True
                to_be_returned = i
        if can_it_be_returned is False:
            raise ValueError("There is no rental with that ID!")  # not found
        if self._rental_repo[to_be_returned].returned_date != datetime.date.max:
            raise RepoError("The movie has already been returned!")  # already returned case
        to_be_returned.returned_date = return_date

    def number_of_days_of_rental_i(self, i):
        """
        returns the number of rental days of a rental i
        :param i: rental
        :return:
        """
        if i.returned_date == datetime.date.max:  # not returned case
            delta = datetime.date.today() - i.rented_date
        else:
            delta = i.returned_date - i.rented_date
        return int(delta.days)

    def return_movie_id_rental_days_dict(self):
        """
        the function that creates a dictionary of the type MOVIE : NUMBER OF RENTAL DAYS
        :return: the dictionary, usage below
        """
        movie_rent_days = dict()
        for i in self.rental_repo:
            if i.movie_id not in movie_rent_days:
                movie_rent_days[i.movie_id] = self.number_of_days_of_rental_i(i)  # we create it
            else:
                movie_rent_days[i.movie_id] += self.number_of_days_of_rental_i(i)  # we add to it
        return movie_rent_days

    def most_rented_movies(self, movie_repo):
        """
        returns the most rented movies in a list
        :param movie_repo: the movie repository
        :return: the movie list, sorted in the order of the most rented ones
        """
        movie_dictionary = self.return_movie_id_rental_days_dict()
        sorted_dictionary = list(sorted(movie_dictionary.items(), key=operator.itemgetter(1), reverse=True))
        # SORTED DICTIONARY IN ORDER OF DAYS
        final_list = []
        for i in sorted_dictionary:
            for j in movie_repo:
                if i[0] == j.id:
                    final_list.append(j)
        return final_list

    def return_client_id_rental_days_dict(self):
        """
        the function that creates a dictionary of the type CLIENT : NUMBER OF RENTAL DAYS
        :return: the dictionary, usage below
        """
        client_rent_days = dict()
        for i in self.rental_repo:
            if i.client_id not in client_rent_days:
                client_rent_days[i.client_id] = self.number_of_days_of_rental_i(i)  # we create it
            else:
                client_rent_days[i.client_id] += self.number_of_days_of_rental_i(i)  # we add to it
        return client_rent_days

    def most_active_clients(self, client_repo):
        """
        returns the most active clients in a list
        :param client_repo: the client repository
        :return: the client list, sorted in the order of the most active ones
        """
        client_dictionary = self.return_client_id_rental_days_dict()
        sorted_dictionary = list(sorted(client_dictionary.items(), key=operator.itemgetter(1), reverse=True))
        # SORTED DICTIONARY IN ORDER OF DAYS
        final_list = []
        for i in sorted_dictionary:
            for j in client_repo:
                if i[0] == j.id:
                    final_list.append(j)
        return final_list

    def late_rentals(self, movie_repo):
        """
        the function that returns the list of movies in late rentals, if there are any at all
        :param movie_repo: the movie repository
        :return: the sorted list of movies in late rentals
        """
        day_count = dict()
        for i in self._rental_repo:
            if i.returned_date == datetime.date.max and datetime.date.today() > i.due_date:
                day_count[i.movie_id] = 0  # we create it
        for i in self._rental_repo:
            if i.returned_date == datetime.date.max and datetime.date.today() > i.due_date:
                day_count[i.movie_id] += int((datetime.date.today() - i.due_date).days)  # we add the days
        sorted_dictionary = list(sorted(day_count.items(), key=operator.itemgetter(1), reverse=True))
        sorted_movie_index_list = []
        for i in sorted_dictionary:
            sorted_movie_index_list.append(i[0])
        sorted_list = []
        for i in sorted_movie_index_list:
            sorted_list.append(movie_repo[i])
        if len(sorted_list) == 0:
            sorted_list.append("There are no late rentals!")  # no late rentals case
        return sorted_list

    def remove_certain_rentals_client(self, clienty_id):
        """
        the function that removes certain rentals that contain certain client
        :param clienty_id: the client's ID
        :return: None
        """
        rentals_to_be_removed = []
        for i in self.rental_repo:
            if i.client_id == clienty_id:  # consequences of using a list...
                rentals_to_be_removed.append(i)
        self.rental_repo.data = [x for x in self.rental_repo.data if x not in rentals_to_be_removed]

    def remove_certain_rentals_movie(self, movey_id):
        """
        the function that removes certain rentals that contain a certain movie
        :param movey_id: the movie's id
        :return: None
        """
        rentals_to_be_removed = []
        for i in self.rental_repo:
            if i.movie_id == movey_id:  # the consequences of using a list
                rentals_to_be_removed.append(i)
        self.rental_repo.data = [x for x in self.rental_repo.data if x not in rentals_to_be_removed]

    def remove_rental(self, rental_id):
        """
        the function that removes a rental with a certain ID, used for undo-redo
        :param rental_id: the rental's ID
        :return: None
        """
        did_we_remove = False
        the_rental = []
        for i in self._rental_repo:
            if i.id == rental_id:
                the_rental.append(i)
                did_we_remove = True
        self._rental_repo.data = [x for x in self._rental_repo.data if x not in the_rental]
        if did_we_remove is False:
            raise ValueError("There is no rental with that ID to be removed!")  # nothing to be removed case

    def remove_last_rental(self):
        """
        the function that removes the last rental from the list
        :return: None
        """
        index = len(self._rental_repo) - 1
        self._rental_repo.pop(index)

    def unreturn_rental(self, rental_id):
        """
        the function that "unreturns" a rental, used for undo-redo
        :param rental_id: the rental's ID
        :return: None
        """
        self._rental_repo[rental_id].returned_date = datetime.date.max

    def get_the_rentals_of_a_certain_client(self, client_id):
        """
        the function that gets all the rentals of a certain client
        :param client_id: the client's id
        :return: the list of rentals belonging to that client
        """
        rental_list = []
        for i in self.rental_repo:
            if i.client_id == client_id:
                rental_list.append(i)
        return rental_list

    def get_the_rentals_of_a_certain_movie(self, movie_id):
        """
        the function that gets all the rentals of a certain movie
        :param movie_id: the movie's id
        :return: the list of rentals containing that movie
        """
        rental_list = []
        for i in self.rental_repo:
            if i.movie_id == movie_id:
                rental_list.append(i)
        return rental_list

    def __str__(self):
        s = f"\033[1;35;40mRental repository:\033[0;0m\n\n"
        for i in self._rental_repo:
            s += f"{i}\n"
        return s
