def solution(x):
    num = list(str(x))
    hap = sum(map(lambda x : int(x), num))
    return True if x % hap == 0 else False

print(solution(10))
print(solution(11))
print(solution(12))
print(solution(13))
