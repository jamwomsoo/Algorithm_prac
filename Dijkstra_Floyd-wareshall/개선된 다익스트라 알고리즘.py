#시간복잡도
#V-> 노드의 개수, E-> 간선의 개수
#O(E*logV)
#우선순위 큐를 사용하여 삽입시 O(logN), 삭제시O(logN)걸림
#우선순위 큐를 사용으로 최소값을 갖는 간선을 따로 안 찾아줘도 된다
import heapq
import sys
input = sys.stdin.readline
INF =int(1e9)

n, m =map(int, input().split())
start = int(input())
graph= [[] for i in range(n+1)]
distance = [INF] * (n+1)

for _ in range(m):
    #노드 a와 노드 b로 가는 비용 c
    a, b, c = map(int, input().split())
    graph[a].append((b,c))

def djikstra(strat):
    q = []
    headq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist +i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q,(cost, i[0]))

djikstra(start)

for i in range(1, n+1):
    if distance[i] == INF:
        print("INFINITY")
    else:
        print(distance[i])