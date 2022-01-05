"""
# 14. 04. 15652. N과 M 4
# DATE SOLVED: 22. 01. 05

# COMMENTS:
    1부터 N까지 자연수 중 비내림차순 정렬, 같은 수 허용, M개 선택
"""

import sys

N, M = map(int, sys.stdin.readline().split())

def DFS(array, k):
    if len(array) == M:
        print(" ".join(map(str, array)))
        return

    for i in range(k, N + 1):
        array.append(i)
        DFS(array, i)
        array.pop()

ar = []
DFS(ar, 1)