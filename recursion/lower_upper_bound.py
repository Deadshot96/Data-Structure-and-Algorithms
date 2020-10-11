# Get lower and upper bound of a element in sorted list using binary search
from typing import List, Tuple

def lBoundUtil(data: List[int], target:int) -> int:
    low = 0
    high = len(data) - 1
    first_pos = -1

    while low <= high:
        mid = (low + high) // 2

        if data[mid] < target:
            first_pos = mid
            low = mid + 1

        elif data[mid] >= target:
            high = mid - 1

    return first_pos + 1

def uBoundUtil(data: List[int], target: int) -> int:
    low = 0
    high = len(data) - 1
    first_pos = len(data)

    while low <= high:
        mid = (low + high) // 2
        
        if data[mid] <= target:
            low = mid + 1
        else:
            first_pos = mid
            high = mid - 1

    return first_pos - 1

def lower_bound(data: List[int], target: int) -> int:
    return lBoundUtil(data, target)

def upper_bound(data: List[int], target: int) -> int:
    return lBoundUtil(data, target + 1) - 1

def low_upp_bound(data: List[int], target: int) -> Tuple:

    low = lower_bound(data, target)
    high = upper_bound(data, target)

    if low > high:
        return (-1, -1)

    return lower_bound(data, target), upper_bound(data, target)



if __name__ == '__main__':
    X = [0, 0, 0, 0, 0, 1, 1, 1, 2, 2, 2, 3, 3,\
         3, 4, 4, 5, 5, 5, 6, 6, 6, 6, 7, 8, 9, 9, 9, 9, 9]

    target = 1 # ans should be 5, 7

    print("lower bound: ", lower_bound(X, target), sep="\t")
    print("upper bound: ", uBoundUtil(X, target), sep="\t")
    print("lower-upper bound: ", low_upp_bound(X, target), sep="\t")


