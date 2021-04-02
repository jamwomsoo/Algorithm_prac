def solution(n, results):
    answer = 0
    graph = [[int(1e9)]*n for _ in range(n) ]
    for a,b in results:
        graph[a-1][b-1] = 1
    for i in range(n):
        for j in range(n):
            if i == j:
                graph[i][j] = 0
    for k in range(n):
        for i in range(n):
            for j in range(n):
                graph[i][j] = min(graph[i][j],graph[i][k]+graph[k][j])
    for i in range(n):
        tmp = 0
        for j in range(n):
            if graph[i][j] != int(1e9) or graph[j][i] != int(1e9):
                tmp+=1
        if tmp == n:
            answer+=1

    return answer
print(solution(5,[[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]))