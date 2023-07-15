# https://school.programmers.co.kr/learn/courses/30/lessons/86491
def solution(sizes):
    maxes = [max(i) for i in sizes]
    mins = [min(i) for i in sizes]
    answer = max(maxes) * max(mins)
    return answer