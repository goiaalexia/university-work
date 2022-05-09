import datetime

class Rental:
    def __init__(self, rental_id, movie_id, client_id, rented_date, due_date, returned_date):
        if not isinstance(rental_id, int):
            raise ValueError("Invalid rental ID type!")
        if not isinstance(movie_id, int):
            raise ValueError("Invalid movie ID type!")
        if not isinstance(client_id, int):
            raise ValueError("Invalid client ID type!")
        if not isinstance(rented_date, datetime.date):
            raise ValueError("Invalid rented date type!")
        if not isinstance(due_date, datetime.date):
            raise ValueError("Invalid due date type!")
        if returned_date == "not returned":
            self._returned_date = datetime.date.max
        elif not isinstance(returned_date, datetime.date):
            raise ValueError("Invalid returned date type!")
        else:
            self._returned_date = returned_date
        self.__id = rental_id
        self._movie_id = movie_id
        self._client_id = client_id
        self._rented_date = rented_date
        self._due_date = due_date

    @property
    def id(self):
        return self.__id

    @property
    def movie_id(self):
        return self._movie_id

    @property
    def client_id(self):
        return self._client_id

    @property
    def due_date(self):
        return self._due_date

    @property
    def returned_date(self):
        return self._returned_date

    @property
    def rented_date(self):
        return self._rented_date

    @movie_id.setter
    def movie_id(self, value):
        self._movie_id = value

    @client_id.setter
    def client_id(self, value):
        self._client_id = value

    @due_date.setter
    def due_date(self, value):
        if value < self._rented_date:
            raise ValueError("The due date can't be before the rented date!")
        self._due_date = value

    @returned_date.setter
    def returned_date(self, value):
        if value < self._rented_date:
            raise ValueError("The return date can't be before the rented date!")
        self._returned_date = value

    @rented_date.setter
    def rented_date(self, value):
        if value > self._returned_date:
            raise ValueError("The rented date can't be after the return date!")
        self._rented_date = value

    @staticmethod
    def read_as_string(conv_string):
        conv_string = conv_string.split(',')
        d1 = Rental.parse_date(conv_string[3])
        d2 = Rental.parse_date(conv_string[4])
        d3 = Rental.parse_date(conv_string[5])
        r = Rental(int(conv_string[0]), int(conv_string[1]), int(conv_string[2]), d1, d2, d3)
        return r
    @staticmethod
    def parse_date(given_date):
        """
        the function that parses the user input to a datetime.date object
        :param given_date: the user's input, a string that resembles a date
        :return: the parsed date
        """
        if given_date.lower() == "not returned":
            given_date = datetime.date.max
        else:
            try:
                year, month, day = map(int, given_date.split('-'))
                given_date = datetime.date(year, month, day)
            except ValueError:
                print("Not a valid format! (year/month/date)")
                return
        return given_date

    @staticmethod
    def make_it_string(rental):
        f = f"{rental.id},{rental.movie_id},{rental.client_id},{rental.rented_date},{rental.due_date},{rental.returned_date}\n"
        return f

    def __str__(self):
        s = f"Rental with ID {self.__id} of the movie with ID {self._movie_id} belonging to client {self._client_id}" \
            f"\nRent date: {self._rented_date}\nDue date: {self._due_date}\n"
        if self._returned_date == datetime.date.max and self._due_date < datetime.date.today():
            s += "Returned date: NOT RETURNED! (DUE DATE PASSED)"
        elif self._returned_date == datetime.date.max:
            s += "Returned date: NOT RETURNED!"
        else:
            s += f"Returned date: {self._returned_date}"
        return s


#