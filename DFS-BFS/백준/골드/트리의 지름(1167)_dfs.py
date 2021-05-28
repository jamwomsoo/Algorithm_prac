

V = int(input())
tree = [[] for _ in range(V+1)]
for i in range(V):
    tmp = list(map(int ,input().split()))
    num= tmp[0]
    tmp = tmp[1:-1]
    for i in range(0,len(tmp),2):
        tree[num].append([tmp[i],tmp[i+1]])
def dfs(num,cost,arr):
    global V
    
    for ele,value in tree[num]:
        if arr[ele]  == int(1e9):
            arr[ele] = value+arr[num] 
            dfs(ele,cost+value,arr)
    return
distance = [int(1e9)]*(V+1)
distance[1] = 0
dfs(1,0,distance)

start = distance.index(max(distance[1:]))
distance1 = [int(1e9)]*(V+1)
distance1[start] = 0
dfs(start,0,distance1)

print(max(distance1[1:]))