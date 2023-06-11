# https://school.programmers.co.kr/learn/courses/30/lessons/72413?language=python3
def solution(n, s, a, b, fares):
    # 노드 간 거리 dict 생성
    fare = {}
    for i in range(len(fares)):
        fares.append([fares[i][1],fares[i][0],fares[i][2]])
    for f in fares:
        if f[0] in fare:
            fare[f[0]].update({f[1]:f[2]})
        else:
            fare.update({f[0]:{f[1]:f[2]}})
    
    print(fare)
    # 방문 여부와 거리계산용 list 생성
    INF = 1e8
    
    import heapq
    
    def dijkstra(s):
        dist = [INF] * (n+1)
        q = []
        heapq.heappush(q, (0, s))
        dist[s] = 0
        
        while q:
            d, now = heapq.heappop(q)
            
            if dist[now] < d:
                continue
            
            for i in fare[now]:
                if d+fare[now][i] < dist[i]:
                    dist[i] = d+fare[now][i]
                    heapq.heappush(q, (d+fare[now][i], i))

        return dist
                    
    taxi = [INF] * (n+1)
    for i in fare:
        taxi[i] = dijkstra(i)
    for i in fare:
        cash = taxi[s][i] +taxi[i][a] + taxi[i][b]
        if taxi[0] > cash:
            taxi[0] = cash
    print(taxi)
    answer = taxi[0]
    return answer

solution(6, 4, 6, 2, [[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]])
solution(7, 3, 4, 1, [[5, 7, 9], [4, 6, 4], [3, 6, 1], [3, 2, 3], [2, 1, 6]])
solution(6, 4, 5, 6, [[2,6,6], [6,3,7], [4,6,7], [6,5,11], [2,5,12], [5,3,20], [2,4,8], [4,3,9]])