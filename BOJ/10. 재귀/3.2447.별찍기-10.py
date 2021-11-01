# 10. 3. 2447. 별찍기 
# 재귀 함수로 별을 찍어보는 것. 
# 3의 거듭제곱 형태의 입력. 재귀 함수 사용


import sys, math

# 블랭크 찍는 함수
def printBlank(k):
    # 재귀 함수 처리용
    n = int(math.log(k, 3))

    # 베이스
    if n == 1:
        print("   ")
        print("   ")
        print("   ")

    # 재귀함수 호출
    else:
        print(printBlank(n-1) + printBlank(n-1) + printBlank(n-1))


# 별 찍는 함수
def printStar(k):
    # 재귀 함수 처리용
    n = int(math.log(k, 3))

    # 베이스
    if n == 1:
        print("***")
        print("* *")
        print("***")

    # 재귀함수 호출
    else:
        print(printStar(n-1) + printStar(n-1) + printStar(n-1))
        print(printStar(n-1) + printBlank(n-1) + printStar(n-1))
        print(printStar(n-1) + printStar(n-1) + printStar(n-1))


N = int(sys.stdin.readline())
printStar(N)