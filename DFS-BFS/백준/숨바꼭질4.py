from collections import deque
n, k = map(int, input().split())
visited = [False]*100001
d = [1,-1]
road=[]
def bfs():
    q = deque()
    q.append((0,n))
    while q:
        cost, now = q. popleft() 
        visited[now] = True
        
        if now == k:
            return cost
        for i in range(2):
            next_pos = now + d[i]
            if 0 <= next_pos <= 100000 and visited[next_pos] == False:
                q.append((cost+1,next_pos))
                road.append((now,next_pos))
        next_pos = now*2
        if 0 <= next_pos <= 100000 and visited[next_pos] == False:
                q.append((cost+1,next_pos))
                road.append((now,next_pos))
    
if n<=k:
    print(bfs())
    find = k
    ans = []
    while True:
        ans.append(find)
        if find == n:
            break
        for i in range(len(road)):
            if road[i][1] == find:
                find = road[i][0]
                #flag = True
                break
        
    for i in range(len(ans)-1,-1,-1):
        print(ans[i], end = " ")
else:
    print(n-k)
    for i in range(n,k-1,-1):
        print(i,end = " ")