import datetime
from src.domain.movie import Movie
from src.domain.rental import Rental
from src.domain.client import Client
from src.services.movie_services import MovieServices
from src.services.rental_services import RentalServices
from src.services.client_services import ClientServices
from src.services.undo_services import *
from enum import Enum
from src.repository.repository import RepoError
from settings import Settings

class UIError(Exception):
    pass


class WhichMenu(Enum):
    """
    this class is used to determine in which menu we currently reside, by using an enumerator
    """
    MainMenu = 1
    MovieMenu = 2
    ClientMenu = 3
    RentalMenu = 4


class ApplicationUI:
    def __init__(self, settings):
        self._movie_service = MovieServices(settings)
        self._client_service = ClientServices(settings)
        self._rental_service = RentalServices(settings)
        self._menu_state = WhichMenu.MainMenu
        self._undo_service = UndoServices()

    @property
    def state(self):
        return self._menu_state

    @property
    def movie_service(self):
        return self._movie_service

    @property
    def rental_service(self):
        return self._rental_service

    @property
    def client_service(self):
        return self._client_service

    @state.setter
    def state(self, value):
        self._menu_state = value

    @staticmethod
    def print_main_menu():
        """
        the function that prints the main menu
        :return: None
        """
        print("1. Movie Menu")
        print("2. Client Menu")
        print("3. Rental Menu")
        print("4. Undo")
        print("5. Redo")
        print("6. Exit")

    @staticmethod
    def print_movie_menu():
        """
        the function that prints the movie menu
        :return: None
        """
        print("1. Add Movie")
        print("2. Update Movie")
        print("3. Remove Movie")
        print("4. List Movies")
        print("5. Search Movies")
        print("6. Back")

    @staticmethod
    def print_client_menu():
        """
        the function that prints the client menu
        :return: None
        """
        print("1. Add Client")
        print("2. Update Client")
        print("3. Remove Client")
        print("4. List Clients")
        print("5. Search Clients")
        print("6. Back")

    @staticmethod
    def print_rentals_menu():
        """
        the function that prints the rental menu
        :return: None
        """
        print("1. Add Rental")
        print("2. Finish Rental")
        print("3. List Rentals")
        print("4. Most Rented Movies")
        print("5. Most Active Clients")
        print("6. Late Rentals")
        print("7. Back")

    def print_menu(self):
        """
        the function that prints the good menu, depending on the current menu state
        :return:
        """
        if self._menu_state == WhichMenu.MainMenu:
            ApplicationUI.print_main_menu()
        elif self._menu_state == WhichMenu.ClientMenu:
            ApplicationUI.print_client_menu()
        elif self._menu_state == WhichMenu.RentalMenu:
            ApplicationUI.print_rentals_menu()
        elif self._menu_state == WhichMenu.MovieMenu:
            ApplicationUI.print_movie_menu()
        else:
            raise UIError("Not a valid menu!")

    def run_command(self, command):
        """
        the function that runs the necessary command, depending on the menu state
        :param command: the command
        :return: None
        """
        if self._menu_state == WhichMenu.ClientMenu:
            self.process_client_menu(command)
        elif self._menu_state == WhichMenu.RentalMenu:
            self.process_rental_menu(command)
        elif self._menu_state == WhichMenu.MovieMenu:
            self.process_movie_menu(command)
        elif self._menu_state == WhichMenu.MainMenu:
            self.process_main_menu(command)
        else:
            raise UIError("Not a valid menu state!")

    @staticmethod
    def get_command():
        """
        the function that gets a command from user input
        :return: the command, parsed a.k.a. made to be an integer
        """
        command = input("Please input a command: ")
        try:
            command = int(command)
            return command
        except ValueError:
            print("Invalid command! (please input the corresponding number)")
            return

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
                year, month, day = map(int, given_date.split('/'))
                given_date = datetime.date(year, month, day)
            except ValueError:
                print("Not a valid format! (year/month/date)")
                return
        return given_date

    def process_main_menu(self, command):
        """
        the main menu process
        :param command: the command to be executed
        :return: None
        """
        if command == 1:  # movie menu
            self.state = WhichMenu.MovieMenu
        elif command == 2:  # client menu
            self.state = WhichMenu.ClientMenu
        elif command == 3:  # rental menu
            self.state = WhichMenu.RentalMenu
        elif command == 4:  # undo
            try:
                self._undo_service.undo()
            except UndoRedoError as ure:
                print(str(ure))
        elif command == 5:  # redo
            try:
                self._undo_service.redo()
            except UndoRedoError as ure:
                print(str(ure))
        elif command == 6:  # exit
            print("Goodbye!")
            exit()
        else:
            raise UIError("Not a valid command!")

    def process_rental_menu(self, command):
        """
        the rental menu
        :param command: the command to be executed
        :return: None
        """
        if command == 1:  # add a rental
            rental_id = movie_id = client_id = None
            try:
                ok = False  # rental id input
                while not ok:
                    try:
                        rental_id = int(input("Input a new rental ID: "))
                        ok = True
                    except ValueError:
                        print("Please input an actual ID number!")
                        return
                ok = False  # movie id input
                okmovie = False
                while not ok:
                    try:
                        movie_id = int(input("Input an existing movie ID: "))
                        ok = True
                        for i in self.movie_service.movie_repo:
                            if i.id == movie_id:
                                okmovie = True
                    except ValueError:
                        print("Please input an ID number!")
                ok = False  # client id input
                okclient = False
                while not ok:
                    try:
                        client_id = int(input("Input a client ID: "))
                        ok = True
                        for i in self._client_service.client_repo:
                            if i.id == client_id:
                                okclient = True
                    except ValueError:
                        print("Please input an ID number!")
                        return
                rented_date = ApplicationUI.parse_date(input("Enter rented date (YYYY/MM/DD): "))
                due_date = ApplicationUI.parse_date(input("Enter due date (YYYY/MM/DD): "))
                returned_date = ApplicationUI.parse_date(input("Enter returned date (YYYY/MM/DD) or 'not returned': "))
                if rental_id is None or movie_id is None or client_id is None:
                    raise UIError("Something weird happened here. Try inputting correct data?")
                if okclient is True and okmovie is True:
                    r = Rental(rental_id, movie_id, client_id, rented_date, due_date, returned_date)
                    self._rental_service.add_rental(r)
                    """
                    
                    THIS IS GOING TO HAPPEN EVERYWHERE WHERE WE MODIFY THE REPOS. 
                    We are going to register the calls necessary to undo or redo, and then create an operation
                    that we are going to record in the history. Same thing for the cascading operations, but
                    when there are cascading ones (remove client/movie) we basically do it more times in one.
                    
                    """
                    undo = Call(self._rental_service.remove_last_rental, r.id)
                    redo = Call(self._rental_service.add_rental, r)
                    op = Operation(undo, redo)
                    self._undo_service.record(op)
                elif okclient is False and okmovie is True:
                    raise RepoError("There is no client with that ID!")
                elif okclient is True and okmovie is False:
                    raise RepoError("There is no movie with that ID!")
                else:
                    raise RepoError("There is no client or movie with that ID!")
            except ValueError as ve:
                print(str(ve))
            except RepoError as re:
                print(str(re))
            except TypeError as te:
                print(str(te))
            except UIError as ue:
                print(str(ue))
        elif command == 2:  # return rental
            rental_id = None
            ok = False  # rental id input
            while not ok:
                try:
                    rental_id = int(input("Enter the ID of the rental you want to return: "))
                    ok = True
                except ValueError:
                    print("Please input a valid value!")
                    return
            try:
                thing = datetime.date.today()
                self._rental_service.return_rental(rental_id, thing)
                undo = Call(self._rental_service.unreturn_rental, rental_id)
                redo = Call(self._rental_service.return_rental, rental_id, thing)
                op = Operation(undo, redo)
                self._undo_service.record(op)
            except KeyError:
                print("Invalid ID!")
            except ValueError as ve:
                print(str(ve))
            except RepoError as re:
                print(str(re))
        elif command == 3:  # list rentals
            print(self.rental_service)
        elif command == 4:  # most rented movies
            try:
                print("The most rented movies are:")
                for i in self._rental_service.most_rented_movies(self._movie_service.movie_repo):
                    print(i)
            except ValueError as ve:
                print(str(ve))
            except RepoError as re:
                print(str(re))
            except TypeError as te:
                print(str(te))
            except IndexError:
                pass
        elif command == 5:  # most active clients
            try:
                print("The most active clients are:")
                for i in self._rental_service.most_active_clients(self._client_service.client_repo):
                    print(i)
                print("\n")
            except ValueError as ve:
                print(str(ve))
            except RepoError as re:
                print(str(re))
            except TypeError as te:
                print(str(te))
            except IndexError as ie:
                print(str(ie))
        elif command == 6:  # late rentals
            try:
                print("The movies that are in late rentals are:")
                for i in self._rental_service.late_rentals(self._movie_service.movie_repo):
                    print(i)
                print("\n")
            except ValueError as ve:
                print(str(ve))
            except RepoError as re:
                print(str(re))
            except TypeError as te:
                print(str(te))
            except IndexError as ie:
                print(str(ie))
        elif command == 7:  # go back
            self._menu_state = WhichMenu.MainMenu
        else:
            raise UIError("Unrecognised command!")

    def process_client_menu(self, command):
        """
        the client menu
        :param command: the command to be executed
        :return: None
        """
        if command == 1:  # add client
            client_id = None
            ok = False  # client id input
            while not ok:
                try:
                    client_id = int(input("Enter new client ID: "))
                    ok = True
                except ValueError:
                    print("Invalid ID!")
                    return
            name = str(input("Enter new client name: "))
            try:
                c = Client(client_id, name)
                self._client_service.add_client(c)
                undo = Call(self._client_service.remove_client, c.id)
                redo = Call(self._client_service.add_client, c)
                op = Operation(undo, redo)
                self._undo_service.record(op)
            except ValueError as ve:
                print(str(ve))
            except RepoError as re:
                print(str(re))
            except KeyError as ke:
                print(str(ke))
            except TypeError as te:
                print(str(te))
        elif command == 2:  # update client
            client_id = None
            ok = False  # client id input
            while not ok:
                try:
                    client_id = int(input("Enter the ID of the client you want to update: "))
                    ok = True
                except ValueError:
                    print("Invalid ID!")
                    return
            name = str(input("Enter new client name: "))
            try:
                c = Client(client_id, name)
                former_c = self._client_service.client_repo[client_id]
                self._client_service.update_client(c)
                undo = Call(self._client_service.client_setter, client_id, former_c)
                redo = Call(self._client_service.client_setter, client_id, c)
                op = Operation(undo, redo)
                self._undo_service.record(op)
            except ValueError as ve:
                print(str(ve))
            except RepoError as re:
                print(str(re))
            except KeyError as ke:
                print(str(ke))
            except TypeError as te:
                print(str(te))
        elif command == 3:  # remove client
            try:
                client_id = int(input("Enter the ID of the client you want to remove: "))
            except ValueError:
                print("Invalid ID!")
                return
            try:
                the_client = self._client_service.get_client_with_certain_id(client_id)
                undo = Call(self._client_service.add_client, the_client)
                redo = Call(self._client_service.remove_client, client_id)
                op = Operation(undo, redo)

                """
                
                as you can see, in the cascaded operation we basically have to also remove all the rentals
                that follow a client, which is why I said earlier that cascaded operations are more operations
                considered to be a single one, as a whole.
                
                """

                cascaded_op = CascadedOperation()
                cascaded_op.add(op)
                self._client_service.remove_client(client_id)
                the_rentals = self._rental_service.get_the_rentals_of_a_certain_client(client_id)
                self._rental_service.remove_certain_rentals_client(client_id)
                for rental in the_rentals:
                    undo = Call(self._rental_service.add_rental, rental)
                    redo = Call(self._rental_service.remove_rental, rental.id)
                    op = Operation(undo, redo)
                    cascaded_op.add(op)
                self._undo_service.record(cascaded_op)
            except KeyError:
                print("Nonexistent ID!")
            except ValueError as ve:
                print(str(ve))
            except RepoError as re:
                print(str(re))
        elif command == 4:  # list clients
            print(self._client_service)
        elif command == 5:  # search clients by field
            try:
                which_field = str(input("Enter by which field you want to search: "))
                search_term = str(input("Search: "))
                # print(str(self._client_service.search_clients(search_term, which_field))) -> failed print attempt
                for el in self._client_service.search_clients(search_term, which_field):
                    print(el)
            except ValueError as ve:
                print(str(ve))
        elif command == 6:  # go back
            self.state = WhichMenu.MainMenu
        else:
            raise UIError("Unrecognised command!")

    def process_movie_menu(self, command):
        """
        the movie menu
        :param command: the command to be executed
        :return: None
        """
        if command == 1:  # add movie
            movie_id = None
            ok = False  # movie ID input
            while not ok:
                try:
                    movie_id = int(input("Enter new movie ID: "))
                    ok = True
                except ValueError:
                    print("Invalid ID!")
                    return
            title = input("Enter new movie title: ")
            desc = input("Enter new movie description: ")
            genre = input("Enter new movie genre: ")
            try:
                m = Movie(movie_id, title, desc, genre)
                self._movie_service.add_movie(m)
                undo = Call(self._movie_service.remove_movie, m.id)
                redo = Call(self._movie_service.add_movie, m)
                op = Operation(undo, redo)
                self._undo_service.record(op)
            except KeyError:
                print("Nonexistent ID!")
            except ValueError as ve:
                print(str(ve))
            except RepoError as re:
                print(str(re))
        elif command == 2:  # update movie
            movie_id = None
            ok = False
            while not ok:
                try:
                    movie_id = int(input("Enter the ID of the movie you want to update: "))
                    ok = True
                except ValueError:
                    print("Invalid ID!")
                    return
            title = input("Enter new movie title: ")
            desc = input("Enter new movie description: ")
            genre = input("Enter new movie genre: ")
            try:
                m = Movie(movie_id, title, desc, genre)
                former_m = self._movie_service.get_movie_with_certain_id(movie_id)
                self._movie_service.update_movie(m)
                undo = Call(self._movie_service.movie_setter, movie_id, former_m)
                redo = Call(self._movie_service.movie_setter, movie_id, m)
                op = Operation(undo, redo)
                self._undo_service.record(op)
            except KeyError:
                print("Nonexistent ID!")
            except ValueError as ve:
                print(str(ve))
            except RepoError as re:
                print(str(re))
        elif command == 3:  # remove movie
            movie_id = None
            try:
                movie_id = int(input("Enter the ID of the movie you want to remove: "))
            except ValueError:
                print("Invalid ID!")
            try:
                the_movie = self._movie_service.get_movie_with_certain_id(movie_id)
                undo = Call(self._movie_service.add_movie, the_movie)
                redo = Call(self._movie_service.remove_movie, movie_id)
                op = Operation(undo, redo)

                cascaded_op = CascadedOperation()
                cascaded_op.add(op)
                self._movie_service.remove_movie(movie_id)
                the_rentals = self._rental_service.get_the_rentals_of_a_certain_movie(movie_id)
                self._rental_service.remove_certain_rentals_movie(movie_id)
                for rental in the_rentals:
                    undo = Call(self._rental_service.add_rental, rental)
                    redo = Call(self._rental_service.remove_rental, rental.id)
                    op = Operation(undo, redo)
                    cascaded_op.add(op)
                self._undo_service.record(cascaded_op)
            except KeyError:
                print("Nonexistent ID!")
            except ValueError as ve:
                print(str(ve))
            except RepoError as re:
                print(str(re))
        elif command == 4:  # list movies
            print(self._movie_service)
        elif command == 5:  # search movies by field
            try:
                which_field = str(input("Enter by which field you want to search: "))
                search_term = str(input("Search: "))
                # print(str(self._client_service.search_clients(search_term, which_field))) -> failed print attempt
                for el in self._movie_service.search_movies(search_term, which_field):
                    print(el)
            except ValueError as ve:
                print(str(ve))
        elif command == 6:  # back
            self.state = WhichMenu.MainMenu
        else:
            raise UIError("Unrecognised command!")


class App:

    def __init__(self, settings):
        self._ui = ApplicationUI(settings)
        self.running = True

    @property
    def ui(self):
        return self._ui

    def start(self):
        """
        the function that starts the application
        :return: None
        """
        while self.running:
            self.ui.print_menu()
            command = ApplicationUI.get_command()
            if command is not None:
                try:
                    self.ui.run_command(command)
                except UIError as ue:
                    print(str(ue))


if __name__ == "__main__":
    settingss = Settings()
    app = App(settingss)
    app.start()
