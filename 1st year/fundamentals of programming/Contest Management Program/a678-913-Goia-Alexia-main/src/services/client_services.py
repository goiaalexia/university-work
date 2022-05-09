from src.repository.file_repository import *
from src.repository.binary_repository import *
import random
from src.domain.client import *
from src.repository.repository import *


class ClientServices:

    def __init__(self, settings):
        if settings.repo_type == "inmemory":
            self._client_repo = Repository()
        elif settings.repo_type == "file":
            self._client_repo = FileRepository(settings.client_file, Client)
        elif settings.repo_type == "binary":
            self._client_repo = BinaryRepository(settings.client_file)
        #self.generate_random_clients()

    @property
    def client_repo(self):
        return self._client_repo

    def client_setter(self, client_index, client):
        self._client_repo[client_index] = client

    def get_client_with_certain_id(self, client_id):
        the_client = 0
        for i in self._client_repo:
            if i.id == client_id:
                the_client = i
        return the_client

    def generate_random_clients(self):
        """
        the function that generates 20 random clients in the list
        :return: None
        """
        names = ["Suciu", "Vlaicu", "Luca", "Lujerdean", "Werner", "Chirila", "Murg", "Traian", "Remetan", "Pop",
                 "Paul", "Mircea", "Jugu", "Doia", "Vancea", "Rosca"]
        surnames = ["Ana", "Vanessa", "Serafina", "Clara", "Marius", "Adrian", "Dumitru", "Bogdan", "Maria", "Theresa",
                    "Razvan", "Mirabela", "Daniela"]
        for i in range(0, 20):
            generated_name = Client(i, random.choice(names) + " " + random.choice(surnames))
            self._client_repo.add_item(generated_name)

    def add_client(self, client):
        """
        the function that adds a client to the repo
        :param client: the client to be added
        :return: None
        """
        can_we_add = True
        for i in self._client_repo:
            if client.id == getattr(i, "id"):  # the consequences of working with a list
                can_we_add = False
        if can_we_add is True:
            self._client_repo.add_item(client)
        else:
            raise RepoError("There is already a client with that ID!")

    def update_client(self, updated_client):
        """
        the function that updates an existing client
        :param updated_client: the new information for the client
        :return: None
        """
        did_we_update = False
        for i in range(0, len(self._client_repo)):
            if getattr(self._client_repo[i], "id") == updated_client.id:  # if we can update it, we do
                self._client_repo[i] = updated_client
                did_we_update = True
        if did_we_update is False:
            raise RepoError("There is no client with that ID to be updated!")

    def remove_client(self, client_to_be_removed_index):
        """
        the function that removes a certain client from the repository
        :param client_to_be_removed_index: the client's id
        :return: None
        """
        did_we_remove = False
        the_client = []
        for i in self._client_repo:
            if i.id == client_to_be_removed_index:
                the_client.append(i)
                did_we_remove = True
        self._client_repo.data = [x for x in self._client_repo.data if x not in the_client]
        if did_we_remove is False:
            raise ValueError("There is no client with that ID to be removed!")

    def search_clients(self, search_term, which_field):
        """
        function that searches and returns a list of clients
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
            for i in self._client_repo:
                if search_term == i.id:
                    returned_list.append(i)
        elif which_field == "name":
            for i in self._client_repo:
                if search_term in i.name.lower():
                    returned_list.append(i)
        else:
            raise ValueError("Not a valid field!")
        if len(returned_list) > 0:
            return returned_list
        returned_list.append("The search returned no results!\n")
        return returned_list

    def __str__(self):
        s = f"\033[1;35;40mClient repository:\033[0;0m\n\n"
        for i in self._client_repo:
            s += f"{i}\n"
        return s
