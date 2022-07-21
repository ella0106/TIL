def solution(s):
    pcnt, ycnt = 0, 0
    for i in s.lower():
        if i == 'p' : pcnt += 1
        if i == 'y' : ycnt += 1

    return pcnt == ycnt