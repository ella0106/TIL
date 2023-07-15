def solution(n):
    num = sorted(list(str(n)))
    answer = ''
    for i in range(len(num)):
        answer += num.pop()
    return int(answer)
