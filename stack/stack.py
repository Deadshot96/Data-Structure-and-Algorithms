from typing import NoReturn


class Empty(Exception):
    # attempting to access the component from empty stack
    pass

 class StackWithList():

    def __init__(self):
        self._stack = list()
        self._len = 0

    def __len__(self) -> int:
        return self._len

    def is_empty(self) -> bool:
        return self._len == 0

    def push(self, n: int) -> NoReturn:
        pass

    def pop(self) -> int:
        pass

    def peek(self) -> int:
        pass



