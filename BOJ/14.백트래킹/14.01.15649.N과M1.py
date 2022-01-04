"""
# 14. 01. 15649. N과 M 1
# DATE SOLVED: 22. 01. 05

# COMMENTS:
    1부터 N까지 자연수 중에서 중복 없이 M개를 고른 수열
"""

from collections import deque
import sys

n, m = list(map(int, sys.stdin.readline().split()))

s = []

def DFS(arr):
    if len(arr) == m:
        print(" ".join(map(str, arr)))
        return

    for i in range(1, n + 1):
        if i not in arr:
            arr.append(i)
            DFS(arr)
            arr.pop()

DFS(s)