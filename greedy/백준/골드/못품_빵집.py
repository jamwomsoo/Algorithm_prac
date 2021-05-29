# 못품
# 백준 사이트 :
# 핵심 아이디어 & 알고리즘
# -> 해당 구간에 파이프를 넣으려고 할때 두가지 경우의 수가 생긴다(해당 구간에 파이프라인을 넣어서 목적지 도착, 실패) 
# -> 1. 해당 구간에 파이프를 넣었을때 목적지까지 도착한 경우
#       해당 구간에 파이프가 이미 있어서 다른 파이프는 접근불가
# -> 2. 해당 구간에 파이프를 넣었을때 목적지까지 실패한 경우
#      해당 구간은 이미 다른 경로에서 실패한 구간이다, 그러므로 해당 구간을 통해서 지나갈때 역시 실패할 것이므로 방문하면 안된다
# ======> 한번 방문한 구간을 다시 방문하지 않는다
#  
# 이문제는 dfs로 풀어야한다
# BFS로 풀게되면 가는 경로가 막힐 수 있다(한 열에서 확실히 파이프라 지나가는 경로가 아니여도 막힐 수 있음)
# visited에 append()하는 것보다 visted 이차배열을 만들어서 교환하는게 더 빠르다
direction = [(-1,1),(0,1),(1,1)]
R,C = map(int, input().split())
board = [list(map(str, input())) for _ in range(R)]
ans = 0

visited = [[0]*(C) for _ in range(R)]
def dfs(x,y):
    global R,C
    if y == C-1:
        return True
    
    for dx,dy in direction:
        nx,ny = x+dx,y+dy
        if 0 <= nx < R and 0 <= ny < C and board[nx][ny] == '.' and visited[nx][ny] == 0:
            visited[nx][ny] = 1
            if dfs(nx,ny): 
                return True
    return False

for i in range(R):
    if dfs(i,0):
        ans+=1
    
print(ans)    
        