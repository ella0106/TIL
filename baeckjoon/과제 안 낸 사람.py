a = [i+1 for i in range(30)]
num = []
for i in range(28):
    num.append(int(input()))

for i in num:
    a.remove(i)

a = sorted(a)
for i in a:
    print(i)