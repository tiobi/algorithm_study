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

    왼쪽 상단을 기준으로 하면 틀릴 수도 있다. 
    칠해야 하는 체스판을 계산해서 범위를 넘으면 다시 계산.
"""

import sys

def next_square(now):
    if now == 'B':
        return 'W'
    
    return 'B'


def get_minimum_squares_to_fill(board, N, M):
    min_sq_to_fill = N * M  # Set Max 

    for i in range(0, N-7):             # N과 M이 0보다 큰 경우
        for j in range(0, M-7):         # 8 * 8 보드 크기를 정해서 searching

            squares_to_fill = 0         # 이번 8 * 8 보드에서 채워야 하는 square 수 초기화
            now_square = board[i][j]    # 왼쪽 상단 기준

            for a in range(i, i+8):
                for b in range(j, j+8):
                    if a == i and b == j:# 첫 칸 패스
                        pass

                    if now_square == next_square(now_square):       # 지금 칸과 다음 칸이 같으면(안 좋은 뜻)
                        squares_to_fill += 1
                        now_square = next_square

                    else:                                           # 지금 칸과 다음 칸이 다르면(좋은 뜻)
                        now_square = next_square(now_square)

                now_square = next_square(now_square)                # 줄 넘어감

            min_sq_to_fill = min(min_sq_to_fill, squares_to_fill)


    return min_sq_to_fill



board = []

N, M = map(int, sys.stdin.readline().split())
for _ in range(N):
    board.append(sys.stdin.readline())


print(get_minimum_squares_to_fill(board, N, M))