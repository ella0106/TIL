# https://school.programmers.co.kr/learn/courses/30/lessons/147355
def solution(t, p):
    n = len(p)
    num = []
    for i in range(len(t)-n+1):
        num.append(t[i:i+n])
    small = [i for i in num if int(i) <= int(p)]
    answer = len(small)
    return answer