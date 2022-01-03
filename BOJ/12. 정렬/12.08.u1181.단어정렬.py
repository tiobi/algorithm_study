"""
# 12. 08. 1181. 단어정렬
# DATE SOLVED: Solving...

# COMMENTS:
    N개의 알파벳 소문자 단어 정렬
    길이가 짧은 것부터, 
    길이가 같으면 사전 순으로 
"""

import sys

N = int(sys.stdin.readline())

words = []
for _ in range(N):
    words.append(str(sys.stdin.readline()))


    