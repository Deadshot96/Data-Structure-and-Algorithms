# This will give integer part of log operation
# only with addition and integer division

def logBase(num: int, base: int) -> int:
    if num == 0:
        return -1
    return 1 + logBase(num // base, base)

if __name__ == "__main__":
    while True:
        x = input("Enter the number: ")
        if x == "":
            break

        b = input("Enter the base: ")
        if b == "":
            break

        ans = logBase(int(x), int(b))

        print(f"Log of {x} with base {b} is: {ans}")
