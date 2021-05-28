# 백준 사이트 https://www.acmicpc.net/problem/1162
# 해설 사이트 https://dlwnsdud205.tistory.com/104


# C++하면 풀리고 python으로 하면 안풀림
# 문제해설
# 벽뚫고 목적지까지 최단거리를 구하는 문제와 같다
# 나머지는 다익스타를 적용하면 된다

# 알고리즘
# 1. distance를 2차원으로 만든다(도시, 도를 포장한 갯수)
# 2. 우선순위 큐를 만들어서 서울(1)번 부터 N번도시까지 가는 최단거리를 구한다
#   2-1. 포장도로를 안깔았을때 경우를 우선순위큐에 넣어준다
#   2-2. 포장도로를 깔았을때 경우를 우선순위 큐에 넣어준다
#
import heapq
N,M,K = map(int, input().split())
graph = [[] for i in range(N+1)]
for i in range(M):
    a,b,cost = map(int, input().split())
    graph[a].append([b,cost])
    
    graph[b].append([a,cost])

q = []
distance = [[int(1e9)]*(K+1) for _ in range(N+1)]


heapq.heappush(q,[0,[1,0]])

distance[1][0] = 0
ans = int(1e9)

while q:
    nowIdx, [nowTime, nowP] = heapq.heappop(q)
    if nowIdx == N:
        ans = min(ans,nowTime)
    if distance[nowIdx][nowP] <nowTime: continue
    distance[nowIdx][nowP] = nowTime

    
    for ele,road_cost in graph[nowIdx]:
        nextTime = road_cost + nowTime
        if distance[ele][nowP] > nextTime:
            distance[ele][nowP] = nextTime
            heapq.heappush(q,[nextTime,[ele,nowP]])
        if nowP < K and distance[ele][nowP+1] > nowTime:
            distance[ele][nowP+1] = nowTime
            heapq.heappush(q,[nextTime,[ele,nowP+1]])
        

print(ans)