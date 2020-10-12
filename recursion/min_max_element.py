from typing import List

def minimumElement(data: List[int]) -> int:
    return minEleUtil(data, len(data))

def minEleUtil(data: List[int], index: int) -> int:
    if index == 1:
        return data[0]

    return min(data[index - 1], minEleUtil(data, index - 1))

def maximumElement(data: List[int]) -> int:
    return maxEleUtil(data, len(data))

def maxEleUtil(data: List[int], index: int) -> int:
    if index == 1:
        return data[0]

    return max(data[index - 1], maxEleUtil(data, index - 1))

if __name__ == '__main__':
    X = [3, 4, 4, 8, 10, 12, 13, 22, 27, 34, 34, 45,\
         45, 47, 47, 49, 52, 53, 53, 57, 60, 62, 62,\
              63, 64, 65, 77, 84, 92, 97]

    print("Minimum Element: ", minimumElement(X))
    print("Maximum Element: ", maximumElement(X))