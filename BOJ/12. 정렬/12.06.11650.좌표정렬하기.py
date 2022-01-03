"""
# 12. 06. 11650. 좌표 정렬하기 
# DATE SOLVED: 22. 01. 03

# COMMENTS:
    (x, y)좌표가 주어졌을 때 x -> y 좌표 증가하는 순으로. 
    lambda 함수를 사용하면 쉽게 풀 수 있다. 
    dictionary는 시간초과.
"""

import sys


N = int(sys.stdin.readline())

coo = []

for _ in range(N):
    x, y = map(int, sys.stdin.readline().split())
    coo.append((x, y))

coo.sort(key = lambda xy:(xy[0], xy[1]))

for xy in coo:
    print(xy[0], xy[1])