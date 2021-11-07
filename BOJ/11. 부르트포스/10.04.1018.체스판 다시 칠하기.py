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

    부르트포스를 적용하면 O(N^4)
"""

import sys

def next_square(now):
    if now == 'B':
        return 'W'
    
    return 'B'


def squares_to_fill(board, N, M):

    min_fills = N*M
    for a in range(0, N-7):
        for b in range(0, M-7):
            fills = 0
            now_square = board[a][b]
            
            # 보드  탐색 시작. 
            for i in range(a, 8+a):
                for j in range(b, 8+b):
                    if i == a and j == b: continue

                    # 지금 칸이랑 다음 칸이랑 
                    # 다른 경우(좋은 뜻)
                    elif now_square != board[i][j]:
                        now_square = next_square(now_square)
                        pass
                    
                    # 같은 경우(안 좋은 뜻)
                    else:
                        fills += 1                              # 다시 칠하는 칸 + 1      
                        now_square = next_square(now_square)

                #한 줄 넘어감
                now_square = next_square(now_square)

            # 탐색 끝
            min_fills = min(fills, min_fills)

    return min_fills


def minimum_squares_to_fill(board, col, row):
    # 최소값
    min_fills = col*row                  
    for i in (col - 8):
        for j in (row - 8):
            min = min(min, squares_to_fill(board[i][j]))


    return min_fills


board = []

N, M = map(int, sys.stdin.readline().split())
for _ in range(N):
    board.append(sys.stdin.readline())

print(squares_to_fill(board, N, M))