from typing import List, NoReturn

class QueueWithList:
    MAXSIZE = 10

    def __init__(self) -> NoReturn:
        self._data = [None] * self.MAXSIZE
        self._size = 0

    def __len__(self) -> int:
        return self._size

    def isEmpty(self) -> bool:
        return self._size == 0

    def enqueue(self, val: int) -> NoReturn:
        if len(self) == self.MAXSIZE:
            self._resize()

    def dequeue(self) -> int:
        pass

    def _resize(self):
        self.MAXSIZE *= 2
        temp = [None] * self.MAXSIZE

        for index, value in enumerate(self._data):
            temp [index] = value
        self._data = temp
    
