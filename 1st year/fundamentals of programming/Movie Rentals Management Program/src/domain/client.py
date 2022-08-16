class Client:
    def __init__(self, client_id, name):
        if not isinstance(client_id, int):
            raise ValueError("Invalid client ID type!")
        if not isinstance(name, str):
            raise ValueError("Invalid client name type!")
        self.__id = client_id
        self._name = name

    # GETTER MOVIE ID
    @property
    def id(self):
        return self.__id

    # GETTER TITLE
    @property
    def name(self):
        return self._name

    @staticmethod
    def read_as_string(conv_string):
        # print(conv_string)
        conv_string = conv_string.split(",")
        c = Client(int(conv_string[0]), conv_string[1])
        return c

    @staticmethod
    def make_it_string(client):
        f = f"{client.id},{client.name}"
        return f

    def __str__(self):
        return f"Client {self._name} with ID {self.__id}"
