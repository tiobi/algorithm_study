"""
# 14. 02. 15650. N과 M 2
# DATE SOLVED: Solving...

# COMMENTS:
    자연수 N과 M이 주어졌을 때 중복 없이 M개를 고른 수열. 
    오름차순.
"""

import sys

N, M = map(int, sys.stdin.readline().split())
arr = []

def DFS(array):
    if len(array) == M:
        print(" ".join(map(str, array)))

    for i in range(1, N + 1):
        if i not in array:
            array.append(i)
            DFS(array)
            array.pop()

DFS(arr)