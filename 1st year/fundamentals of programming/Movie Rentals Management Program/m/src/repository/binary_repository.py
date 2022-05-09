from src.repository.repository import Repository
import pickle


class BinaryRepository(Repository):
    def __init__(self, file_name):
        super().__init__()
        self._file_name = file_name
        self.__read_entities()

    @property
    def data(self):
        return super().data

    def __read_entities(self):
        with open(self._file_name, "rb") as f:
            try:
                lis = pickle.load(f)
                for elem in lis:
                    super().add_item(elem)
            except EOFError:
                pass

    def __update_file(self):
        with open(self._file_name, "wb") as f:
            pickle.dump(self.data, f)
            self.data.clear()

    def add_item(self, obj):
        super().add_item(obj)
        self.__update_file()

    def __getitem__(self, item):
        i = super().__getitem__(item)
        self.data.clear()
        return i

    def __setitem__(self, index, item):
        super().__setitem__(index, item)
        self.__update_file()

    def __delitem__(self, index):
        super().__delitem__(index)
        self.__update_file()

    def __str__(self):
        r = super().__str__()
        self.__update_file()
        return r

    @data.setter
    def data(self, value):
        self._data = value
