def solution(s):
    return s[int(len(s)/2)] if len(s)%2 == 1 else s[int(len(s)/2)-1 : int(len(s)/2)+1]


def solution(s):
    if len(s)%2 == 1:
        return s[int(len(s)/2)]
    else:
        print(s[1:3])
        return s[int(len(s)/2)-1 : int(len(s)/2)+1]

'''solution("abcde")
solution("word")
'''
