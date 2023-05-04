def solution(s):
    a = s.split(' ')
    b = []
    for num in a:
        b.append(int(num))
    print(b)
    c = []
    c.append(min(b))
    c.append(max(b))
    d = []
    for num in c:
        d.append(str(num))
    answer = ' '.join(d)
    print(d)
    return answer

def solution(s):
    s = list(map(int,s.split()))
    return str(min(s)) + " " + str(max(s))



solution("1 2 3 4")
# return "1 4"
solution("-1 -2 -3 -4")
# "-4 -1"
solution("-1 -1")
# "-1 -1"