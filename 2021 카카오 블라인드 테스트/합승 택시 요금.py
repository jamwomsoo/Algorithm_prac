# 1. 각 노드간의 간선을 입력하여 그래프를 그려준다
# 2. 플로이드 웨셜로 각 노드간의 최단거리를 구해준다
# 3. s로 시작해서 k를 거쳐 각각 a,b로
# 효율성을 향상 시킬려면
# ->  @ 0  1  2  3  4  5
#     0 0  63 41 10 24 25
#     1 63 0  22 66 46 48
#     2 41 22 0  51 24 26 
#     3 10 66 51 0  34 35
#     4 24 46 24 34 0  2
#     5 25 48 26 35 2  0   일때
#       *  *  *  *  *  *
#          *  *  *  *  *
#             *  *  *  *
#                *  *  *
#                   *  *
#                      *  
# 이 부분만으로 최단 거리를 구해주고 반대 인덱스에 복사해준다(ex. graph[i][j] = min ; graph[j][i] = graph[i][j] )
# (그러면 돌아야하는 인덱스 수가 반으로 줄어든다)
 
 
def solution(n, s, a, b, fares):
    answer = int(1e9)
    graph = [[int(1e9)]*(n+1) for _ in range(n+1)]
    for i in range(1,n+1):
        for j in range(1,n+1):
            if i == j:
                graph[i][j] = 0
    for fare in fares:
        _a,_b,f = fare
        graph[_a][_b] = f
        graph[_b][_a] = f

    for k in range(1,n+1):
        for i in range(1,n+1):
            for j in range(i,n+1):
                if i!= j:
                    graph[i][j] =  min(graph[i][j],graph[i][k]+graph[k][j])
                    graph[j][i] = graph[i][j]
    
    for k in range(1,n+1):
        
        answer = min(answer, graph[s][k]+graph[k][a]+graph[k][b])
    return answer

print(solution(6,4,6,2,[[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]]))