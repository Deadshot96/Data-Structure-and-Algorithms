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

    def isEmpty(self) -> bool:
        return self._len == 0

    def push(self, n: int) -> NoReturn:
        self._stack.append(n)
        self._len += 1

    def pop(self) -> int:
        if self.isEmpty():
            raise Empty('Empty Stack')
        self._len -= 1
        return self._stack.pop()

    def peek(self) -> int:
        if self.isEmpty():
            raise Empty('Empty Stack')
        return self._stack[-1]

    def __str__(self) -> str:
        return " ".join(list(map(str, self._stack)))

    def __repr__(self) -> str:
        return str(self)


class StackWithLinkedList:

    class _Node:
        def __init__(self, val: int) -> NoReturn:
            self.data = val
            self.next = None

    def __init__(self):
        self._head = None
        self._len = 0

    def __len__(self) -> int:
        return self._len

    def isEmpty(self) -> bool:
        return self._head is None

    def push(self, val: int) -> NoReturn:
        node = self._Node(val)
        node.next = self._head
        self._head = node
        self._len += 1


    def pop(self) -> int:
        if self.isEmpty():
            raise Empty("Empty Stack")
        val = self._head.data
        self._head = self._head.next
        self._len -= 1
        return val

    def peek(self) -> int:
        if self.isEmpty():
            raise Empty("Empty Stack")

        return self._head.data

    def __str__(self) -> str:
        s = ""
        temp = self._head

        while temp is not None:
            s += (str(temp.data) + " ")
            temp = temp.next

        return s[:-1]

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
    print(S.isEmpty())
    print(S.peek())
    for i in range(20):
        S.push(i)
    print(S)