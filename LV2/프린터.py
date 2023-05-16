def solution(priorities, location):
    n = len(priorities)
    pointer = 0
    maxnum = max(priorities)
    while True:
        if priorities[pointer] == maxnum:
            if pointer == location:
                return len([x for x in priorities if x==0]) + 1
            priorities[pointer] = 0
            maxnum = max(priorities)
        pointer = (pointer + 1) % n
        
    answer = 0
    return answer

print("근데 이것보다는 효율적인 방법이 있을 것 같은데... 하지만 이게 최선이 맞는 것 같다.")