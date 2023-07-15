# https://school.programmers.co.kr/learn/courses/30/lessons/12977

def solution(nums):
    from itertools import combinations
    n = list(combinations(nums,3))
    answer = 0
    for i in n:
        i = sum(i)
        flag = True
        for j in range(2, i) :
            if i % j == 0 :
                flag = False
                break
        if flag == True :
            answer += 1
    return answer