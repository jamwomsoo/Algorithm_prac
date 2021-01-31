# 범위가 10억인 문제
# 출발지와 목적지를 최대 무게를 이진 탐색으로 옮겨가며 최적의 해를 구하는 문제이다
# 해당 무게를 bfs함수에 보내서 보내진 무게가 다리의 최대 무게보다 작거나 같으면 해당 무게를 옮길 수 있다는 뜻
# BFS를 사용하는 이유는 목적지에서 출발지로 가는 길이 있는지 확인하는 차원이다
# -> 싣고 가는 무게가 다리의 최대 수용량보다 크면 이동할 수 있는 다리가 없기 불가하기 때문이다 
from collections import deque
n, m =map(int, input().split())
graph= [[] for _ in range(n+1)]
for i in range(m):
    a,b,c = map(int, input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))

start, end = map(int, input().split())

def bfs(weight):
    global start,end
    q = deque()
    q.append(start)
    visited = set()
    visited.add(start)
    while q:
        now = q.popleft()
        for next_pos, limit_weight in graph[now]:
            if next_pos not in visited and limit_weight >= weight:
                q.append(next_pos)
                visited.add(next_pos)
    if end in visited:
        return True
    else:
        return False
left = 1
right = 1000000000
ans = 1
while left <= right:
    mid = (left + right)//2
    if bfs(mid):
        ans = mid
        left = mid + 1
    else:
        right = mid - 1
print(ans)

