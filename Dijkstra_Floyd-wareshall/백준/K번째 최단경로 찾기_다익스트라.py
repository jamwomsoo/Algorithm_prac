# 백준 사이트 : https://www.acmicpc.net/problem/1854
# 참고 사이트 : https://postbarca.tistory.com/29

# dp를 사용해서 [도시번호][1~k번호까지 각각의 최단경로]


from heapq import heappop, heappush


n,m,k = map(int, input().split())
dp = [[int(1e9)]*k for _ in range(n+1)]
con = [[] for _ in range(n+1)]
for _ in range(m):
    a,b,c = map(int, input().split())
    con[a].append((b,c))
q = []

heappush(q,(0,1))
dp[1][0] = 0
while q:
    dist,now = heappop(q)
    for nex, c in con[now]:
        cost = c+dist
        if dp[nex][k-1] > cost:
            dp[nex][k-1] = cost
            dp[nex].sort()
            heappush(q,(cost,nex))

for i in range(1,n+1):

    print(-1 if dp[i][k-1] == int(1e9) else dp[i][k-1] ) 



# 내풀이

# import heapq
# n,m,k = map(int ,input().split())
# board = [[] for _ in range(n+1)]
# for _ in range(m):
#     a,b,c = map(int, input().split())
#     board[a].append([b,c])
# distance = [[] for _ in range(n+1)]

# q = []
# heapq.heappush(q,[0,1])



# while q:
#     dist,now = heapq.heappop(q)
   
#     if len(distance[now]) >k: continue

#     for next_location, c in board[now]:
#         cost = c + dist
#         if not distance[now]:
#             distance[next_location].append(cost)
#         else:
#             distance[next_location].append(cost)
#             distance[next_location].sort()
#         q.append([cost,next_location])

# for i in range(1,n+1):
#     if not distance[i]:
#         print(-1)
#     else:
#         print(distance[i][k-1])
