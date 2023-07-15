def solution(clothes):
    kind = set([i[1] for i in clothes])
    closet = dict.fromkeys(kind, 0)
    for cloth in clothes:
        closet[cloth[1]] += 1
    
    n = 1
    for i in closet.values():
        n *= i+1
    
    return n-1

print("경우의 수를 구하는 식을 왜 생각하지 못했나.. 역시 확통을 열심히 하지 않은 티가 났네. 해시는 dict를 사용한 것으로 충분했던 것 같다.")