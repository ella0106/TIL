def solution(n):
    return sum([int(i) for i in list(str(n))])



# 아래는 재귀구조로 10씩 나누어서 1의 자리수를 계속 더하는 방식이다.
# 진짜,, 똑똑한 듯
def sum_digit(number):
    if number < 10:
        return number;
    return (number % 10) + sum_digit(number // 10) 