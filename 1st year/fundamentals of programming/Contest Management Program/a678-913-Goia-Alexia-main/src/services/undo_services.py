class UndoRedoError(Exception):
    pass


class UndoServices:

    def __init__(self):
        self._history = []
        self._index = -1

    def record(self, operation):
        """
        the function that records the previous operation in history
        :param operation: the operation
        :return: None
        """
        length = len(self._history) - 1
        while self._index != length:
            self._history.pop()
            length = len(self._history) - 1
        self._history.append(operation)
        self._index = len(self._history) - 1

    def undo(self):
        """
        the function that undoes the last operation
        :return: None
        """
        if self._index == - 1:
            raise UndoRedoError("There's nothing to undo!")
        else:
            self._history[self._index].undo()
            self._index -= 1

    def redo(self):
        """
        the function that redoes the last undone operation
        :return: None
        """
        if self._index == len(self._history) - 1:
            raise UndoRedoError("There's nothing to redo!")
        else:
            self._history[self._index].redo()
            self._index += 1


class Call:

    def __init__(self, function_name, *function_params):
        self._function_name = function_name
        self._function_params = function_params

    def call(self):
        """
        the function call calls a certain function with certain parameters
        :return: None
        """
        self._function_name(*self._function_params)


class Operation:

    def __init__(self, undo_call, redo_call):
        self._undo_call = undo_call
        self._redo_call = redo_call

    def undo(self):
        """
        the function that calls the operation to be undone in the stack
        :return: None
        """
        self._undo_call.call()

    def redo(self):
        """
        the function that calls the operation to be redone in the stack
        :return:
        """
        self._redo_call.call()


class CascadedOperation:

    def __init__(self):
        self._operations = []

    def add(self, operation):
        """
        the function that adds an operation to the cascaded operation
        :param operation: the operation that is a compound of the cascaded one
        :return: None
        """
        self._operations.append(operation)

    def undo(self):
        """
        cascaded undo that undoes all the operations in the cascaded one
        :return: None
        """
        for op in self._operations:
            op.undo()

    def redo(self):
        """
        cascaded redo that redoes all the operations in the cascaded one
        :return: None
        """
        for op in self._operations:
            op.redo()
