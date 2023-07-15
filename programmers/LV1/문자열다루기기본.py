"""
문제 설명

문자열 s의 길이가 4 혹은 6이고,
숫자로만 구성돼있는지 확인해주는 함수,
solution을 완성하세요.
예를 들어 s가 "a234"이면 False를 리턴하고
"1234"라면 True를 리턴하면 됩니다.

제한 사항

s는 길이 1 이상, 길이 8 이하인 문자열입니다.

입출력 예

s	return
"a234"	false
"1234"	true

"""

def solution(s):
    if len(s) == 4 or len(s)==6: # len 점검도 한 번이면 충분하다
        for i in s.split(): # try-except를 사용할꺼면 사실 for문을 안 써도 된다
            try:
                int(i)
            except:
                return False
        return True
    else: return False


print(solution("a234"))
print(solution('1234'))

def solution(s):
    if len(s) in [4,6]:
        try: int(i)
        except: return False
        return True
    else : return False