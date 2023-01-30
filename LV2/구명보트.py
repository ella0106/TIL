def solution(people, limit):
    people = list(reversed(sorted(people)))
    left = 0
    right = len(people) - 1
    cnt = 0
    
    while left < right:
        if people[left] + people[right] > limit:
            left += 1
        elif people[left] + people[right] <= limit:
            left += 1
            right -= 1
        cnt += 1
    if left == right:
        cnt += 1
        
    return cnt

print("포인터를 활용해서 어렵게 따로 목록을 나누지 않고 계산을 진행한다.")