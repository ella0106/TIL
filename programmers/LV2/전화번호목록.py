def solution(phone_book):
    p_hash = [[],[],[],[],[],[],[],[],[],[]]
    for num in sorted(phone_book):
        p_hash[int(num[0])].append(num)
    for p in p_hash:
        if len(p) > 1:
            for i in range(len(p)-1):
                min_num = min(p[i], p[i+1])
                min_len = len(min_num)
                if p[i][0:min_len] == p[i+1][0:min_len]:
                    return False      
                
    return True

    print("내가 만든 기존의 해시테이블이랑 각 옆에것을 비교해서 뛰어넘는 로직까지 추가하니 효율성이 완전히 잡혔음!")


def solution(phone_book):
    answer = True
    hash_map = {}
    for phone_number in phone_book:
        hash_map[phone_number] = 1
    for phone_number in phone_book:
        temp = ""
        for number in phone_number:
            temp += number
            if temp in hash_map and temp != phone_number:
                answer = False
    return answer

print("이게 정석 해시 풀이인듯..ㅠㅡㅜ")