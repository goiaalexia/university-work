from src.repository.repository import *


class FileRepository(Repository):
    def __init__(self, file_name, entity_type):
        super().__init__()
        self._file_name = file_name
        self._entity_type = entity_type
        self.__read_entities()

    def __read_entities(self):
        """
        the function that reads entities from a file
        :return: None
        """
        with open(self._file_name, "a+") as f:
            f.seek(0)
            lines = f.readlines()
            for line in lines:
                if line != "\n":
                    super().add_item(self._entity_type.read_as_string(line))

    def __update_file(self):
        """
        the function that updates a file
        :return: None
        """
        with open(self._file_name, "wt") as f:
            f.writelines([self._entity_type.make_it_string(item) for item in super().data])
        # self.data.clear()

    def add_item(self, item):
        super().add_item(item)
        self.__update_file()

    #def __getitem__(self, item):
      #  i = super().__getitem__(item)
       # self.__update_file()
       # return i

    def __setitem__(self, index, item):
        super().__setitem__(index, item)
        self.__update_file()

    def __delitem__(self, index):
        super().__delitem__(index)
        self.__update_file()

    #def __str__(self):
       # r = super().__str__()
       # return r
