def solution(answers):
    score = {x:0 for x in [1,2,3]}
    one = [1,2,3,4,5]
    two = [2,1,2,3,2,4,2,5]
    three = [3,3,1,1,2,2,4,4,5,5]

    for i in range(len(answers)):
        if answers[i] == one[i%5]: score[1] += 1
        if answers[i] == two[i%8]: score[2] += 1
        if answers[i] == three[i%10]: score[3] += 1

    answer = [key for key, val in score.items() if val == max(score.values())]
    return answer


#answers = [1,2,3,4,5]
#[1]
#answers = [1,3,2,4,2]
#[1,2,3]

#solution(answers)
