"""
# 10. 02. 2231. 분해합
# DATE SOLVED: 21. 12. 24

# COMMENTS: 
    어떤 자연수 N의 분해합은 N과 N을 이루는 각 자리수의 합이다.
    어떤 자연수 M의 분해합이 N이면 M을 N의 생성자라고 한다.
    자연수 N의 가장 작은 생성자를 구하라.
"""

from sys import stdin

"""
192 = 192 + 12 = 204 = 210 = 

"""

def generator(N):
    minGen = float('inf')

    for i in range(N):
        buf = sum(map(int, str(i)))
        minGen = i + buf

        if minGen == N:
            return i

    return 0
    pass

N = int(stdin.readline())
print(generator(N))