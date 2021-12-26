"""
# 12. 05 . 1427. 소트인사이드
# DATE SOLVED: 21. 12. 26

# COMMENTS:
    수가 주어졌을 때 각 자리수를 내림차순 정렬.
    array를 만들어 정렬하고 문자열로 합침
"""

import sys

N = int(sys.stdin.readline())
arr = []

while(1):
    arr.append(N%10)
    N = int(N/10)
    if N <= 0: break

arr.sort(reverse=True)

ans = ''

for i in range(len(arr)):
    ans += str(arr[i])

print(ans)
