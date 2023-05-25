# https://school.programmers.co.kr/learn/courses/30/lessons/142086
def solution(s):
    startidx = 0
    finidx = 0
    q = []
    answer = []
    for i in range(len(s)):
        if s[i] not in q:
            q.append(s[i])
            answer.append(-1)
        else:
            idx = q.index(s[i])
            q[idx] = '0'
            answer.append(len(q) - idx)  
            q.append(s[i])
    return answer

# dictionary로 구성해도 됨