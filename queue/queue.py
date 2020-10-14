from typing import List, NoReturn

class QueueWithList:
    MAXSIZE = 10

    def __init__(self) -> NoReturn:
        self._data = [None] * self.MAXSIZE
        self._size = 0
        self._head = -1
        self._tail = -1

    def __len__(self) -> int:
        return self._size

    
