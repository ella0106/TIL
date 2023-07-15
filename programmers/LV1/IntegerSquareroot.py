def solution(n):
    from math import sqrt
    return (sqrt(n)+1)**2 if sqrt(n) == int(sqrt(n)) else -1
