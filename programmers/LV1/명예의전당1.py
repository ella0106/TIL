# https://school.programmers.co.kr/learn/courses/30/lessons/138477
def solution(k, score):
    q = []
    answer = []
    for i in range(len(score)):
        q.append(score[i])
        q = list(reversed(sorted(q)))
        if i >= k:
            q = q[:k]
        answer.append(min(q))
    return answer