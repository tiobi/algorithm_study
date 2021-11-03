"""
# 10. 02. 10870. 피보나치 수 5
# DATE SOLVED: 21. 11. 02

# COMMENTS:
    0 과 1로 시작하는 피보나치 수열의 N번째 항을 구하는 문제
    0으로 시작하는 피보나치 수열은 근본이 없다.
    재귀로 푸는 피보나치 수열 함수도 근본이 없다.
"""


import sys

def fibo(n):
    # 근본 없는 입력
    if n == 0:
        return 0
    elif n == 1:
        return 1

    # 근본 없는 재귀
    else:
        return fibo(n-1) + fibo(n-2)


n = int(sys.stdin.readline())
print(fibo(n))