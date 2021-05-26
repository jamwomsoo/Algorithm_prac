# 틀림
# 아이디어 핵심은 g,h 사이의 경로가 존재할때 해당경로를 0.1을 빼주어 float으로 만드는 것이다
# -> 그러면 g,h를 거치지 않고도 같은 최단 거리가 나올시 오답이 나올 수 있다
# -> 하지만 0.1을 빼줌으로써 최단 거리가 같은 것이 나올 가능성을 없애고 최종에서도 flaot인 최단 경로를 갖는 것들만
#    정답(최종 목적지))에 넣으면 된다
import heapq
import sys
from copy import deepcopy
for i in range(int(input())):
    n,m,t = map(int, input().split())
    s,g,h = map(int, input().split())
    graph = [[] for i in range(n+1)]
    distance = [int(sys.maxsize)]*(n+1)
    road_arr = [[] for i in range(n+1)]
    distance[0] = 0
    distance[s] = 0

    for i in range(m):
        a,b,d = map(int, input().split())
        if {a,b} == {g,h}: d -= 0.1
        graph[a].append([b,d])
        graph[b].append([a,d])
            
    goal_list = [int(input()) for _ in range(t)]
    goal_list.sort()
    q = []
    heapq.heappush(q,[0,s])

    while q:
        dis, now= heapq.heappop(q)
        if distance[now] <dis:
            continue
        for spot, c in graph[now]:
            cost = dis + c
            if distance[spot] > cost: 
                heapq.heappush(q,[cost,spot])
                distance[spot] = cost
               
    ans = []
    # print(road_arr)
    # print(distance)
    for spot in goal_list:
        if distance[spot] != int(sys.maxsize) and type(distance[spot]) == float:
            ans.append(spot)
    
    print(*ans)

                