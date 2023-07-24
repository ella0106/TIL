# https://www.acmicpc.net/problem/4153
while True:
    a  = [int(x) for x in input().split(' ')]
    a.sort()
    if a[0] == 0:
        break
    elif a[0]**2 + a[1]**2 == a[2]**2:
        print('right')
    else:
        print('wrong')
