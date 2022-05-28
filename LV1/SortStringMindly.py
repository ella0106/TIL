def solution(strings, n):
    return [k for (v,k) in sorted(list(zip([i[n] for i in strings], strings)))]
