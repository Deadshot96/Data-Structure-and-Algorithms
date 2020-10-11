from typing import List

def linear_sum(data: List[int]) -> int:
    return linearSumUtil(data, len(data))

def linearSumUtil(data: List[int], index: int) -> int:
    if index == 0:
        return 0
    return data[index - 1] + linearSumUtil(data, index - 1)

def binary_sum(data: List[int]) -> int:
    return binarySumUtil(data, 0, len(data))

def binarySumUtil(data: List[int], start: int, stop: int) -> int:
    if start >= stop:
        return 0
    elif start == stop - 1:
        return data[start]
    else:
        mid = (start + stop) // 2
        return binarySumUtil(data, start, mid) + binarySumUtil(data, mid, stop)



if __name__ == '__main__':
    X = [3, 4, 4, 8, 10, 12, 13, 22, 27, 34, 34, 45,\
         45, 47, 47, 49, 52, 53, 53, 57, 60, 62, 62,\
              63, 64, 65, 77, 84, 92, 97]

    print("Sum of sequence: ", linear_sum(X), sep='\t')
    print("Binary sum of sequence: ", binary_sum(X), sep='\t')
