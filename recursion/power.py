from time import time

def power(x: int, n: int) -> int:
    if n == 0:
        return 1
    else:
        return x * power(x, n - 1)

def quickPower(x: int, n: int) -> int:
    if n == 0:
        return 1
    else:
        partial = quickPower(x, n // 2)
        result = partial * partial
        if n % 2 == 1:
            result *= x
        
        return result


if __name__ == '__main__':
    while True:
        x = input("Enter the number: ")
        n = input("Enter the power: ")

        if x == "" or n == "":
            break
        
        x, n = int(x), int(n)

        startTime = time()
        p = power(x, n)
        timeTaken = time() - startTime
        
        print("Power: ", p, "Time taken: ", timeTaken, sep='\t')
        
        startTime = time()
        p = quickPower(x, n)
        timeTaken = time() - startTime

        print("Quick Power: ", p, "Time taken: ", timeTaken, sep='\t')
