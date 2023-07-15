def solution(d, budget):
    d.sort()
    sum = 0
    for i in range(len(d)):
        sum += d[i]
        if sum > budget:
            return i
        if sum == budget:
            return i+1
    if sum < budget:
        return len(d)