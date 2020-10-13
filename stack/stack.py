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
        self._stack.append(n)
        self._len += 1

    def pop(self) -> int:
        if self.is_empty():
            raise Empty('Empty Stack')
        self._len -= 1
        return self._stack.pop()

    def peek(self) -> int:
        if self.is_empty():
            raise Empty('Empty Stack')
        return self._stack[-1]

    def __str__(self) -> str:
        return " ".join(list(map(str, self._stack)))

    def __repr__(self) -> str:
        return str(self)


if __name__ == '__main__':
    S = StackWithList()
    S.push(29)
    S.push(20)
    print(S.peek())
    print(len(S))
    print(S.pop())
    print(len(S))
    print(S.is_empty())
    print(S.peek())
    for i in range(20):
        S.push(i)
    print(S)