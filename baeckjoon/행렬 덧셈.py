nm = [int(n) for n in input().split(" ")]
A = []

for i in range(nm[0]*2):
    A.extend([int(n) for n in input().split(" ")])

C = [str(a+b) for a, b in zip(A[:nm[0]*nm[1]],A[nm[0]*nm[1]:])]

for i in range(nm[0]):
    print(' '.join(C[:nm[1]]))
    del C[:nm[1]]
