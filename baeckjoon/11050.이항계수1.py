# https://www.acmicpc.net/problem/11050

def factorial(n):
    if n <= 1:
        return 1
    else:
        return n * factorial(n-1)
    
a = [int(x) for x in input().split(" ")]
n = a[0]
k = a[1]

print(int(factorial(n) / (factorial(n-k) * factorial(k))))