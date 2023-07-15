def solution(k, m, score):
    score = list(reversed(sorted(score)))
    answer = 0
    for i in range(len(score)):
        if i % m == m-1:
            answer += score[i]*m
    return answer