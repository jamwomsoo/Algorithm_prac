from collections import deque
f,s,g,u,d = map(int,input().split())
visited = [False]*(f+1)
q = deque()
q.append([0,s])
visited[s] = True
while q:
    cost, now = q.popleft()
    if now == g:
        print(cost)
        exit()
    if now+u <= f and visited[now+u]==False: 
        q.append([cost+1,now+u])
        visited[now+u] = True
    if 1<=now-d and visited[now-d]==False: 
        q.append([cost+1,now-d])
        visited[now-d] = True
print("use the stairs")