def solution(s):
    stack = []
    for string in s:
        if string == "(":
            stack.append(string)
        if string == ")":
            if len(stack) == 0:
                return False
            stack.pop()
    if len(stack) == 0:
        return True
    return False