def solution(s):
    list = s.split(" ")
    print("초기 분리결과:", list)
    for j in range(len(list)):
        word = list[j]
        #print("이번에는 {}를 수정할 것입니다.".format(word))
        letter = [0 for i in range(len(word))]
        for i in range(len(letter)):
            if i % 2 == 0:
                letter[i] = word[i].upper()
            else:
                letter[i] = word[i].lower()
        list[j] = "".join(letter)
    for i in range(len(list)):
        list[i] = list[i] + " "
    print("list:",list)
    connect = "".join(list)
    connect = connect[:-1]
    print('"{}"'.format(connect))
    return connect

solution('HELLO')
solution('hello my world')
solution(' hello my  world   ')
