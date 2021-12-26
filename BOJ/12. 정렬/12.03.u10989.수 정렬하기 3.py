"""
# 12. 03. 10989. 수 정렬하기 3
# DATE SOLVED: 21. 11. 14

# COMMENTS:
    N 개의 수를 오름차순으로 정렬.
    수의 범위가 작다면 카운팅 정렬을 사용.
     
"""

import sys

N = int(sys.stdin.readline())
array = []
for _ in range(N):
    array.append(int(sys.stdin.readline()))


array.sort()
for i in range(N):
    print(array[i])
