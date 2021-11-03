# 11. 1. 2798. 블랙잭
# N장의 카드 중에서 세 장을 골라 M을 넘지 않으면서 M과 최대한 가까운 수
#모든 경우의 수를 고려하는 부르트포스 기법 사용

import sys


N, M = map(int, sys.stdin.readline().split())
