# https://school.programmers.co.kr/learn/courses/30/lessons/131705
from itertools import combinations
def solution(number):
    return list(map(sum, list(combinations(number, 3)))).count(0)