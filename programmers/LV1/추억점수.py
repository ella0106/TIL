# https://school.programmers.co.kr/learn/courses/30/lessons/176963
def solution(name, yearning, photo):
    score = dict(zip(name, yearning))
    answer = []
    for i in range(len(photo)):
        total = [score[x] for x in photo[i] if x in name]
        answer.append(sum(total))
    return answer