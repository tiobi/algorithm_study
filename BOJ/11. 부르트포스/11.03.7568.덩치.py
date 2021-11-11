"""
# 10. 03. 7568. 덩치 
# DATE SOLVED: 21. 11. 05

# COMMENTS:
    어떤 사람이 다른 사람보다 키와 몸무게가 덩 클 때 덩치가 더 크다고 함.
    덩치를 비교할 수 없을 때 등수가 같다. 
    모든 사람의 덩치 등수를 출력. 
    클래스를 지정해서 클래스 만드는 연습. 
"""

from sys import stdin


class Person:
    def __init__(self):
        self.height = 0
        self.weight = 0
        self.rank = 1

    def set_wh(self, weight, height):
        self.weight = weight
        self.height = height


def isBigger(p1, p2):
    if p1.weight > p2.weight and p1.height > p2.height:
        return True

    return False


def isSmaller(p1, p2):
    if p1.weight < p2.weight and p1.height < p2.height:
        return True
    
    return False

def setRank(N, person_list):

    for i in range(N - 1):
        for j in range(i + 1, N):
            if isSmaller(person_list[i], person_list[j]):
                person_list[i].rank += 1

            if isBigger(person_list[i], person_list[j]):
                person_list[j].rank += 1

    return person_list

person_list = []
N = int(stdin.readline())

for _ in range(N):
    new_person = Person()
    x, y = map(int, stdin.readline().split())
    new_person.set_wh(x, y)
    person_list.append(new_person)

person_list_ranked = setRank(N, person_list)

for i in range(N):
    print(person_list_ranked[i].rank)
