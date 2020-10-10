import time
from typing import Tuple

def bad_Fibonacci(n: int) -> int:
    if n <= 1:
        return 1
    return bad_Fibonacci(n - 1) + bad_Fibonacci(n - 2)

def good_Fibonacci(n: int) -> Tuple:
    
    if n <= 1:
        return (n, 0)
    else:
        a, b = good_Fibonacci(n - 1)
        return (a + b, a)

if __name__ == "__main__":
    while True:
        n = input("Enter the index of Fib seq: ")

        if n == "":
            break
        
        startTime = time.time()
        fib = bad_Fibonacci(int(n))
        timeTaken = time.time() - startTime
        print("Bad Fib num: ", fib, sep='\t')
        print("Bad Fib Time taken: ", timeTaken)


        startTime = time.time()
        fib, _ = good_Fibonacci(int(n) + 1)
        timeTaken = time.time() - startTime
        print("Good Fib num: ", fib, sep='\t')
        print("Good Fib Time taken: ", timeTaken)
