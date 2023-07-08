#https://www.acmicpc.net/problem/2744

string = input()
answer = []
for i in string:
    if i.isupper():
        answer.append(i.lower())
    else:
        answer.append(i.upper())

print(''.join(answer))