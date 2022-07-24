class RepoError(Exception):
    pass


class Repository:

    def __init__(self):
        self._repository = []

    def __getitem__(self, item):
        return self._repository[item]

    def __setitem__(self, index, item):
        self._repository[index] = item

    def __delitem__(self, index):
        del self._repository[index]

    @property
    def data(self):
        return self._repository

    @data.setter
    def data(self, value):
        self._repository = value

    def __str__(self):
        s = f"{type(self._repository[0])} list:\n\n"
        for i in self._repository:
            s += f"{i}\n"
        return s

    def pop(self, item_index):
        """
        the function that pops a certain item out of the repo
        :param item_index: the item's index
        :return: None
        """
        self._repository.pop(item_index)

    def __len__(self):
        return len(self._repository)

    def add_item(self, item):
        """
        function that adds an item to the repository
        :param item: the item to be added
        :return:
        """
        if item in self._repository:
            raise RepoError(f"There is already a {type(item)} with ID {str(item.id)} in the repository!")
        self._repository.append(item)
