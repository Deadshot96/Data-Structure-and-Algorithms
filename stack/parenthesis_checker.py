from stack import StackWithList

def checkParenthesis(s: int) -> bool:
    right = ")]}"
    left = "([{"
    parenthesisStack = StackWithList()
    for i in s:
        if i in left:
            parenthesisStack.push(i)

        elif i in right:
            if parenthesisStack.isEmpty():
                return False
            j = parenthesisStack.pop()
            if left.index(j) != right.index(i):
                return False

    if not parenthesisStack.isEmpty():
        return False
    return True


if __name__ == "__main__":
    statement = "((name))(something)()(({{}}))[][][]{{}}(([]))"
    print(checkParenthesis(statement))
    statement = "{main}[()])"
    print(checkParenthesis(statement))
