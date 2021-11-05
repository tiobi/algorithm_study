"""
# 10. 04. 1018. 체스판 다시 칠하기 
# DATE SOLVED: Solving...

# COMMENTS:
    M*N 크기의 보드를 잘라서 8*8 크기의 체스판으로 만들 때
    다시 칠해야 하는 사각형의 최소 개수
    #@##
    @#@#
    #@@@  -> 다시 칠해야 하는 사각형 2개
    @#@#
"""

import sys



board = []

N, M = map(int, sys.stdin.readline().split())
for _ in range(N):
    board.append(sys.stdin.readline())

for i in range(N):
    print(board[i][1])