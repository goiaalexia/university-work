class Movie:
    def __init__(self, movie_id, title, description, genre):
        if not isinstance(movie_id, int):
            raise ValueError("Invalid movie ID type!")
        if not isinstance(title, str):
            raise ValueError("Invalid movie title type!")
        if not isinstance(description, str):
            raise ValueError("Invalid movie description type!")
        if not isinstance(genre, str):
            raise ValueError("Invalid movie genre type!")
        self.__id = movie_id
        self._title = title
        self._description = description
        self._genre = genre

    # GETTER MOVIE ID
    @property
    def id(self):
        return self.__id

    # GETTER TITLE
    @property
    def title(self):
        return self._title

    # GETTER DESCRIPTION
    @property
    def description(self):
        return self._description

    # GETTER GENRE
    @property
    def genre(self):
        return self._genre

    @staticmethod
    def read_as_string(conv_string):
        conv_string = conv_string.split(",")
        m = Movie(int(conv_string[0]), conv_string[1], conv_string[2], conv_string[3])
        return m

    @staticmethod
    def make_it_string(movie):
        f = f"{movie.id},{movie.title},{movie.description},{movie.genre}"
        return f

    def __str__(self):
        return f"The movie {self._title} with ID {self.__id} in the {self._genre} genre: {self._description}"
