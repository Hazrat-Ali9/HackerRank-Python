#!/bin/python3

import math
import os
import random
import re
import sys

def climbingLeaderboard(ranked, player):
    res = []
    x = [(ranked[0], 1)]
    for r in ranked[1:]:
        if r != x[-1][0]:
            x.append((r, x[-1][1] + 1))
    i = len(x) - 1
    for p in player:
        while i >= 0 and p > x[i][0]:
            i -= 1
        if i < 0:
            res.append(1)
        elif p == x[i][0]:
            res.append(x[i][1])
        else:
            res.append(x[i][1] + 1)
    return res

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ranked_count = int(input().strip())

    ranked = list(map(int, input().rstrip().split()))

    player_count = int(input().strip())

    player = list(map(int, input().rstrip().split()))

    result = climbingLeaderboard(ranked, player)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
