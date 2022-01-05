"""
# 14. 05. 9663. N-Queen
# DATE SOLVED: Solving...

# COMMENTS:
    N * N 체스판 위에 퀸 N개를 서로 공격할 수 업게 놓는 문제. 

"""

import sys

N = int(sys.stdin.readline())


def sol(arr, coor):
    if len(arr) == N:
        print("Y")
        return

    for i in range(coor[0], N + 1):
        for j in range(coor[1], N + 1):
            if i != coor[0] and j != coor[1]:
                array.append((i,j))
                sol(array, (i, j))
                array.pop()



array = []
count = 0

sol(array, (1, 1))