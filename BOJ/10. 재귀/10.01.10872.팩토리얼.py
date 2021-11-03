"""
# 10. 01. 10872. 팩토리얼
# DATE SOLVED: 21. 11. 02

# COMMENTS:
    0보다 크거나 같은 정수 N에 대해 N!를 출력하는 프로그랜을 작성. 
    문제 풀이 조건은 재귀 함수를 사용하는 것이므로
    함수를 define 하는 것이 포인트.
"""


import sys

#팩토리얼 함수 정의
def factorial(n):
    # 팩토리얼을 재귀함수로 사용하기 위해 0과 1은 예외처리 
    # 팩토리얼 정의에 따라 0! = 1. 왜그런지몰름
    if n == 0:
        return 1
    elif n == 1:
        return 1
    
    #N이 1과 2가 아닌 경우, 재귀함수 형식으로 반환.
    else:
        return n * factorial(n-1) 


N = int(sys.stdin.readline())
print(factorial(N))