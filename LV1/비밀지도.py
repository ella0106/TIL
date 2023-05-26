# https://school.programmers.co.kr/learn/courses/30/lessons/17681
def solution(n, arr1, arr2):
    pwd = []
    for i in range(n):
        num = str(bin(arr1[i] | arr2[i]))[2:]
        num = num.zfill(n)
        num = num.replace('1','#').replace('0',' ')
        pwd.append(num)
    
    return pwd
    
        
            