def product(x: int, y: int) -> int:
    return prodUtil(max(x, y), min(x, y))

def prodUtil(x: int, y:int) -> int:
    if y == 0:
        return 0
    return x + prodUtil(x, y - 1)

if __name__ == "__main__":
    while True:
        x = input("Enter the 1st num: ")
        if x == "":
            break

        y = input("Enter the 2nd num: ")
        if y == "":
            break

        prod = product(int(x), int(y))
        print(f"Product is: {prod}")
