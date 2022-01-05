"""
# 14. 03. 15651. N과 M 3
# DATE SOLVED: 22. 01. 05

# COMMENTS:
    N까지 자연수 중에서 중복을 포함한 M개의 자연수를 고른 수열. 
    오름차순 정렬
"""

import sys

N, M = map(int, sys.stdin.readline().split())

arr = []

def DFS(array):
    if len(array) == M:
        print(" ".join(map(str, array)))
        return

    for i in range(1, N + 1):
        array.append(i)
        DFS(array)
        array.pop()

DFS(arr)
