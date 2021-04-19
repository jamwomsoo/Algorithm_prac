n = int(input())
arr = []
tmp = [ i for i in range(1,n+1)]
arr.append(tmp)
tmp = [int(input()) for _ in range(n)]
arr.append(tmp)

ans =[]
def dfs(index,top,bottom):
    global n
    if arr[0][index] in top:
        if sorted(top) == sorted(bottom):
            ans.extend(top) 
    else:
        top.append(arr[0][index])
        bottom.append(arr[1][index])
        dfs(arr[1][index]-1,top,bottom)      
        
for i in range(n):
    if arr[0][i] not in ans:
        dfs(i,[],[])

print(len(ans))
ans.sort()
for i in ans:
    print(i)