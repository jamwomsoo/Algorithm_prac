# 못품
# 백준 사이트 : https://www.acmicpc.net/problem/10217
# 해설 : https://hooongs.tistory.com/288
# 다익스트라로 풀려했지만 못품
# dp로 풀었음
 
# 풀이 
# [도착 공항][드는 비용]으로 된 이차열 배열 DP를 만든다
# 각각의 공항에 0~M 비용으로 도착 공항 1번부터 N번까지 마다 올 수 있는 거리를 비교해서 최단거리를 저장한다.
# (한 공항으로 올 수 있는 경로가 여러개일 수 있으므로 비용당 거리비교가 필요하다)
for _ in range(int(input())):
    N,M,K = map(int, input().split())
    graph = [[] for _ in range(N+1) ]
    dp = [[int(1e9)]*(M+1) for _ in range(N+1)]

    for i in range(K):
        u,v,c,d = map(int, input().split())
        graph[u].append([v,c,d])
    
    dp[1][0] = 0
    for money in range(0,M+1):
        for now in range(1,N+1):
            if dp[now][money] == int(1e9): continue
            h_dis = dp[now][money]

            for ele,cost,time in graph[now]:
                if money + cost > M: continue
                dp[ele][money+cost] = min(dp[ele][money+cost],time + h_dis)
    answer = min(dp[N])
    print("Poor KCM" if answer == int(1e9) else answer) 
            