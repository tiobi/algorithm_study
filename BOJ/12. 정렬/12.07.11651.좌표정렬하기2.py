"""
# 12. 07. 11651. 좌표정렬하기
# DATE SOLVED: 22. 01. 03

# COMMENTS:
    y좌표가 증가하는 순, y좌표가 같으면 x좌표가 증가하는 순
"""

import sys

N = int(sys.stdin.readline())

coo = []

for _ in range(N):
    x, y = map(int, sys.stdin.readline().split())
    coo.append((x, y))

coo.sort(key = lambda xy:(xy[1], xy[0]))

for xy in coo:
    print(xy[0], xy[1])