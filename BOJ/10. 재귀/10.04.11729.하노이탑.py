"""
# 10. 04. 11729. 하노이 탑 이동 순서
# DATE SOLVED: 21. 11. 03

# COMMENTS:
    재귀적으로 하노이 탑 문제를 풀어야 한다.
    하노이 탑의 이전 단계를 하나의 덩어리라고 생각하면 쉽다.
"""
import sys

def hanoi(n, _from, to, aux):
    global K
    if n == 1:
        print(_from, to)
        return

    hanoi(n-1, _from, aux, to)
    print(_from, to)
    hanoi(n-1, aux, to, _from)


N = int(sys.stdin.readline())   # 원판의 개수

#N개의 원판을 전부 이동시키면 최소 2^N - 1 번으 ㅣ이동 횟수가 필요하다.
print(2**N - 1)                 #이동 횟수
hanoi(N, 1, 3, 2)