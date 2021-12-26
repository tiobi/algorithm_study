"""
# 12. 03. 10989. 수 정렬하기 3
# DATE SOLVED: 21. 11. 14

# COMMENTS:
    N 개의 수를 오름차순으로 정렬.
    O(nlogn)으로 풀어야 하는 문제. 
    카운팅 정렬을 사용해봄. 
"""

import sys 

N = int(sys.stdin.readline())

input_arr = []
for _ in range(N):
    input_arr.append(int(sys.stdin.readline()))

max_num = max(input_arr)
counting_arr = [0] * max_num

# adding up counts
for i in range(0, len(input_arr)):
    counting_arr[input_arr[i] - 1] += 1

for i in range(1, max_num):
    counting_arr[i] = counting_arr[i - 1] + counting_arr[i]

sorted_arr = [0] * max_num
for i in range(0, max_num):
    sorted_arr[counting_arr[input_arr[i] - 1] - 1] = input_arr[i]
    counting_arr[input_arr[i] - 1] -= 1

print(sorted_arr)

