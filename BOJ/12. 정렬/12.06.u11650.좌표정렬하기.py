"""
# 12. 06. 11650. 좌표 정렬하기 
# DATE SOLVED: Solving...

# COMMENTS:
    (x, y)좌표가 주어졌을 때 x -> y 좌표 증가하는 순으로. 
"""

import sys


N = int(sys.stdin.readline())

coordinates = []

for _ in range(len(N)):
    a, b = map(int, sys.stdin.readline().split())
    coordinates.append((a, b))

print(coordinates)