"""
# 10. 05. 1436. 영화감독 숌
# DATE SOLVED: 21. 11. 1l

# COMMENTS:
    666이 들어가는 숫자를 작은 순서대로 찾는 문제
    모든 수를 보고 풀면 된다.
"""

import sys 

def nthTitle(n):
    nth = 0     # n번째로 666이 들어간 수
    title = 0

    # 모든 경우 탐색 시작
    while(True):

        # 타이틀에 666이 있으면
        if '666' in str(title):
            # 몇 번째인지 업데이트
            nth += 1

        # n 번째면 반환
        if nth == n:
            break

        title += 1

    return title



N = int(sys.stdin.readline())
print(nthTitle(N))