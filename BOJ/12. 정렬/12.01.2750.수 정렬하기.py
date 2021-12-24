"""
# 11. 01. 2750. 수 정렬하기 
# DATE SOLVED: Solving...

# COMMENTS:
    N개 입력, 오름차순 정렬.
    O(N^2)으로 풀어도 된다.
    따라서 삽입정렬로 풀겠다. Best case O(N)
"""

import sys

def insertionSort(array):
    for i in range(1, len(array)):
        for j in range(i, 0, -1):
            if array[j - 1] > array[j]:
                array[j], array[j -1] = array[j - 1], array[j]


N = int(sys.stdin.readline())
array = []

for _ in range(N):
    buf = int(sys.stdin.readline())
    array.append(buf)

insertionSort(array)

for i in range(len(array)):
    print(array[i])
