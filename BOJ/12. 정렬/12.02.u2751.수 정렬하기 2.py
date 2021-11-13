"""
# 12. 02. 2571. 수 정렬하기 2
# DATE SOLVED: 21. 11. 14

# COMMENTS:
    N 개의 수를 오름차순으로 정렬.
    O(nlogn)으로 풀어야 하는 문제. 
    내장함수 이용하래서 내장함수 씀.
"""
import sys

N = int(sys.stdin.readline())
array = []
for _ in range(N):
    array.append(int(sys.stdin.readline()))


array.sort()
for i in range(N):
    print(array[i])
