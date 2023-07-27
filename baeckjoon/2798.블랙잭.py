# https://www.acmicpc.net/problem/2798
cond = [int(x) for x in input().split(" ")]
num = [int(x) for x in input().split(" ")]

for i in range(cond[0]):
    for j in range(i+1, cond[0]):
        for k in range(j+1, cond[0]):
            total = sum([num[i], num[j], num[k]])
            if total > cond[1]:
                continue
            else:
                result = total

print(result)
