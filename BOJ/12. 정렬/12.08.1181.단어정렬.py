"""
# 12. 08. 1181. 단어정렬
# DATE SOLVED: 22. 01 03

# COMMENTS:
    N개의 알파벳 소문자 단어 정렬
    길이가 짧은 것부터, 
    길이가 같으면 사전 순으로 
    여러 번 입력은 한 번씩만 출력한다.
"""

import sys

N = int(sys.stdin.readline())

words = []
for _ in range(N):
    words.append(str(sys.stdin.readline().strip()))


words.sort()
words.sort(key = len)

words_no_duplicats = []

for i in words:
    if i not in words_no_duplicats:
        words_no_duplicats.append(i)
        print(i)