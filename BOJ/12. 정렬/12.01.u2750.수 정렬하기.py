"""
# 11. 01. 2750. 수 정렬하기 
# DATE SOLVED: Solving...

# COMMENTS:
    N개 입력, 오름차순 정렬.
    O(N^2)으로 풀어도 된다.
    따라서 삽입정렬로 풀겠다. Best case O(N)
"""

import sys


def insertion_sort(arr):
    for i in range(1, len(arr)):
        for j in range(i, 0, -1):
            if arr[i - 1] > arr[i]:
                arr[i - 1], arr[i] = arr[i], arr[i - 1]

    return arr

N = int(sys.stdin.readline())
a = []

for i in range(N):
    a.append(int(sys.stdin.readline()))

sorted_array = insertion_sort(a)


for i in range(N):
    print(sorted_array[i])