# 0에서 시작해서 0에서 가장 먼곳을 찾는다
# 0에서 가장 먼곳을 start라 할때 start 부터 가장 먼곳을 찾아서 그 곳의 가중치가 정답
import sys
sys.setrecursionlimit(10001)
n = int(input())
graph = [[] for _ in range(n)]
for i in range(n-1):
    parent, child, weight = map(int, input().split())
    graph[parent-1].append([child-1, weight])
    graph[child-1].append([parent-1, weight])
ans = 0

def dfs(num,w_arr):
    global ans
    for t,w in graph[num]: 
        if w_arr[t] == 0:
            w_arr[t] = w_arr[num] + w
            dfs(t,w_arr)

weight = [0]*n
dfs(0,weight)
weight[0] = 0
start = weight.index(max(weight))
weight2 = [0]*n
dfs(start,weight2)
weight2[start] = 0

print(max(weight2))