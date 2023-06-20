num = ''.join(input()).split(" ")
num = [int(n) for n in num]
answer = abs(num[0] - num[1])
print(answer)