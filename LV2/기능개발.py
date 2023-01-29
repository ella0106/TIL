def solution(progresses, speeds):
    finish = []
    for i in range(len(progresses)):
        cnt = 0
        while progresses[i] < 100:
            progresses[i] += speeds[i]
            cnt += 1
        finish.append(cnt)
    #print(finish)
    deploy = [finish.pop(0)]
    answer = []
    #print(deploy)
    while len(finish):
        if deploy[0] >= finish[0]:
            deploy.append(finish.pop(0))
        else:
            answer.append(len(deploy))
            deploy = [finish.pop(0)]

        #print(answer)
    answer.append(len(deploy))
    #print(answer)
    return answer

solution([95, 90, 99, 99, 80, 99],[1, 1, 1, 1, 1, 1])