"""
# 14. 01. 15649. N과 M 1
# DATE SOLVED: Solving...

# COMMENTS:
    1부터 N까지 자연수 중에서 중복 없이 M개를 고른 수열
"""

import sys
from collections import deque

M, N = map(int, sys.stdin.readline().split())

box = [[0] * M for _ in range(N)]
visited = [[0] * M for _ in range(N)]

for i in range(N):
    l = list(map(int, sys.stdin.readline().split()))
    for j, k in enumerate(l):
        box[i][j] = k

q = deque()

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for i in range(N):
    for j in range(M):
        if box[i][j] == 1:
            q.append((i, j))


while q:
    x, y = q.popleft()

    if visited[x][y] == 0: 
        visited[x][y] = 1

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if 0 <= nx < N and 0 <= ny < M:
                if visited[nx][ny] == 0 and box[nx][ny] == 0:
                    box[nx][ny] = box[x][y] + 1
                    q.append((nx, ny))

isZero = False

for i in range(N):
    if 0 in box[i]:
        isZero = True
        break

if isZero: print("-1")
else:
    