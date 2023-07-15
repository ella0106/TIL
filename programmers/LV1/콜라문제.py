# https://school.programmers.co.kr/learn/courses/30/lessons/132267
def solution(a, b, n):
    cnt = 0
    while n >= a:
        cnt += (n//a)*b
        n = n % a + (n//a)*b
    answer = cnt
    return answer

# solution = lambda a, b, n: max(n - b, 0) // (a - b) * b
# 병을 주고 받는 과정을 하나로 합쳐서 n - b 개의 병을 소비하는 것으로 생각의 전환
