# This will walk through given path recursively 
# and print the size of each path

import os
from typing import Text
from os.path import dirname, abspath

def DiskUsage(path: Text) -> int:
    total = os.path.getsize(path)
    if os.path.isdir(path):
        for filename in os.listdir(path):
            childpath = os.path.join(path, filename)
            total += DiskUsage(childpath)

    print("{0:<7}".format(total), path)
    return total

if __name__ == '__main__':
    path = dirname(abspath(__file__))
    # print(path)
    total = DiskUsage(path)
    print("Total size: ", total)