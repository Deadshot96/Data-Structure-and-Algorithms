from typing import List
from random import random

def binary_search(data: List[int], target: int) -> int:
    if random() < 0.5:
        print("with recursion")
        return bSearchUtilwRecursion(data, target, 0, len(data) - 1)
    else:
        print("without recursion")
        return bSearchwoRecursion(data, target)

def bSearchUtilwRecursion(data: List[int], target: int, low: int, high: int) -> int:

    if low > high:
        return -1
    else:
        mid = (low + high) // 2

        if target == data[mid]:
            return mid
        else:
            if data[mid] > target:
                high = mid - 1
            else:
                low = mid + 1

            return bSearchUtilwRecursion(data, target, low, high)

def bSearchwoRecursion(data: List[int], target: int) -> int:
    low = 0
    high = len(data) - 1
    
    while low <= high:
        mid = (low + high) // 2
        if data[mid] == target:
            return mid

        elif data[mid] > target:
            high = mid - 1

        else:
            low = mid + 1
    
    return -1





if __name__ == '__main__':
    X = [3, 4, 4, 8, 10, 12, 13, 22, 27, 34, 34, 45,\
         45, 47, 47, 49, 52, 53, 53, 57, 60, 62, 62,\
              63, 64, 65, 77, 84, 92, 97]

    # sorting the data
    X.sort()
    target = 12

    index = binary_search(X, target)
    print('The index is: ', index)
