#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the fairRations function below.
def fairRations(A):
    suml = 0;
    current = -1
    paired = -1
    distance = 0
    total = 0;

    for i in A:
        suml += i
        if(i % 2 == 1 and current == -1):
            current = i
            paired = -1
            distance = 0
        elif(current != -1 and i % 2 == 1):
            paired = i
            current = -1
            loavesNeeded = (2 + ((distance + 1) - 1) * 2)
            total += loavesNeeded
        else:
            distance += 1   

    if(suml % 2 == 1):
        return "NO"
    else :
        return total

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    N = int(input())

    A = list(map(int, input().rstrip().split()))

    result = fairRations(A)

    fptr.write(str(result) + '\n')

    fptr.close()
