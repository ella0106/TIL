def solution(arr):
    while len(arr)-1:
        arr.remove(min(arr))
        return arr
    return [-1]
