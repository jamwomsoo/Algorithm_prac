n,m =map(int, input().split())
arr= [list(map(int, input().split())) for _ in range(n)]


new_arr = [[0]*n for _ in range(m)]
for i in range(n):
    for j in range(m):
        print(m-j-1,n-i-1)
        new_arr[j][n-i-1] = arr[i][j] 
print(new_arr)