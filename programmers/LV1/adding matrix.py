def solution(arr1, arr2):
    for idx, n in enumerate(arr1):
        for i in range(len(n)):
            n[i] += arr2[idx][i]
    return arr1
