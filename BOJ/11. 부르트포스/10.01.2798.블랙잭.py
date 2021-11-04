"""
# 11. 01 2798. 블랙잭
# DATE SOLVED: 21. 11. 05

# COMMENTS:
    N장의 카드 중에서 세 장을 골라 M을 넘지 않으면서 M과 최대한 가까운 수
    즉, M보다 크지 않은 수 중에 가장 큰 수를 골라야 한다.
    모든 경우의 수를 고려하는 부르트포스 기법 사용.
    비용이 증가하지만, it works
"""


import sys

# 모든 경우의 수 고려
def blackJack(num_of_cards, sum_limit, list_of_cards):
    # 세 개의 카드 선택
    # [v][v][v][ ][ ] iter 1
    # [v][v][ ][v][ ] iter 2
    # [v][v][ ][ ][v] iter 3...

    # sum limit과 최대한 가까운 수
    max_sum = 0

    for i in range(num_of_cards):
        for j in range(i+1, num_of_cards):
            for k in range(i+2, num_of_cards):
                sum = list_of_cards[i] + list_of_cards[j] + list_of_cards[k]    # 세 카드의 합이
                if sum <= sum_limit and sum > max_sum:                          # limit보다 작고 max sum보다 크다면
                    max_sum = sum                                               # 새로운 max sum 저장

    return max_sum


N, M = map(int, sys.stdin.readline().split())
cards = list(map(int, sys.stdin.readline().split()))

print(blackJack(N, M, cards))