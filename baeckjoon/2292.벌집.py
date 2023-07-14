# https://www.acmicpc.net/problem/2292
a = int(input()) - 1
c = 1
while a > 0:
    a -= c*6
    c += 1

print(c)