n, m = map(int,input().split())
arr = []

def turn_right_rotate_90(arr):
    n = len(arr) # 세로
    m = len(arr[0]) # 가로
    new_arr = [[0]*n for _ in range(m)]
    
    for i in range(n):
        for j in range(m):
            new_arr[j][n-i-1] = arr[i][j]
    return new_arr

def make_techro(i,j,num):
    if num == 1:
        tmp = list([[i,j], [i, j+1],[i, j+2], [i, j+3]])
    if num == 2:
        tmp = list([[i,j], [i,j+1], [i+1, j], [i+1,j+1]])
    if num == 3:
        tmp = list([[i,j], [i+1, j], [i+2, j], [i+2, j+1]])
    if num == 4:
        tmp = list([[i, j], [i+1, j], [i+1, j+1], [i+2, j+1]])
    if num == 5:
        tmp = list([[i, j], [i, j+1], [i, j+2], [i+1, j+1]])
       
    return tmp
    
def check_over(arr,n,m):
    for x,y in arr:
        if 0 > x or x >= n or 0 > y or y >= m:
            return False
    return True

def tmp_sum(arr, tmp):
    _sum = 0
    for x,y in tmp:
        _sum += arr[x][y]
    return _sum
    

def check_max(arr,num): 
    n = len(arr)
    m = len(arr[0])
    _max = 0
    for i in range(n):
        for j in range(m):
            
            tmp = make_techro(i,j,num)
            if i ==2 and j == 0:
                print(tmp)
            if not check_over(tmp,n,m):
                continue
            
            _sum = tmp_sum(arr,tmp)
            if i ==2 and j == 0:
                print(tmp, _sum)

            _max = max(_max, _sum)
    return _max
def symmetry(arr):
    n = len(arr)
    m = len(arr[0])
    new_arr = [[0]*m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            new_arr[i][j] = arr[i][m-1-j]
    return new_arr    

for i in range(n):
    arr.append(list(map(int,input().split())))

result = 0
for i in range(3):
    arr = turn_right_rotate_90(arr)
#arr = symmetry(arr)
print()
for i in range(len(arr)):
    for j in range(len(arr[0])):
        print(arr[i][j], end = " ")
    print()

result = max(result,check_max(arr,5))

print(result)

print()