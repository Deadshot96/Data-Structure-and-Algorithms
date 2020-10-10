def factorial(n: int) -> int:
    if n == 0:
        return 1
    return n * factorial(n - 1)

if __name__ == '__main__':
    while True:
        n = input("Enter a number : ")

        if n == "":
            break

        fact = factorial(int(n))

        print(f"Factorial of {n}: {fact}")