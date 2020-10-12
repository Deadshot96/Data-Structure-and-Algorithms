def Harmonic_num(n: int) -> float:
    if n <= 1:
        return 1
    return 1 / n + Harmonic_num(n - 1)

if __name__ == '__main__':
    while True:
        n = input("Enter the number: ")
        if n == "":
            break
        hNum = Harmonic_num(int(n))
        print(f"The Harmonic Number of index {n} is: {hNum}")

