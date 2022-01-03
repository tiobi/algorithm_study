"""
# 12. 04. 2108. 통계학
# DATE SOLVED: Solving...

# COMMENTS:
    홀수인 자연수 N이 주어졌을 때 산술평균, 중앙, 최빈, 범위 구하기
"""

import sys

N = int(sys.stdin.readline())

arr = []

for _ in range(N):
    arr.append(int(sys.stdin.readline()))

arr.sort()

print()