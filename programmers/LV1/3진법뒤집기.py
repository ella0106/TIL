def solution(n):
    answer = 0
    rest = []
    while n >= 3:
        rest.append(n % 3)
        n = n // 3
    rest.append(n)
    rest.reverse()
    for i in range(len(rest)):
        answer += (3 ** i) * rest[i]
    print(answer)
    return answer

solution(45)
solution(125)