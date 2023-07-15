def solution(numbers, target):
    answer = 0
    leaves = [0]
    for num in numbers:
        tmp = []
        for leaf in leaves:
            tmp.append(leaf + num)
            tmp.append(leaf - num)
        leaves = tmp
    
    for leaf in leaves:
        if leaf == target:
            answer += 1
    return answer

print("아니 BFS를 어떻게 구현해?!?! 라고 생각하고 있다가")
print("그치,, 굳이 트리 형태로 구현할 필요는 없지 라고 풀이를 보고 깨달았다.")
print("아 너무 어렵다. 나는 이걸 이렇게 타파할 수 있는 것일까?")