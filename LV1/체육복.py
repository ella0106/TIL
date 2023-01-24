def solution(n, lost, reserve):
    trim_lost = [i for i in lost if i not in reserve] # 도둑 맞은 학생에게 여유분이 있는 경우
    trim_reserve = [i for i in reserve if i not in lost]
    trim_lost.sort()
    trim_reserve.sort()
    cnt = 0
    for i in trim_lost:
        if i-1 in trim_reserve:
            cnt += 1
            trim_reserve.remove(i-1)
        elif i+1 in trim_reserve:
            cnt += 1
            trim_reserve.remove(i+1)
    return n - len(trim_lost) + cnt



def solution(n, lost, reserve):
    _reserve = [r for r in reserve if r not in lost]
    _lost = [l for l in lost if l not in reserve]
    _reserve.sort()
    _lost.sort()
    for r in _reserve: # 여긴 정렬이 없는데,, 무슨 차이일까
        f = r - 1
        b = r + 1
        if f in _lost: # 얘는 앞의 친구에게 먼저 빌려줄 수 있는지 확인한다
            _lost.remove(f)
        elif b in _lost:
            _lost.remove(b)
    return n - len(_lost)

    # 논리적으로는 앞의 친구에게 먼저 확인하는 게 맞음
    # 결국엔 둘 다 정렬해야함 테스트 케이스가 통과 안됨