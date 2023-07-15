def solution(lottos, win_nums):
    num_list = list(set(lottos))
    if 0 in num_list:
        num_list.pop(0)
    count = 0
    for i in lottos:
        if i in win_nums:
            count += 1
    place = [6, 6, 5, 4, 3, 2, 1]
    answer = [place[count+6-len(num_list)], place[count]]
    return answer
