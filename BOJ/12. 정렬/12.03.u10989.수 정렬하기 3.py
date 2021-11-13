"""
# 12. 03. 10989. 수 정렬하기 3
# DATE SOLVED: Solving...

# COMMENTS:
    N 개의 수를 오름차순으로 정렬.
    O(nlogn)으로 풀어야 하는 문제. 
    퀵 정렬로 풀어봄
"""

import sys

N = int(sys.stdin.readline())
array = []
for _ in range(N):
    array.append(int(sys.stdin.readline()))


array.sort()
for i in range(N):
    print(array[i])
