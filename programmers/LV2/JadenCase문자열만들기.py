def solution(s):
    numbers = ['0','1','2','3','4','5','6','7','8','9']
    a = s.lower().split(' ')
    for i in range(len(a)):
        if a[i] != '':
            if a[i][0] not in numbers:
                a[i] = a[i].capitalize()
    
    print(a)
    answer = ' '.join(a)
    print(answer)
    return answer

solution("   hi 4Weeks WAs   happier  I think  ")
# "   Hi 4weeks Was   Happier  I Think  "