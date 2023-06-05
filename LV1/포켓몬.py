# https://school.programmers.co.kr/learn/courses/30/lessons/1845
def solution(nums):
    cnt = len(nums) / 2
    kind = len(list(set(nums)))
    answer = min(cnt, kind)
    return answer