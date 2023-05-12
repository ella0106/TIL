def solution(n, m):
    answer = [1, 0]
    while True:
        for i in range(min(n,m),0, -1):
            print(i)
            if i == 1:
                break
            if n%i==0 and m%i==0:
                answer[0] *= i
                n = n//i
                m = m//i
                print(i, n, m)
                continue
        break

    answer[1] = n*m*answer[0]


    return answer
