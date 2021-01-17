#from collections import deque
import heapq
import sys
input = sys.stdin.readline
t = int(input())
result = [0]*t
for index in range(t):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    q = []#deque()
    heapq.heappush(q,(arr[0][0],0,0))
    #q.append((arr[0][0],0,0))
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    distance = [[int(1e9)]*(n+1) for _ in range(n+1)]
    distance[0][0] = arr[0][0]
    while q:
        cost,x,y = heapq.heappop(q)
        if distance[x][y]<cost:
            continue 
        for i in range(4):
            xn = x+dx[i]
            yn = y + dy[i]
            if 0<=xn< n and 0<=yn<n:
                tmp_cost = arr[xn][yn]+cost
                if distance[xn][yn] > tmp_cost:
                    distance[xn][yn] = tmp_cost
                    heapq.heappush(q,(tmp_cost,xn,yn))
                    #q.append((tmp_cost,xn,yn))
    
    result[index] = distance[n-1][n-1]
for i in range(t):
    print(result[i])


