import sys


def check(x,y,visited):
    if (x,y) in visited and visited[(x,y)] is True:
        return True
    return False

def dfs(n,x,y,direction,visited):
    if n<0:
        return 1
    # 이미 들린경로인지 확인
    if check(x,y,visited):
        return 0
    visited[(x,y)] = True
    ret = 0
    for dx,dy, PROB in direction:
        ret+=PROB*dfs(n-1,x+dx,y+dy,direction,visited)
    visited[(x,y)] = False
    return ret

def solve(n,direction,visited):
    return dfs(n,0,0,direction,visited)/(100**(n+1))

def main():
    n,p_e,p_w,p_s,p_n = map(int, sys.stdin.readline().split())
    visited = {}
    direction = (0,-1,p_e),(0,1,p_w),(1,0,p_s),(-1,0,p_n)
    print(solve(n,direction,visited))
main()