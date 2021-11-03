"""
# 10. 4. 11729. 하노이 탑 이동 순서
# DATE SOLVED: 211103

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

print(2**N - 1)
hanoi(N, 1, 3, 2)