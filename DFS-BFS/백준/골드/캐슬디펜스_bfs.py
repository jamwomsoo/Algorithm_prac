from itertools import combinations
from copy import deepcopy
from collections import deque
n, m ,d =map(int, input().split())
m_ls = [i for i in range(m)]
arr = [list(map(int,input().split())) for _ in range(n)]
coms = list(combinations(m_ls,3))
_max = -int(1e9)


def bfs(array,c):
    global n,m,d
    tmp = []
    for i in range(n):
        for j in range(m):
            if array[i][j] == 1 and n-i + abs(c-j) <= d:
                tmp.append([n-i + abs(c-j),i,j])
    if tmp:
        tmp.sort(key = lambda x : (x[0],x[2]))
        return (tmp[0][1],tmp[0][2])
    return None
def move_enemy(array):
    global n,m
    for i in range(n-1,-1,-1):
        for j in range(m-1,-1,-1):
            if array[i][j] == 1:
                if i+1>=n:
                    array[i][j]=0
                else:
                    array[i+1][j],array[i][j] = array[i][j],0
    _sum = 0
    for i in range(n):
        _sum+=sum(array[i])
    if _sum == 0: return False
    return True    
def game_play(com):
    global _max,n,m,arr 
    array = deepcopy(arr)
    cnt = 0
    while True:
        s = set()
        
        for c in com:
            tmp = bfs(array,c)
            if tmp != None:
                s.add(tmp)
        cnt+=len(s)
       
        for x,y in s:
            array[x][y] = 0
        tmp = move_enemy(array)
        if not tmp:    
            _max = max(_max, cnt)
            return 
        

for com in coms:
    game_play(com)

print(_max)



        