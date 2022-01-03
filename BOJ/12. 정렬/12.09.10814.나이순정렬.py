"""
# 12. 09. 10814. 나이순 정렬
# DATE SOLVED: 22. 01. 03

# COMMENTS:
    나이와 이름순으로 정렬
"""

import sys

N = int(sys.stdin.readline())

members = []

for _ in range(N):
    age, name = map(str, sys.stdin.readline().split())
    age = int(age)
    members.append((age, name))

members.sort(key = lambda x: x[0])

for x in members:
    print(x[0], x[1])