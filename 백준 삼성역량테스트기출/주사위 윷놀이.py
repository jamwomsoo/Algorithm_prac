# 백준 17825
# https://rhdtka21.tistory.com/91참고
# 너무너무 어렵다...
import sys
input = sys.stdin.readline
dice = list(map(int, input().split()))
horse = [(0,0) for _ in range(4)]
board = []
board.append([i*2 for i in range(21)]+[0])
board.append([10,13,16,19])
board.append([20,22,24])
board.append([30,28,27,26])
board.append([25,30,35,40,0])
ans = -int(1e9)

def solution(total,index):
    global ans
    if index == 10:
        ans = max(ans,total)
        return
    for horseNum,ls in enumerate(horse):
        #현재위치
        branch, location = ls
        if (branch,location) == (0,21) or (branch,location) == (4,4):
            continue
        nxtLocation = dice[index]+location
        nxtbranch = 0
        if branch == 0:
            if nxtLocation >=22:
                nxtLocation =21
                nxtbranch = branch
            elif board[branch][nxtLocation] == 10:
                nxtbranch = 1
                nxtLocation = 0
            elif board[branch][nxtLocation] == 20:
                nxtbranch = 2
                nxtLocation = 0
            elif board[branch][nxtLocation] == 30:
                nxtbranch = 3
                nxtLocation = 0
            else:
                #가지는 그대로
                nextBranch = branch
        elif branch == 1 or branch == 2 or branch == 3:
            if nxtLocation >= len(board[branch]):
                nxtbranch = 4
                nxtLocation = nxtLocation-len(board[branch])
            else:
                nxtbranch= branch
        elif branch == 4:
            if nxtLocation>=len(board[branch])-1:
                nxtLocation = len(board[branch])-1
                nxtbranch = 4
            else:
                nxtbranch = branch

        if (nxtbranch,nxtLocation) == (0,21) or (nxtbranch,nxtLocation) == (4,4):
            horse[horseNum] = (nxtbranch,nxtLocation)
            solution(total+board[nxtbranch][nxtLocation],index+1)
            horse[horseNum] = (branch,location)
            continue
        if (nxtbranch,nxtLocation) in horse:
            continue
        if (nxtbranch,nxtLocation) == (0,20) and (4,3) in horse:
            continue
        if (nxtbranch,nxtLocation) == (4,3) and (0,20) in horse:
            continue
        horse[horseNum] = (nxtbranch,nxtLocation)
        solution(total+board[nxtbranch][nxtLocation],index+1)
        horse[horseNum] = (branch,location)




solution(0,0)
print(ans)
