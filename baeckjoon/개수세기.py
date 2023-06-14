n = int(input())
nums = [int(n) for n in input().split(" ")]
a = int(input())
cnt = 0
for i in nums:
    if a == i:
        cnt += 1

print(cnt)