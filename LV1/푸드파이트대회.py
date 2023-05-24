# https://school.programmers.co.kr/learn/courses/30/lessons/134240
def solution(food):
    answer = []
    for i in range(len(food)):
        answer.append(food[i]//2 * str(i))
    answer = ''.join(answer) + '0' + ''.join(reversed(answer))
    return answer