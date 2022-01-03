"""
# 12. 08. 1181. 단어정렬
# DATE SOLVED: 22. 01. 03

# COMMENTS:
    N개의 좌표를 압축한 결과 Xi: len(Xi > Xj)
    가장 작은 좌표 Xk = 0
    가장 큰 좌표 Xl = len(X) - (same value)
"""

import sys

N = int(sys.stdin.readline())

coo = list(map(int, sys.stdin.readline().split()))
coo_s = sorted(coo)
d = {}
w = 0

for c in coo_s:
    if c not in d:
        d[c] = w
        w += 1

    else: continue

for i in range(N):
    print(d[coo[i]])