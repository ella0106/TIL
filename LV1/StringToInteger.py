def solution(s):
    buho = {'+':1, '-':-1}
    if s.split()[0] in buho:
        answer = buho[s.split()[0]] * int(s.split[1:].join)
    else:
        answer = int(s)
    return answer